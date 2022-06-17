#997

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
#                [BeTrustedNum, TrustOtherNum]
        person = [[0, 0] for i in range(n + 1)]

        for i in trust:
            a, b = i
#           有信任別人就加1
            person[a][1] += 1
#           有被人信任就加1
            person[b][0] += 1

        for i in range(1, n + 1):
#           滿足不信任其他人 和 被全部的人信任，則為法官
            if person[i][1] == 0 and person[i][0] == n - 1:
                return i
            
        return -1

