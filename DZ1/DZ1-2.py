# 1
def meters_from_centimeters(L):
    return L // 100

# 2
def tonnes_from_kilograms(M):
    return M // 1000

# 3
def kilobytes_from_bytes(file_size):
    return file_size // 1024

# 4
def segments(A, B):
    return A // B

# 5
def segments_length(A, B):
    return A % B

# 6
def extract_digits(num):
    tens = num // 10
    ones = num % 10
    return tens, ones

# 7
def sum_and_product(num):
    tens, ones = extract_digits(num)
    return tens + ones, tens * ones

# 8
def swap_digits(num):
    tens, ones = extract_digits(num)
    return ones * 10 + tens

# 9
def extract_hundreds(num):
    return num // 100

# 10
def extract_last_and_middle(num):
    last_digit = num % 10
    middle_digit = (num // 10) % 10
    return last_digit, middle_digit

# Test the functions
L = 356
M = 2345
file_size = 4096
A = 100
B = 7
num1 = 76
num2 = 546

print(meters_from_centimeters(L))
print(tonnes_from_kilograms(M))
print(kilobytes_from_bytes(file_size))
print(segments(A, B))
print(segments_length(A, B))
print(extract_digits(num1))
print(sum_and_product(num1))
print(swap_digits(num1))
print(extract_hundreds(num2))
print(extract_last_and_middle(num2))