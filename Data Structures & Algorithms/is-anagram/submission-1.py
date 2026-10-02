class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        hash_count_s={}
        hash_count_t={}
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if i in hash_count_s:
                    hash_count_s[i] = hash_count_s[i] + 1
                else:
                    hash_count_s[i] = 1
            for i in t:
                if i in hash_count_t:
                    hash_count_t[i] = hash_count_t[i] + 1
                else:
                    hash_count_t[i] = 1
            if hash_count_t == hash_count_s:
                return True
            else:
                return False
        
                
        


        