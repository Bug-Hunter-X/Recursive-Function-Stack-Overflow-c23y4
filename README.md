This repository contains a Python function that demonstrates a common programming error: a stack overflow caused by unbounded recursion. The `my_function` is designed to calculate the sum of numbers from 1 to x recursively. However, it lacks a base case to handle very large inputs, leading to exceeding the recursion depth limit and causing a stack overflow. The solution demonstrates how to address this issue by implementing proper base case handling.