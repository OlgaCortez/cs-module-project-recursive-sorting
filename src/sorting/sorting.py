# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB): # Takes 2 array as arguments 
    elements = len(arrA) + len(arrB) # Elements is the lenght of both arrA and arrB combined

    # NOT SURE WHAT IS GOING ON HERE
    # New array created (merged_arr):
    # multiplies 0 by the number of elements 
    merged_arr = [0] * elements 

    # Your code here
    arrA_idx = 0 # Setting variables
    arrB_idx = 0 # Setting variables
    idx = 0 # Setting variables

    while arrA_idx < len(arrA) and arrB_idx < len(arrB): # If both arrA and arrB are empty
        if arrA[arrA_idx] < arrB[arrB_idx]: # If 0 index of arrA is less than 0 index of arrB
            merged_arr[idx] = arrA[arrA_idx] # The ArrA indx becomes new idx of merged_arr idx 
            idx += 1
            arrA_idx += 1
        else:
            merged_arr[idx] = arrB[arrB_idx]
            idx += 1
            arrB_idx += 1
    while arrA_idx < len(arrA):
        merged_arr[idx] = arrA[arrA_idx]
        idx += 1
        arrA_idx += 1
    while arrB_idx < len(arrB):
        merged_arr[idx] = arrB[arrB_idx]
        idx += 1
        arrB_idx += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr): # Takes an array as an argument
    start = 0 # 1st index in the array
    end = len(arr) # ending at the index after the final item in the array

    # NOT SURE WHAT THIS LINE IS DOING 
    # Base Case: If only one item is left in the array... break and go to line 48?
    if end > start + 1: 

        # Divide's array to get the middle index. 
        # Will continue to do this over and over until it is finished on left side 
        mid = start + end // 2 

        # This will break down continue to get the middle index and make
        # Smaller arrays within arrA handleing the left sides 1st until 
        # it can move on to the and handle the right sides
        arrA = merge_sort(arr[0:mid]) 

        # This will break down continue to get the middle index and make
        # Smaller arrays within arrB handleing the right side until we call on line 50
        arrB = merge_sort(arr[mid:end]) 

        # After it runs lines 46 and 50 we want to merge arrA and arrB
        arr = merge(arrA, arrB)


    return arr # Will return value of the last item in the array

# example for line 41, 46, 50:
# arr = 5, 1, 4, 6, 9, 7
#       0  1  2 mid 4  5  6 <-- index #
#     start     mid       end
#  line 41 --> mid is # 6
# line 46 --> Working in a new array arrA 5, 1, 4 (range [0:mid]), recursion happens now and it will start at beginning
# line 41 --> 1 is mid now 
# line 46 --> 5 range(range [0:mid])... reursion since function called itself and start ath beginning
# Line 37 -->  since only one value left it will add 1 and go to line 54
# line 54 --> return value of only item 
# Line 50 --> working is arrB Now we need to take care of # 4 (range[mid:end])
# Due to recursion this will run and start at the beginning and since it is only one item
# left it will add 1 to arrB and return the value for last item 
# After this is done on just 5 - 4 it will call on line 51 which will now merge 
# arrA and arrB using the function merge on line 2





# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

