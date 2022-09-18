class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        #### Count and Build ####
        ans = []
        tableOrder = {}
        allDishes = set()
        for order in orders:
            if int(order[1]) not in tableOrder:
                tableOrder[int(order[1])] = {}
            if int(order[1]) in tableOrder:
                if order[2] in tableOrder[int(order[1])]:
                    tableOrder[int(order[1])][order[2]] += 1
                else:
                    tableOrder[int(order[1])][order[2]] = 1
            allDishes.add(order[2])
        dishes = sorted(list(allDishes))
        ans.append(["Table"] + dishes)
        for table in sorted(tableOrder.keys()):
            cache = [str(table)]
            for dish in dishes:
                if dish in tableOrder[table]:
                    cache.append(str(tableOrder[table][dish]))
                else:
                    cache.append(str(0))
            ans.append(cache)
        return ans