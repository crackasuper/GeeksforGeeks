#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def checkEqual(self,A,B):
        
        if len(A) != len(B):
            return False
            
        return sorted(A) == sorted(B) 
