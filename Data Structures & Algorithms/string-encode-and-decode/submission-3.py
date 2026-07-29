class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            l = len(s)
            encoded_str += str(l) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        l = ""
        decoded_str = []
        
        while i < len(s):
            if s[i] == "#":
                p = int(l)
                decoded_str.append(s[i+1:i+p+1])
                i += p+1
                l = ""
            else:
                l += s[i]
                i += 1
        
        return decoded_str











