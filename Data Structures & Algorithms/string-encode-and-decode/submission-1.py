class Solution:

    def encode(self, strs: List[str]) -> str:


        encoded_str = ""

        for s in strs:
            l = len(s)
            encoded_str += str(l) + ","
            
        encoded_str += "#"  

        for s in strs:
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        pos = []
        decoded_str = []
        
        j = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                break
            if s[i] == ",":
                pos.append(int(s[j:i]))
                j = i+1
            i += 1

        for p in pos:
            decoded_str.append(s[i:i+p])
            i += p 

        return decoded_str










