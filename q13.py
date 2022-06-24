# 	The code snippet below looks for the first two elements that are out of order and swaps them; however, 
#   it is not producing the correct results. 
#   Rewrite the code so that it works correctly.


arr = [5, 22, 29, 39, 19, 51, 78, 97, 84]
i = 0
while (i < len(arr) -1):
    # and (arr[i] <= arr [i+1]
    if (arr[i] >= arr[i+1]):
        print(i)
        saved = arr[i+1]
        arr[i+1] = arr[i]  
        arr[i] = saved
        print(arr)

    i += 1