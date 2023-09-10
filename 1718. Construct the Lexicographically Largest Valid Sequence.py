class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def construct(start, array, used):
            if start == len(array):
                nonlocal ans
                ans = array
                return True
            
            if array[start] == 0:
                for number in range(n, 0, -1):
                    if number not in used:
                        if number == 1:
                            array[start] = number
                            used.add(number)
                            if construct(start + 1, array, used):
                                return True
                            array[start] = 0
                            used.remove(number)
                        elif start + number < len(array) and array[start + number] == 0:
                            array[start] = number
                            array[start + number] = number
                            used.add(number)
                            if construct(start + 1, array, used):
                                return True
                            array[start] = 0
                            array[start + number] = 0
                            used.remove(number)
            elif construct(start + 1, array, used):
                return True
                
        ans = None
        construct(0, [0] * (n * 2 - 1), set())
        return ans