def countingSort(arr):
    result_array = [0 for i in range(len(arr))] # [0]*100 possible
    for i in arr:
        result_array[i] += 1
        
    return result_array

# 해당 숫자에 해당하는 index 를 1씩 더해주면 됨.
# arr 크기 제한이 100으로 걸려 있으므로 result_array를 [0]*100 해줘도 무관.
