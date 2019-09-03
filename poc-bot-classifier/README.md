#scp nuria@stat1007.eqiad.wmnet:~/workplace/classifier_bots/*

GOAL: 
The goal of this project is to label as"automated" the traffic spikes caused by bots 
that distort our pageview numbers so labeling of bots by this algorithm
is done mostly by calculating request frequencies. We also calculate additional features like
user_agent_length nad the number of requests from an entity with nocookies = 1.


We get 1 day of webrequest pageview data (we call this our test dataset) and we calculate pseudo sessions for the purpose
of identifying entities that do too-many requests in a given time period. 
The bot identification works on a dataset in which pageviews have already been refined.

The most complicated part of this is to come up with the "labeled" datasets, for the "human"
data we have used data from apps with app-install-ids which contains very few automated requests.
For the "bot" labeled data we have used pageviews tagged as "spider" (self-reported-bots). This data also includes a fair amount of requests
at low volume by "good" bots. We have run these datasets through a simplistic model to further classify requests as user or automated as the user dataset 
contains for sure a significant amount of automated data. This model further labels the data to "user" or "automated". Then, after running our original data
through the simplistic labeling we choose 2000 records from each set of sessions, only the ones that have been labeled as "user" from teh mobile data
and the ones that have been labeled as "automated" from the self-reported bots. 

As last step we feed this data to a decision-tree based prediction model.






_sorted tables indicate sessions
_sorted_processed is really labeled data 


Notes: 
hive -f select_mark_automated_traffic.hql -d input_table=classifier_data_sorted -d output_table=classifier_data_sorted_processed
hive -f select_mark_automated_traffic.hql -d input_table=classifier_training_data_human_sorted -d output_table=classifier_training_data_human_sorted_processed
hive -f select_mark_automated_traffic.hql -d input_table=classifier_training_data_bot_sorted -d output_table=classifier_training_data_bot_sorted_processed



https://en.wikipedia.org/wiki/Predictive_analytics#Classification_and_regression_trees_.28CART.29
