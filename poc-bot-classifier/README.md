#scp nuria@stat1007.eqiad.wmnet:~/workplace/classifier_bots/*

We get 1 day of webrequest pageview data (we call this our test dataset) and we calculate pseudo sessions for the purpose
of identifying entities that do too-many requests in a given time period

So, the bot identification does not work on pageview data but rather on sessions of pageviews

How do we identify bots?

Our basic criteria is to label as bot the automated traffic spikes
that distort our pageview numbers so labeling of bots by this algorithm 
is done mostly by calculating request frequencies.

We do two things. First, we get two datasets that we call "labeled" (human and bot pageviews) 
and we apply this vert simplistic algorithm and (borrowing from ML ideas) we calculate a 
confusion matrix. 

After, we use our "testing" data, 1 day of webrequest pageviews and we see what results we get 
of running that data through the bot detecting algorithm. To be clear the algorithm not a classifier
but rather just a 'criteria to label' that can be used to build a good dataset that can be used as 
the data to train a classifier.



The most ciomplicated part of this is to come up with the "labeled" datasets, for the "human"
data we have used data from apps with app-install-ids which contains very few automated requests.
For the "bot" labeled data we have used pageviews tagged as "spider" (self-reported-bots). This data also includes a fair amount of requests
at low volume by "good" bots.



Notes: 

-- group by label, ideally most everything is labelled as bot
--select count(*), label from classifier_training_bot_data_model_result group by label;

-- now join to see true positives (they have to be calculated in requests, not sessions)
-- select count(*), label from classifier_labeled_bot_data_sorted s right join classifier_training_bot_data_model_result l on (s.sessionId=l.sessionid) group by label;



https://en.wikipedia.org/wiki/Predictive_analytics#Classification_and_regression_trees_.28CART.29
