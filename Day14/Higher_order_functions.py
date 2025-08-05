'''def sum_numbers(nums): # normal function
    return sum(nums) # a sad function abusing the built-in
def higher_order_function(f, lst): # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)'''

def get_voyelles_numbers(n):
    voyelles = ["a", "i", "o", "u", "e", "y"]
    if len(n) is 