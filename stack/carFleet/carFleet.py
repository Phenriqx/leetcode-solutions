from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {position[i]: speed[i] for i in range(len(position))}
        position.sort(reverse=True)
        stack = []

        for idx in range(len(position)):
            time = (target - position[idx]) / hashmap[position[idx]]
            stack.append(time)
            if len(stack) >= 2:
                if time <= stack[-2]:
                    stack.pop()

        return len(stack)