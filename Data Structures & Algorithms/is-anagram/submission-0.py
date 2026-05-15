class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        countS = Counter(s)
        countT = Counter(t)

        for key in countS.keys():
            if (countT[key] == None or countT[key] != countS[key]):
                return False

        return True
        