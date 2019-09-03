use nuria;

drop table if exists model_training_data_tmp;

-- the number of sessions has to be the same for both datasets 
-- we choose "user" pageviews from user dataset plus "automated"
-- pageviews from "bots" dataset


-- Although model does not need sessionId we include it as a way to be able to order data arbitrarily

create table model_training_data_tmp
    as  
    select * from classifier_training_data_human_sorted_processed where label="user" limit 2000 
    UNION ALL
    select * from classifier_training_data_bot_sorted_processed where label="automated" limit 2000;


drop table if exists model_training_data;

create table model_training_data
    as 
    select sessionId, session_length_secs, number_of_pageviews, pageview_ratio_per_min,nocookies,user_agent_length, label  
    from model_training_data_tmp;


drop table if exists  model_training_data_tmp;


-- now use the data we have labeled from general pageviews as testing data

drop table if exists model_testing_data_tmp;

create table model_testing_data_tmp
    as 
    -- make sure to exclude self-reported bots with little traffic
    select * from classifier_data_sorted_processed where label="user" and agent_type="user" limit 2000
    UNION ALL
    select * from classifier_data_sorted_processed where label="automated"  limit 2000;

drop table if exists model_testing_data;

create table model_testing_data 
    as 
    select sessionId, session_length_secs, number_of_pageviews, pageview_ratio_per_min,nocookies,user_agent_length, label
    from model_testing_data_tmp;

drop table if exists model_testing_data_tmp;




