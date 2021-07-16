import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    notification = 0
    count = 0
    list1 = sorted(expenditure[0:d])
    sub = expenditure[d:]
    for i in sub:
        if d%2!=0:
            median=list1[d//2]
        else:
            median=(list1[d//2]+list1[(d//2)+1])//2
        if i >= 2 * median:
            notification += 1
        list1.pop(bisect.bisect_left(list1,expenditure[count]))
        count+=1
        bisect.insort(list1, i)
    return notification



first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
expenditure = list(map(int, input().rstrip().split()))
result = activityNotifications(expenditure, d)
print(result)