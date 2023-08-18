def two_positive(a, b, c):
    count = 0
    
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
        
    return count == 2

# Test cases
print(two_positive(2, 4, -3))
print(two_positive(3,9,4))