#!/usr/bin/python

# Mapper will print the largest forum posts
# id"    "title" "tagnames"  "author_id" "body"  "node_type" "parent_id" "abs_parent_id"

import sys
import csv
import heapq as heapq

# stores top ten longest form posts this mapper is processing
# by id, so we can evict them as needed


# heap, since it is a minimun heap we store negative lengths
h = []

# read data as csv
# this is how the file looks
'''
"id"    "title" "tagnames"      "author_id"     "body"  "node_type"     "parent_id"     "abs_parent_id" "added_at"      "score" "state_string"  "last_edited_id"        "last_activity_by_id"   "last_activity_at"      "active_revision_id"    "extra" "extra_ref_id"  "extra_count"   "marked"
'''
reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    body = line[4]

    # it is a minimun heap so we are storing negative lengths
    # to retrieve largests posts
    l = len(body)*-1
    # add to heap
    heapq.heappush(h, (l, line[0]))

# heap is populated, pop 10 items
# store temporarily as we need to print in reverse order
ids = []
for i in range(0, 10):
    l, _id = heapq.heappop(h)
    l = l *(-1)
    ids.append((l,_id))

# revert to print in reverse order (shortest 1st)
ids.reverse()

for item in ids:
    post_id = item[1]
    l = item[0]
    print "{0}\t{1}".format(post_id,l)

#for l in lines:
 #   writer.writerow(l)
