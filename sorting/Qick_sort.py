def partition(array,l,h): 
    i = ( l-1 )          
    p = array[h]     
  
    for j in range(l, h): 
  
        
        if   array[j] < p: 
    
            i = i+1 
            array[i],array[j] = array[j],array[i] 
  
    array[i+1],array[h] = array[h],array[i+1] 
    return ( i+1 ) 
  
 
def quickSort(a,l,h): 
    if l < h: 
   
        pin = partition(a,l,h)        
        quickSort(a, l, pin-1) 
        quickSort(a, pin+1, h) 
  
 
arr = [100, 76, 80, 9, 111, 50] 
n = len(arr)-1 
quickSort(arr,0,n) 
print ("Elements of array after applying sorting:") 
for i in range(n): 
    print ("%d" %arr[i]), 

