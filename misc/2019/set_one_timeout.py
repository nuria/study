#!/usr/local/bin/python
from collections import deque

from threading import Timer
# set_one_timeout(callback, delay)
# Calls callback function after delay seconds.
# If called a second time before delay is over,
# the first callback is forgotten.

q = deque()

def set_one_timeout(callback, delay):
    # stub implementation
    t = Timer(delay, callback)

# Implement set_timeout(callback, delay),
# which allows to submit "illimited" callbacks.
# You can use set_one_timeout().

def set_timeout(callback, delay):
    global q

    def callback_wrapper(callback):
        # execute callback
        callback()
        # decrement queue, FIFO
        # calls are executed FIFO regardless of delay
        q.popleft()
        # now enque following callback
        if len(q) > 1:
            set_timeout(q[0][0], q[0][1])


    q.append((callback_wrapper, delay))

    if len(q) == 1:
        # nobody is waiting
        set_one_timeout(callback_wrapper, delay)






