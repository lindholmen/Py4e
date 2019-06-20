class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            j = i + 1
            while j <= len(nums)-1:
                if target == (nums[i] + nums[j]):
                    return [i,j]
                j = j+1

class Solution2:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            remain_to_get = target - nums[i]
            if remain_to_get in nums:
                ct = nums.count(remain_to_get)
                if ct == 1 and remain_to_get == nums[i]:
                    continue
                else:
                    j = nums.index(remain_to_get,i+1)
                    return [i,j]

class Solution3:
    def twoSum(self, nums, target):
        mydict = {}
        for i in range(len(nums)):
            if target-nums[i] not in mydict:
                mydict[nums[i]]=i
            else:
                return [mydict[target-nums[i]],i]

nums = [3,3]
print(nums)
target = 6
s = Solution3()
print(s.twoSum(nums,target))


def test(A,B):
    return A + 1 if A > B else A - 1

c = test(4,3)
print(c)
c = test(3,4)
print(c)