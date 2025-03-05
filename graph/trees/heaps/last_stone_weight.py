"""
1046. Last Stone Weight
Solved
Easy
Topics
Companies
Hint
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
"""




def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    sorted_stones = sorted(stones)

    while len(sorted_stones) > 1:
        s1 = sorted_stones.pop()
        s2 = sorted_stones.pop()

        if s2 != s1:
            stone_to_add = s1 - s2

            for i in range(len(sorted_stones)+1):
                if len(sorted_stones) == i or sorted_stones[i] >= stone_to_add:
                    sorted_stones.insert(i, stone_to_add)
                    break

    return sorted_stones[0] if sorted_stones else 0









stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))