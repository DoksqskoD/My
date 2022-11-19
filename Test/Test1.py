import numpy as np

new_arr = np.array([16, 20, 12, 10, 8, 22, 97, 75, 43])
print("Creation of array:",new_arr)
final_output = np.fromiter((i for i in new_arr if i < 25), dtype = new_arr.dtype)

print("Filtering array:",final_output)