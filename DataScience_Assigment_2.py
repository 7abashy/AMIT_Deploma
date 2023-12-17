#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
print("                                         Ex1")
print("")
def none_of_elements_is_zero(arr):
    return np.all(arr != 0)
arr_1 = np.array([1, 2, 3, 4])
print(none_of_elements_is_zero(arr_1))  # True
arr_2 = np.array([1, 2, 0, 4])
print(none_of_elements_is_zero(arr_2))  # False


# In[4]:


print("                                         Ex2")
print("")



def none_of_elements_is_zero(arr):
    return np.any(arr != 0)


arr_1 = np.array([1, 2, 3, 4])
print(none_of_elements_is_zero(arr_1))  # True
arr_2 = np.array([0, 0, 0, 0])
print(none_of_elements_is_zero(arr_2))  # False
print("#" * 100)


# In[5]:


print("                                         Ex3")
print("")
arr11 = np.array([1.1, 2.2, 3.3])
arr12 = np.array([1.05, 2.2, 3.35])

# Element-wise comparison (equal)
equal_comparison = np.equal(arr11, arr12)
print(equal_comparison)

# Element-wise comparison (equal within a tolerance)
tolerance = 0.05
tolerance_comparison = np.isclose(arr11, arr12, atol=tolerance)
print(tolerance_comparison)
print("#" * 100)


# In[6]:


print("                                         Ex4")
print("")
zeros_array = np.full(shape=10, fill_value=0)
ones_array = np.full(shape=10, fill_value=1)
fives_array = np.full(10, 5)
print(f"Zeros = {zeros_array}")
print(f"Ones  = {ones_array}")
print(f"Fives = {fives_array}")
conc = np.concatenate((zeros_array, ones_array, fives_array))
print(f"Concatenation = {conc}")
print("#" * 100)


# In[7]:


print("                                         Ex5")
print("")
random_array_15 = np.arange(30, 70)
print(random_array_15)
print("#" * 100)


# In[8]:


print("                                         Ex6")
print("")
ex_6 = np.eye(3)
print(ex_6)
print("#" * 100)


# In[9]:


print("                                         Ex7")
print("")
ex_7 = np.random.rand()
print(ex_7)
print("#" * 100)


# In[10]:


print("                                         Ex8")
print("")
ex_8 = np.random.rand(15)
print(ex_8)
print("#" * 100)


# In[11]:


print("                                         Ex9")
print("")
vector_ex9 = np.arange(15, 56)
print(vector_ex9[1:-1])
print("#" * 100)


# In[12]:


print("                                         Ex10")
print("")
vector_ex10 = np.random.randint(0, 11, size=5)
print(vector_ex10)
print("#" * 100)


# In[13]:


print("                                         Ex11")
print("")
matrix_ex11 = np.zeros((10, 10))
matrix_ex11[0] = 1
matrix_ex11[-1] = 1
matrix_ex11[:, 0] = 1
matrix_ex11[:, -1] = 1
print(matrix_ex11)
print("#" * 100)


# In[14]:


print("                                         Ex12")
print("")
matrix_ex12 = np.zeros((5, 5))
np.fill_diagonal(matrix_ex12, [1, 2, 3, 4, 5])
print(matrix_ex12)
print("#" * 100)


# In[15]:


print("                                         Ex13")
print("")
matrix_13 = np.zeros((4, 4), dtype=int)
matrix_13[1::2, ::2] = 1
matrix_13[::2, 1::2] = 1
print(matrix_13)
print("#" * 100)


# In[16]:


print("                                         Ex14")
print("")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
# Save the arrays
np.savez_compressed('arrays.npz', arr1=arr1, arr2=arr2)
# Load the arrays
data = np.load('arrays.npz')
arr1_loaded = data['arr1']
arr2_loaded = data['arr2']
print(arr1_loaded)
print(arr2_loaded)
print("#" * 100)


# In[17]:


print("                                         Ex15")
print("")
random_array_15 = np.random.rand(40)
print(random_array_15)
print("#" * 100)


# In[18]:


print("                                         Ex16")
print("")


def extract_numbers(arr, lower_bound, upper_bound):
    return arr[(arr > lower_bound) & (arr < upper_bound)]

# Example usage
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lower_bound = 3
upper_bound = 8
result = extract_numbers(arr, lower_bound, upper_bound)
print(result)
print("#" * 100)

