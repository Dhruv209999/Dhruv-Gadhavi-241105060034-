arr = [10, 20, 30, 40, 50]
n = 5
key = 30
low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print(f"Found at {mid}")
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Not Found")