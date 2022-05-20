class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #### bubble sort--TLE ####
        # for i in range (len(nums) - 1):
        #     swap = False
        #     for j in range(len(nums) - 1 - i):
        #         if nums[j] > nums[j + 1]:
        #             nums[j + 1], nums[j] = nums[j], nums[j + 1]
        #             swap = True
        #     if swap == False:
        #         break
        # return nums
        
        #### select sort ####
        # for i in range(len(nums) - 1):
        #     indexOfMin = i
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[indexOfMin]:
        #             indexOfMin = j
        #     nums[i], nums[indexOfMin] = nums[indexOfMin], nums[i]
        # return nums
        
        #### insert sort ####
        # for i in range(1, len(nums)):
        #     select = nums[i]
        #     j = i - 1
        #     while j >= 0 and nums[j] > select:
        #         nums[j + 1] = nums[j]
        #         j -= 1
        #     nums[j + 1] = select
        # return nums
        
        #### quick sort ####
        # import random
        # if len(nums) == 1:
        #     return nums
        # def quickSort(nums, l, r):
        #     if l < r:
        #         mid = partition(nums, l, r)
        #         quickSort(nums, l, mid - 1)
        #         quickSort(nums, mid + 1, r)
        #         return nums
        # def partition(nums, l, r):
        #     select = nums[random.randint(l,r)]
        #     while l < r:
        #         while l < r and select <= nums[r]:
        #             r -= 1
        #         nums[l] = nums[r]
        #         while l < r and select >= nums[l]:
        #             l  += 1
        #         nums[r] = nums[l]
        #     nums[l] = select
        #     return l
        # return quickSort(nums, 0, len(nums) - 1)
        
        #### merge sort ####
        # def merge(nums, left, middle, right):
        #     sortArray = []
        #     i = left
        #     j = middle + 1
        #     while i <= middle and j <= right:
        #         if nums[i] < nums[j]:
        #             sortArray.append(nums[i])
        #             i += 1
        #         else:
        #             sortArray.append(nums[j])
        #             j += 1
        #     while i <= middle:
        #         sortArray.append(nums[i])
        #         i += 1
        #     while j <= right:
        #         sortArray.append(nums[j])
        #     nums[left : right + 1] = sortArray
        #     return nums
        # def MergeSort(nums, left, right):
        #     if left < right:
        #         middle = (left + right) // 2
        #         MergeSort(nums, left, middle)
        #         MergeSort(nums, middle + 1, right)
        #         merge(nums, left, middle, right)
        #         return nums
        # return MergeSort(nums, 0, len(nums) - 1)
        
        #### heap sort ####
        # def sift(nums, low, high): #low is root, high is boundary
        #     i = low
        #     j = i * 2 + 1
        #     tmp = nums[low]
        #     while j <= high:
        #         if j + 1 <= high and nums[j] < nums[j + 1]:
        #             j += 1
        #         if nums[j] > tmp:
        #             nums [i] = nums[j]
        #             i = j
        #             j = i * 2 + 1
        #         else:
        #             break
        #     nums[i] = tmp
        # def heapSort(nums):
        #     n = len(nums)
        #     #j = n - 1 high
        #     #i = (n - 2) // 2 反过来求父节点
        #     for i in range((n - 2) // 2, -1, -1):
        #         sift(nums, i, n - 1)
        #     #第一次建堆
        #     for i in range(n - 1, -1, -1):
        #         nums[0], nums[i] = nums[i], nums[0]
        #         sift(nums, 0, i - 1)
        # heapSort(nums)
        # return nums
        
        #### heap sort ####
        # def orderLocalHeap(li, curMax):
        #   left = curMax * 2 + 1
        #   right = curMax * 2 + 2
        #   if left > len(li) - 1:
        #     return li
        #   elif right > len(li) - 1:
        #     if li[curMax] < li[left]:
        #       li[curMax], li[left] = li[left], li[curMax]
        #       curMax = left
        #       return orderLocalHeap(li, curMax)
        #     else:
        #       return li
        #   elif li[left] >= li[right] and li[curMax] < li[left]:
        #     li[curMax], li[left] = li[left], li[curMax]
        #     curMax = left
        #     return orderLocalHeap(li, curMax)
        #   elif li[left] < li[right] and li[curMax] < li[right]:
        #     li[curMax], li[right] = li[right], li[curMax]
        #     curMax = right
        #     return orderLocalHeap(li, curMax)
        #   else:
        #     return li
        # def formHeap(li):
        #   for i in range(len(li) - 1, -1, -1):
        #     orderLocalHeap(li, i)
        #   return li
        # def popHeap(li):
        #   n = len(li)
        #   for i in range(n):
        #     li[0], li[~i] = li[~i], li[0]
        #     li[:~i] = orderLocalHeap(li[:~i], 0)
        # formHeap(nums)
        # popHeap(nums)
        # return nums
        
        #### heapq ####
        import heapq
        heapq.heapify(nums)
        ans = []
        for i in range(len(nums)):
            ans.append(heapq.heappop(nums))
        return ans