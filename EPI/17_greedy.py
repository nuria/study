#!usr/local/bin/python


def make_change(cents, coins=[100, 50, 25, 10, 5, 1]):
    # make miopic decisions hoping that it will all work out
    # find out a way to give a customer an amount with the fewest number of coins.
    # choose the highest coin you can choose at any one time
    change_amount = 0
    change = []
    while (cents -change_amount) > 0:
        # coins are sorted so choose the biggest one you can
        print cents
        for c in coins:
            if cents % c ==0:
                change.append(c)
                break
        change_amount = sum(change)

    return change

# design an algorithm that takes as inputs a set of tasks and returns an optimun assigment
# each worker must be assigned exactly two tasks
def task_assignation(duration =[5,2,1,6,4,4]):
    # is an optimun strategy to assign the top and bottom of list
    # return list of tasks in pairs
    # two pointers
    tasks = []
    last = len(duration)-1

    for i in  range(0, len(duration)/2):
        tasks.append((duration[i], duration[last-i]))

    return tasks

# given service times for  aset of queries, compute a schedule for processing
# the queries that minimizes the total waiting time
# waiting time for a query is the time it waits until
# its turn is called
def sql_time(lengths):
    # how can we make the total waiting time the smallest
    lengths = sorted(lengths)

    _sum = 0
    time = 0
    for l in lengths[0:len(lengths)-1]:
        time += _sum +l
        _sum = _sum + l

    return time


if __name__== "__main__":

    print make_change(20)
    print task_assignation([5,2,1,6,4,4])
    # solution for this case is 10
    print sql_time([2,5,1,3])

