#scp nuria@stat1007.eqiad.wmnet:~/workplace/classifier_bots/*

We get 1 day of webrequest pageview data (we call this our test dataset) and we calculate pseudo sessions for the purpose
of identifying entities that do too-many requests in a given time period

So, the bot identification works on a dataset in which pageviews have already been refined. From those pseudo-sessions are calclated.

How do we identify bots?
The goal of this project is to label as"automated" the traffic spikes caused by bots
that distort our pageview numbers so labeling of bots by this algorithm 
is done mostly by calculating request frequencies.



The most complicated part of this is to come up with the "labeled" datasets, for the "human"
data we have used data from apps with app-install-ids which contains very few automated requests.
For the "bot" labeled data we have used pageviews tagged as "spider" (self-reported-bots). This data also includes a fair amount of requests
at low volume by "good" bots.


We use some simplistic model to label data from the dataset as "user" or "automated" (the human dataset contains a few automated requests)
and later with the results of this labeling we build a dataset 
that we feed to a decision-tree based prediction model.


_sorted tables indicate sessions
_sorted_processed is really labeled data 


Notes: 
hive -f select_mark_automated_traffic.hql -d input_table=classifier_data_sorted -d output_table=classifier_data_sorted_processed
hive -f select_mark_automated_traffic.hql -d input_table=classifier_training_data_human_sorted -d output_table=classifier_training_data_human_sorted_processed
hive -f select_mark_automated_traffic.hql -d input_table=classifier_training_data_bot_sorted -d output_table=classifier_training_data_bot_sorted_processed



https://en.wikipedia.org/wiki/Predictive_analytics#Classification_and_regression_trees_.28CART.29
