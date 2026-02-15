class Solution:    
    def findUnion(self, a, b):
        # code here
        
        # for i in b:
        #     if i not in a:
        #         a.append(i)
        
        # for i in a:
        #     if a.count(i) > 1:
        #         a.remove(i)
        # return a
        
        
        set_a = set(a)
        set_b = set(b)
        
        result = set_a | set_b
        return result
