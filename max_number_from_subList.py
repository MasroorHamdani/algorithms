def main():
    # Array passed
    arr = [2,5,4,6,8,5]
    # Length of Sub String
    x = 3
    i = 0
    min_value = []
    # Loop through the array passed.
    # Get the Sub List with given length and
    # get the min value from sub list and push in array min_value.
    while i < len(arr):
        if len(arr[i:x+i]) == x:
            print(arr[i:x+i])
            min_value.append((min(arr[i:x+i])))
        i+=1

    # Array with all the min values from sub lists.
    # Get the Max out of the List
    print(max(min_value))


if __name__ == "__main__":
    main()