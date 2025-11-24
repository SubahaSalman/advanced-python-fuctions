numbers = [3999,1349,121,4893,234,1,56,23,6,3,8]
print("These are the original numbers: ", numbers)
bigNumbers = [x for x in numbers if x>230]

print("These are the selected numebrs out of the original list, valued above 230: ", bigNumbers)