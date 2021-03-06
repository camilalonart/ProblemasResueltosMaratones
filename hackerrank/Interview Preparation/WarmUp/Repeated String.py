#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ocurrencesInS = s.count('a')
    theSum = ocurrencesInS * int((n/len(s)))
    positionSubstring = n%len(s)
    substring = s[0:positionSubstring]
    theSum += substring.count('a')
    return int(theSum)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
