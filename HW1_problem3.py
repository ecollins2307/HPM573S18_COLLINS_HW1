#HW 1, Problem 3

#iterative function
def iterative(n):
    count = 0
    for x in range(1,n+1):
        count = count + x
    return count

print(iterative(100))

#recursive function
def recursive(n):
    if n == 0:
        return 0
    else:
        return (n + recursive(n-1))

print(recursive(100))


