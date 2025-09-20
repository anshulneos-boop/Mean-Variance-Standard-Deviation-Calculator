import mean_var_std

# Test 1
test_lst = [0,1,2,3,4,5,6,7,8]
print("Result of test list one")
print(mean_var_std.calculate(test_lst))
print("--------------------------------------------------------------")

# Test 2
test_lst = [2,6,2,8,4,0,1,5,7]
print("Result of test list two")
print(mean_var_std.calculate(test_lst))
print("--------------------------------------------------------------")

# Test 3
test_lst = [9,1,5,3,3,3,2,9,0]
print("Result of test list three")
print(mean_var_std.calculate(test_lst))
print("--------------------------------------------------------------")

# Test 4 (invalid length - will raise ValueError)
test_lst = [2,6,2,8,4,0,1]
print("Result of test list four")
try:
    print(mean_var_std.calculate(test_lst))
except ValueError as e:
    print(e)  # prints "List must contain nine numbers."
