import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ab=arr[:]
    arr.remove(max(arr))
    ab.remove(min(ab))
    print(sum(arr), sum(ab))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
