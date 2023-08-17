class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n
        prev_time = 0
        for log in logs:
            funtion_id, typ, time = log.split(":")
            funtion_id = int(funtion_id)
            time = int(time)
            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(funtion_id)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans