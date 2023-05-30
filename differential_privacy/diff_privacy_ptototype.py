#!/usr/local/bin

from mwviews.api import PageviewsClient
from datetime import date, datetime, timedelta
import sys
import numpy as np
import math


# running isacc's examples myself to hands-on understand tradeoffs
# tool https://diff-privacy.toolforge.org/ and code https://github.com/geohci/wiki-diff-privacy/blob/main/app.py
# requires python3

def check_bounds(noisedX, sensitivity, eps, alpha=0.5, prop_within=0.25):
    # english : whether with probability .5 the noise added makes the resulting value to be with .25* (real_value) (+/-)
    # checks whether data is within (100* alpha) of its true value
    # WITHOUT using the ground value so .5 *value means data is 50% higher (or lower)
    # we choose for example, 50% probability of being within the 25% of actual value
    # Based on:
    # * Description: https://arxiv.org/pdf/2009.01265.pdf#section.4
    # * Code: https://github.com/google/differential-privacy/blob/main/java/main/com/google/privacy/differentialprivacy/LaplaceNoise.java#L127.
    # noisedX = the count after adding laplace noise
    # sensitivity 
    # epsilon
    # alpha , how confident should we be that noisy data is within 100* prop_within 
    # of true value (0.5 , 50% confidence, 0.1 -> 90% confidence)
    # prop_within: how close do we expect the data to be to the actual value if 0.25 within 25%

    # I am not really getting how can this work w/o using the groundtruth value but I guess since noise is 
    # addded with a set of probabilistic parameters you just need to probabilistically check those 
    # to see how close you are
    # Computes the quantile z satisfying Pr[Y <= z] = rank (complementary of  aprobability density)

    rank = alpha/ 2 # two tailed
    lbda = sensitivity/eps
    # confidence interval, symetric, could be higher or lower
    z = noisedX + abs(lbda * np.log(2*rank))
    #confidence interval
    L = (-1) *z
    R = z

    # this does not use the 0.25% of actual value is rather the actual value 
    print ("noisedX: {0}, z: {1}".format(noisedX,z))
    return (noisedX >z, z) 




def main():
    # alll examples for spanish wikipedia
    p = PageviewsClient(user_agent="nuria@outschool.com")


    try:
        # defaults to yesterday
        groundtruth = p.top_articles(project='es.wikipedia',limit=50)


    except Exceptioni as e:
        print (e)

        two_days_ago = date.today() - timedelta(days=2)
        groundtruth = p.top_articles(project='es.wikipedia',
                                     access='all-access',
                                     year=two_days_ago.year, month=two_days_ago.month, day=two_days_ago.day,
                                     limit=50)

    # RECORDS LOOK LIKE: {'article': 'Andriy_Nesmachniy', 'views': 9162, 'rank': 50}
    #for g in groundtruth:
        #print(g)

    gt_views = {}
    dp_views = {}

    for p in groundtruth:
        gt_views[p['article']] = p['views']


    # now add laplacian noise
    # epsilon
    eps = float(sys.argv[1])
    dp_views = {}
    sensitivity = float(sys.argv[2])
    floor = 0
    
    result = {}

    # see check bound function for what these mean
    alpha = 0.5
    prop_within =0.25

    for page in gt_views.keys():
        views = gt_views[page]
        dpviews = max(floor, round(views + np.random.laplace(0, sensitivity / eps)))
        dp_views[page] = dpviews
        (within_bounds, ci) = check_bounds(dpviews, sensitivity, eps, alpha, prop_within)
        result[page] = {'dp-views':dpviews, 'gt-views':views, 'within_bounds': str(within_bounds)}

    for k in gt_views.keys():
        item = result[k]
        print ("article:{0}, views: {1}, dpviews: {2}, within bounds: {3}".format( k, gt_views[k], dp_views[k], item['within_bounds']))

    print ("epsilon: {0}, sensitivity: {1}".format(eps, sensitivity))


if __name__=="__main__":
    main()
