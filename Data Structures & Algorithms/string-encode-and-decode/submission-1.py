class Solution:

    def encode(self, strs: List[str]) -> str:
        lengthlist = []
        print(strs)
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+ "#" + strs[i]
        print(strs)
        toReturn = ""
        for i in range(len(strs)):
            toReturn = toReturn + strs[i]
        return toReturn
        

    def decode(self, s: str) -> List[str]:
        toReturn = []
        i = 0
        while i < len(s):
            j = i
            word = ""
            while s[j] != "#":
                word = word + s[j]
                j += 1
            length = int(word)
            i = j + 1
            j = i + length
            toReturn.append(s[i:j])
            i = j
        

        return toReturn
