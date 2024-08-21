# Dictionary that maps 0->a, 1->b, ...,
from mappings import int_to_char_a0 as i2c

def knapsack(arr, target, path=[]):
    # If target is 0, we've found a solution
    if target == 0:
        return [path]

    # If target is negative or arr is empty, there's no solution
    if target < 0 or not arr:
        return []

    # Try including arr[0] in the solution and solve for the remaining target and items
    with_first = knapsack(arr[1:], target - arr[0], path + [arr[0]])

    # Try excluding arr[0] from the solution and solve for the remaining target and items
    without_first = knapsack(arr[1:], target, path)

    return with_first + without_first

#  Function to check if an array is super increasing
def isSuperIncreasing(arr):
    for i in range(0, len(arr)):
        # Return false if not super increasing and report the sum
        if arr[i] <= sum(arr[:i]):
            string = " + ".join([str(x) for x in arr[:i]])
            print(f"{arr[i]} <= {string} = {sum(arr[:i])}")
            return False
    return True

# The SIC array
arr = [1,2,3,5,8]

# Check if the array is super increasing
if not isSuperIncreasing(arr):
    print("Array is not super increasing")
#     exit()
    
# Reverse to adhere to the convention of the knapsack function
arr = arr[::-1]
print(f"With knapsack: {arr}")

# Numbers to find solutions for
targets = [i for i in range(0, 32)]
letters_in_chunk = int(input("Enter the letters in the chunk: "))

# Perform knapsack for each target
for target in targets:
    # print(f"All possible solutions for target {target}:")
    res = knapsack(arr, target)
    if len(res) >= 2:
        print(f"Target: {target}")
        for elem in res:
            print(f"{elem}")
        exit()
            
                
        
print()