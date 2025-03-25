def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)
#So now we can not write timecomplexity is O(n+n) == O(2n) = O(n) as two different variables are present
# Now the time complexity is O(a+b)


#Similarly for nested for loops the timecomplexity becomes O(n*n)