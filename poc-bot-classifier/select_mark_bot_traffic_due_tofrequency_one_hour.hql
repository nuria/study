use nuria;

drop table if exists classifier_data_labeled_one_hour;

create table
    classifier_data_labeled_one_hour
as
select 
    sessionId,
    (unix_timestamp(max(ts)) - unix_timestamp( min(ts))) as session_length_secs,
    count(*) number_of_requests,
    cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) as request_ratio_per_min,
    agent_type,
    sum(coalesce(nocookies, 0L)) nocookies,
    case
        -- more than 1 request with nocookies in 5 secs  
        when sum(coalesce(nocookies, 0L)) > 1 and (unix_timestamp(max(ts)) - unix_timestamp( min(ts))) > 5   then 'bot' 
        -- threshold for bots at 20 reqs per sec 
        when cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) >= 20 then 'bot'
        when length(user_agent) > 400 then 'bot'
        -- low requests ratios as low as 1 per min
        when cast((count(*)/(unix_timestamp(max(ts)) - unix_timestamp( min(ts))) * 60) as int) = 0 then 'user'
        -- less than n reqs per time period which in this case is a day
        when count(*) < 5 then 'user'
   end as label

from
    classifier_data_one_hour_sorted
group by 
    sessionId, agent_type, user_agent;





