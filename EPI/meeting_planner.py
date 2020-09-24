#/usr/local/bin/python
# coding: utf-8
"""
Implement a function meetingPlanner that given the availability,
slotsA and slotsB, of
two people and a meeting duration
dur, returns the earliest time slot that works for both of them and is of duration dur
Times are disjointed, taht is intervals for 1 person do not overlap

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: []


"""

def meeting_planner(slotsA, slotsB, dur):

    # first make sure

    # let's walk both arrays at the same time, try to match first interval with first interval

    pA = 0
    pB= 0

    result = []
    while  pA < len(slotsA) and pB < len(slotsB):
        # try first to first and update each side
        startA = slotsA[pA][0]
        startB= slotsB[pB][0]
        endA = slotsA[pA][1]
        endB = slotsB[pB][1]


        if startA <=startB and endA>= startB:
            if  startB + dur <= endB and startB + dur <= endA:
                result = [startB,startB+ dur]
                break
            else:
                # increment A
                pA += 1

        elif startB <= startA and endB >= startA:
            if startA + dur <= endA and startA + dur <= endB:
                result = [startA, startA + dur]
                break
            else:
                pB += 1

        else:
            # intervals do not overlapp at all
            if startA < startB:
                pA+=1
            else:
                 pB+=1


    return result





if __name__=="__main__":

    print meeting_planner([[10,50], [60,120],[140,210]],[[0,15],[60,70]] ,8)

    print meeting_planner([[10,50],[60,120],[140,210]],[[0,15],[60,70]], 12)

