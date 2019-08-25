use nuria;

drop table if exists model_training_data_tmp;

-- the number of sessions has to be the same for both datasets 
-- you need to count that there is at least 5000, which is the number 
-- we have choosen as there seems to be arround 7000 bots sessions (with high request rate)
-- any day

create table model_training_data_tmp
    as  
    select * from classifier_training_data_human_sorted_processed limit 5000 
    UNION ALL
    select * from classifier_training_data_bot_sorted_processed limit 5000;


drop table if exists model_training_data;

create table model_training_data
    as 
    select session_length_secs, number_of_requests, nocookies, label  
    from model_training_data_tmp;
