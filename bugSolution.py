def my_function(x):
    if x == 0:
        return 0
    else:
        if x > 1000:  # Add a check for large inputs 
            raise ValueError("Input too large for recursive approach")
        else:
            return my_function(x - 1) + x


print(my_function(5))

#Alternative iterative solution
def my_function_iterative(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

print(my_function_iterative(5000))