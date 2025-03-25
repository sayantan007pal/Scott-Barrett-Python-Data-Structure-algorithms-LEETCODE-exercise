def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)

#So as this function runs 2 times independently so timecomplexity is O(n+n) == O(2n) = O(n)
#Thus we are dropping constants