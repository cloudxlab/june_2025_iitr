def binary_search(lst, e): #bisect, bisection
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right)//2
        if lst[mid] == e:
            return mid
        elif lst[mid] > e:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    print("--- Inside the main file: binary_search --- ")
    lst = [1,2,34]
    idx = binary_search(lst, 56)
    print("Result: ", idx)
