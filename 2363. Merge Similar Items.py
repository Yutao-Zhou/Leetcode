class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        #### Brute force (Sort and loop) ####
        # ans, i, j, l1, l2 = [], 0, 0, len(items1), len(items2)
        # items1.sort()
        # items2.sort()
        # while i < l1 and j < l2:
        #     if items1[i][0] < items2[j][0]:
        #         ans.append(items1[i])
        #         i += 1
        #     elif items1[i][0] > items2[j][0]:
        #         ans.append(items2[j])
        #         j += 1
        #     else:
        #         ans.append([items1[i][0], items1[i][1] + items2[j][1]])
        #         i += 1
        #         j += 1
        # if i < l1:
        #     ans.extend(items1[i:])
        # if j < l2:
        #     ans.extend(items2[j:])
        # return ans
        
        #### HashTable ####
        ans, hashTable = [], {}
        for item in items1:
            hashTable[item[0]] = item[1]
        for item in items2:
            if item[0] in hashTable:
                hashTable[item[0]] += item[1]
            else:
                hashTable[item[0]] = item[1]
        for key in hashTable.keys():
            ans.append([key, hashTable[key]])
        return sorted(ans)