from traceback import print_tb
import turtle

from certifi import where


print("Belajar menemukan duplikasi number")

def findDuplicate(nums):
    tortoise=nums[0]
    here=nums[0]
    while True:
        tortoise=nums[tortoise]
        here = nums[nums[here]]
        if tortoise==here:
            break

    ptr1 = nums[0]
    ptr2=tortoise
    while ptr1 != ptr2:
            ptr1=nums[ptr1]
            ptr2=nums[ptr2]

    return ptr1


print(findDuplicate([3,1,3,4,2]))