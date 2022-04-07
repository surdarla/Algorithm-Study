def countingSort(arr):
    result_array = [0]*100 # [0 for i in range(len(arr))] << not working
    for i in arr:
        result_array[i] += 1
        
    return result_array

# 해당 숫자에 해당하는 index 를 1씩 더해주면 됨.
# [0 for i in range(len(arr))] << arr 크기만큼 [0] 을 만들어주면 안됨. [0 3 5] 이런 방식으로 숫자를 건너띄고 input 을 받는 경우가 있음. 
