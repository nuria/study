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
        -- weblight data is a mess
        when user_agent like '%weblight%' then 'user'
        -- less than n pageviews per time period, p90 on 1 day of human dataset is actually 8 but it is mobile data
        -- p99 is ~30$
        when count(*) < 10 then 'user' 
        -- more than N pageviews per time-period p95 of bot dataset for 1 day is 800
        when count(*) > 800 then 'automated'
        -- more than 10 pageviews with nocookies, old phones do not manage cookies nor google weblight    
        when sum(coalesce(nocookies, 0L)) > 10    then 'automated' 
        -- threshold for bots at N pageviews per min, pretty high 
        when cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) >= 30 then 'automated'
        -- shortest of what seem like true browsers are strings like'Opera/8.01 (Windows NT 5.1)'
        when length(user_agent) > 400 or length(user_agent) < 25 then 'automated'
        -- low pageview ratios as low as 1 per min
        when cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) = 0 then 'user'
    end as label

from
    ${input_table} 
group by 
    sessionId, agent_type, user_agent;





