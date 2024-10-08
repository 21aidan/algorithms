def unique(array):                              #O(nlogn) time
    mergeSort(array, 0, len(array) - 1)         #O(n) space
    return compare(array)


def mergeSort(array, l, r):
    # if the left index is smaller than the right index then the array has more than one element and can split
    if l < r:
        m = l + (r - l) // 2    # find the middle point
        # recursively sort the left and right halves
        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        # merge these sorted halves
        merge(array, l, m, r)


# input the array, the left side starting index, middle index and right side ending index
def merge(arr, l, m, r):
    # calculate the size of the two subarrays
    n1 = m - l + 1
    n2 = r - m

    # create temporary arrays to hold the values of the two subarrays
    L = [0] * (n1)
    R = [0] * (n2)

    # copy data from the original arrays into the temp arrrays L[] and R[]
    for i in range (0, n1):
        L[i] = arr[l + i]   # copies arr[l...m]

    for j in range (0, n2):
        R[j] = arr[m + 1 + j]   # copies arr[m+1...3]

    # merge these two sorted subarrays (L[] and R[]) back into the original array (arr[])
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        # compare the elements of L[] and R[]
        # copy the smaller element into arr[] and move the respective i or j value
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1   # k keeps track of where to place the smaller element in arr[]

    # copy any remaining elements of L[] or R[] if there are any (so if there's e.g 10 numbers in L[] higher than that in R[], it goes through and places them at the end)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

def compare(array):
    for i in range(len(array)-1):
        if array[i] == array[i + 1]:
            return False
    return True

s = '?_+?'
array = list(s)
print(array)
print(unique(array))