def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]

    print("Lista przed sortowaniem:", my_list)

    bubble_sort(my_list)

    print("Lista po sortowaniu:", my_list)
