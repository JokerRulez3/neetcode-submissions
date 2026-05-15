class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "" or s == None:
            return True
        
        s_lower = s.lower()
        s_cleaned = re.sub(r'[\W_]+', '', s_lower)

        if s_cleaned == s_cleaned[::-1]:
            return True
        else:
            return False
    
        