1 . Loading of data and sessionize 
        select_training_data.hql, uses webrequest (pageviews plus edit requests) and  eventlogging data, we are iniotally selecting 1 month word of data 


2. Label in external tables sessions according to a critera
    select_mark_bot_traffic_due_tofrequency.hql


3. Negative sets:
    - apps data (mostly a human dataset)
    - requests detected as bot that appear more than 5 times in our time period

    Once we have marked our "negative" datasets, see how many records are: 
    
    1) not labeled 
    
    2) label as human on human dataset 
                
    3) label as bot on bot dataset
