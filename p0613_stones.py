import random
import numpy as np
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # mathematically, can always win. He can choose to either take every other one (starting from left)
        # or every other one (starting from right). One of these must be larger than the other, so he can win.
        return True

    def test(self):
        res = True
        for i in range(100):
            a = self.makeTest(6)
            res = res and (self.naiveSolve(a,0,0,0,[],[])[0] == self.stoneGame(a))
        return res

    def alphabeta(self, piles, player, p1score, p2score, p1best, p2best):
        if len(piles) == 1:
            v = piles[0]
            d = p1score-p2score
            return d+v if player == 0 else d-v
        else:
            if player == 0:
                if p2score - p1score > (500*np.ceil(len(piles)/2)):
                    return p1score-p2score
                value = -np.inf
                if piles[0] >= piles[-1]:
                    newpiles1 = piles[1:]
                    v1 = piles[0]
                    newpiles2 = piles[:-1]
                    v2 = piles[-1]
                else:
                    newpiles1 = piles[:-1]
                    v1 = piles[-1]
                    newpiles2 = piles[1:]
                    v2 = piles[0]

                a = self.alphabeta(newpiles1, 1, p1score+v1, p2score, p1best, p2best)
                value = max(a, value)
                if value >= p2best:
                    # player 1 will never let us get to this branch
                    return value

                b = self.alphabeta(newpiles2, 1, p1score+v2, p2score, max(p1best, value), p2best)

                return max(b, value)
            else:
                if p1score - p2score > (500*np.ceil(len(piles)/2)):
                    return p1score-p2score
                value = np.inf
                if piles[0] <= piles[-1]:
                    newpiles1 = piles[1:]
                    v1 = piles[0]
                    newpiles2 = piles[:-1]
                    v2 = piles[-1]
                else:
                    newpiles1 = piles[:-1]
                    v1 = piles[-1]
                    newpiles2 = piles[1:]
                    v2 = piles[0]

                a = self.alphabeta(newpiles1, 0, p1score, p2score+v1, p1best, p2best)
                value = min(a, value)
                if value <= p1best:
                    return value

                b = self.alphabeta(newpiles2, 0, p1score, p2score+v2, p1best, min(p2best, value))

                return min(b, value)

    def naiveSolve(self, piles, player, p1score, p2score, p1take, p2take):
        if len(piles) == 0:
            return (p1score - p2score, p1take, p2take)
        else:
            if player == 0:
                a = self.naiveSolve(piles[1:], 1, p1score+piles[0], p2score, p1take+[piles[0]], p2take)
                b = self.naiveSolve(piles[:-1], 1, p1score+piles[-1], p2score, p1take+[piles[-1]], p2take)
                if a[0] >= b[0]:
                    return a
                else:
                    return b
            else:
                a = self.naiveSolve(piles[1:], 0, p1score, p2score+piles[0], p1take, p2take+[piles[0]])
                b = self.naiveSolve(piles[:-1], 0, p1score, p2score+piles[-1], p1take, p2take+[piles[-1]])
                if a[0] <= b[0]:
                    return a
                else:
                    return b

    def makeTest(self, length):
        l = [0]
        while sum(l) % 2 == 0:
            l = [random.randint(1,500) for i in range(length)]
        return l