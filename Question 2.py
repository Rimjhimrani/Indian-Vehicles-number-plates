#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def is_valid_number_plate(number_plate):
    # Define the pattern based on "XX NN YY NNNN" format
    pattern = r"^[A-Z]{2}\s\d{2}\s[A-Z]{2}\s\d{4}$"
    
    # Check if the number plate matches the pattern
    if re.match(pattern, number_plate):
        return True
    else:
        return False

# Test cases
if __name__ == "__main__":
    number_plate = input("Enter the vehicle number plate: ").strip()

    if is_valid_number_plate(number_plate):
        print(f"{number_plate} is a valid vehicle number plate.")
    else:
        print(f"{number_plate} is not a valid vehicle number plate.")


# In[ ]:




