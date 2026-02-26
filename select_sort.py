class Solution: 
    def selectionSort(self, arr):
        #code here
       
        n = len(arr)
    
      
        for i in range(n):
              
            imin = i
            for j in range(i+1, n):
                 if arr[j] < arr[imin]:
                    imin = j
            temp = arr[i]
            arr[i] = arr[imin];
            arr[imin] = temp;
         
      

