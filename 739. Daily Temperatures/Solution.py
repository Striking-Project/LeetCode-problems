class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for temp_index in range(len(temperatures)):
            while stack and temperatures[temp_index] > temperatures[stack[-1]]:
                answer[prev_index] = temp_index - (prev_index := stack.pop())
            stack.append(temp_index)
        return answer

with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"[{','.join([str(x) for x in Solution().dailyTemperatures(case)])}]\n")
exit()