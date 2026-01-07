class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # queue for r and d
        r = []
        d = []
        n = len(senate)
        for idx in range(n):
            if senate[idx]=='R':
                r+=[idx]
            else:
                d+=[idx]
        
        while r and d:
            r_current = r[0]
            d_current = d[0]
            if r_current < d_current:
                r+=[r_current+n]
            else:
                d+=[d_current+n]
            del d[0]
            del r[0]
        print(r)
        print(d)
        return "Radiant" if r else "Dire"