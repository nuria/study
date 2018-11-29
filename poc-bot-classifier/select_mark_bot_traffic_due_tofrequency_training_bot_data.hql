use nuria;

drop table if exists  classifier_testing_data_labeled_bot_model_result;

create table
    classifier_testing_data_labeled_bot_model_result
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
    nuria.classifier_testing_data_labeled_bot_sorted st
group by 
    st.sessionId, agent_type, user_agent;

-- group by label, ideally most everything is labelled as bot 
--select count(*), label from classifier_training_bot_data_model_result group by label;

-- now join to see true positives (they have to be calculated in requests, not sessions)
-- select count(*), label from classifier_labeled_bot_data_sorted s right join classifier_training_bot_data_model_result l on (s.sessionId=l.sessionid) group by label;




