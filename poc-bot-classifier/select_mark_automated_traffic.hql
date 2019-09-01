-- This is an, ahem, hive script to produce a labeld dataset
-- It works on top of a table that stores pseudo-session data
--- You need to pass an input and output tables
--- like hive -f this.hql -d input_table=classifier_data_sorted -d output_table=classifier_data_labeled

use nuria;


drop table if exists ${output_table};

create table
    ${output_table}
as
select 
    sessionId,
    (unix_timestamp(max(ts)) - unix_timestamp( min(ts))) as session_length_secs,
    count(*) number_of_pageviews,
    cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) as pageview_ratio_per_min,
    agent_type,
    sum(coalesce(nocookies, 0L)) nocookies,
    length(user_agent) user_agent_length,
    case
        -- less than n pageviews per time period
        when count(*) < 10 then 'user'
        -- more than 1000 pageviews per time-period (generous limit, user dataset is less than 1000)
        when count(*) > 1000 then 'automated'
        -- more than 10 pageviews with nocookies in 10 secs  
        when sum(coalesce(nocookies, 0L)) > 10 and (unix_timestamp(max(ts)) - unix_timestamp( min(ts))) <= 10   then 'automated' 
        -- threshold for bots at N pageviews per min, pretty high 
        when cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) >= 20 then 'automated'
        when length(user_agent) > 400 or length(user_agent) < 50 then 'automated'
        -- low pageview ratios as low as 1 per min
        when cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) = 0 then 'user'
   end as label

from
    ${input_table} 
group by 
    sessionId, agent_type, user_agent;





