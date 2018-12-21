#scp nuria@stat1007.eqiad.wmnet:~/workplace/classifier_bots/*

1 . Loading of data and sessionize 
        select_testing_data.hql, uses webrequest (pageviews plus edit requests) and  eventlogging data, we are iniotally selecting 1 day word of data 


2. Label in external tables sessions according to a critera
    select_mark_bot_traffic_due_tofrequency.hql


3. Negative sets:
    - apps data (mostly a human dataset)
    - requests detected as bot that appear more than 5 times in our time period

    Once we have marked our "negative" datasets, see how many records are: 
    
    1) not labeled 
    
    2) label as human on human dataset 
                
    3) label as bot on bot dataset


Notes: 
select count(*) from classifier_testing_data_labeled_bot_sorted as bot_sessions join  classifier_testing_data_labeled_bot_model_result labels where labels.sessionId=bot_sessions.sessionId  and labels.label="user";

select count(*) from classifier_testing_data_human_sorted as humans  join  classifier_testing_data_human_model_result labels where labels.sessionId=humans.sessionId  and labels.label="user"

Look at pages newly classified as bots:
select count(*) from classifier_data_one_hour_sorted as bot_sessions join  classifier_data_labeled_one_hour labels where labels.sessionId=bot_sessions.sessionId  and labels.label="bot" and labels.agent_type!="spider";


https://en.wikipedia.org/wiki/Predictive_analytics#Classification_and_regression_trees_.28CART.29
