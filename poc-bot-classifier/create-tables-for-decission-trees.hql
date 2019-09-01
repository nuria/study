use nuria;

drop table if exists model_training_data_tmp;

-- the number of sessions has to be the same for both datasets 
-- we choose "user" requests from user dataset plus "automated"
-- requests from "bots" dataset

create table model_training_data_tmp
    as  
    select * from classifier_training_data_human_sorted_processed where label="user" limit 2000 
    UNION ALL
    select * from classifier_training_data_bot_sorted_processed where label="automated" limit 2000;


drop table if exists model_training_data;

create table model_training_data
    as 
    select session_length_secs, number_of_requests, request_ratio_per_min,nocookies,user_agent_length, label  
    from model_training_data_tmp;


drop table model_training_data_tmp;
