class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length=len(nums)
        hashlist={}
        for i in range(length):
            if nums[i] not in hashlist:
                hashlist[nums[i]]=i
            else:
                if i-hashlist[nums[i]]<=k:
                    return True
                else:
                    hashlist[nums[i]]=i

        return False