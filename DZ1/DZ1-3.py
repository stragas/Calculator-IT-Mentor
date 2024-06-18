# Task 1
def is_positive(A):
    return A > 0

# Task 2
def is_not_even(A):
    return A % 2 != 0

# Task 3
def is_even(A):
    return A % 2 == 0

# Task 4
def inequality1(A, B):
    return A > 2 and B <= 3

# Task 5
def inequality2(A, B):
    return A >= 0 or B < -2

# Task 6
def inequality3(A, B, C):
    return A < B < C

# Task 7
def inequality4(A, B, C):
    return A < B < C or A > B > C

# Task 8
def even1(A, B):
    return A % 2 != 0 and B % 2 != 0

# Task 9
def even2(A, B):
    return A % 2 != 0 or B % 2 != 0


# Task 10
def even3(A, B):
    return (A % 2 != 0 and B % 2 == 0) or (A % 2 == 0 and B % 2 != 0)


A = 5
B = 8
C = 10
print("Task 1:", is_positive(A))
print("Task 2:", is_not_even(A))
print("Task 3:", is_even(A))
print("Task 4:", inequality1(A, B))
print("Task 5:", inequality2(A, B))
print("Task 6:", inequality3(A, B, C))
print("Task 7:", inequality4(A, B, C))
print("Task 8:", even1(A, B))
print("Task 9:", even2(A, B))
print("Task 10:", even3(A, B))