# Linear Search using python
pos = -1
n = int(input("Please enter a number "))


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:  # [i] refers to the index number of list
            globals()['pos'] = i  # Gives us the index number where it is located. Global is for global variable pos
            return True
        i += 1
    return False


list = [1, 3, 4, 6, 7, 8, 9, 11]

if search(list, n):
    print("Found at", pos + 1)  # Since human count from 1, but program count from 0, we are adding 1
else:
    print("Not Found")
