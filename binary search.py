# Binary search
#The number in the list need to be in order

def search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [4, 7, 8, 12, 15,45, 89, 100, 120,121,122,123,124,126,129]
n =15


if search(list, n):
    print("Found at", pos + 1)  # Since human count from 1, but program count from 0, we are adding 1
else:
    print("Not Found")
