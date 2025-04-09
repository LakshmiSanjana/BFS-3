#  https://leetcode.com/problems/remove-invalid-parentheses/


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0

            for i in s:
                if i == "(":
                    count += 1
                elif i == ")":
                    count-=1
                    if count < 0:
                        return False
            return count == 0

        
        q = deque([s])
        visited = set()
        found = False
        res = []

        while q:
            len_q = len(q)

            for _ in range(len_q):
                curr = q.popleft()
                if is_valid(curr):
                    res.append(curr)
                    found = True
                
                if found:
                    continue
                
                for i in range(len(curr)):
                    if curr[i].isalpha():
                        continue
                    
                    baby_str = curr[:i] + curr[i+1:]
                    if baby_str not in visited:
                        q.append(baby_str)
                        visited.add(baby_str)
            
            if found:
                break
        
        return res if res else [""]

# TC: O(2^n * n) 2^n for all combinations and n for is valid
# SC: O(2^n * n) q, visited, res - 2^n and each string is of length upto n