#!usr/local/bin

f = open ('./input1.txt');

calories = {}

current_cal = 0 
max_cal = 0

total_cals= []

for l in f:
    #print l.strip()
    if l.strip()=="":
        # start counting again
        if current_cal > max_cal:
            max_cal = current_cal
        total_cals.append(current_cal)
        current_cal  = 0
    else:
        current_cal = current_cal + int(l)
    


print "max"
print max_cal

total_cals.sort(reverse=True)

print "3 max"
print total_cals[0] 
print total_cals[1]
print total_cals[2]

total = total_cals[0] + total_cals[1] + total_cals[2]

print total
