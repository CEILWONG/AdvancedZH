# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         outlist=[]
#         hashset=set()
#         for i in nums1:
#             if i in hashset:
#                 pass
#             else:
#                 hashset.add(i)
#
#         for i in hashset:
#             if i in nums2:
#                 outlist.append(i)
#
#         return outlist

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         outlist=[]
#         for i in nums1:
#             if i in nums2:
#                 if i in outlist:
#                     pass
#                 else:
#                     outlist.append(i)
#             else:
#                 pass
#         return outlist

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset=set()
        for i in num1:
            hashset.add(i)