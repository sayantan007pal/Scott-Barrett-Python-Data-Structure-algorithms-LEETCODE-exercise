num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) 

num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# In Python, integers are immutable, meaning their value cannot be changed after creation.
# When you assign num2 = num1, both variables point to the
# same memory location (object) holding the value 11. However, when you update num2 to 22,
# Python creates a new integer object for 22 and updates num2 to point to it, 
# leaving num1 unchanged. This is why their memory addresses (id()) differ after the update.
#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# In Python, variables like dict1 and dict2 store references to objects, 
# not the objects themselves. When you assign dict2 = dict1, 
# both variables point to the same dictionary in memory (same id).

# When you update dict2['value'], the change affects the shared dictionary, 
# so both dict1 and dict2 reflect the update. This demonstrates that Python uses 
# references for mutable objects like dictionaries.



##Explain what will happen when reference to an object is removed?

# In Python, when a reference to an object is removed
# (e.g., by reassigning a variable or deleting it), the object itself is not
# immediately destroyed. Instead, Python uses garbage collection to manage memory. 
# Here's what happens step by step:

# Reference Count: Each object in Python has a reference count, 
# which tracks how many variables or data structures are pointing to it.

# Reference Removal: When a reference to an object is removed 
# (e.g., dict2 = None or reassigned to another object), the reference count of 
# the original object decreases.

# Garbage Collection: If the reference count of an object drops to zero 
# (i.e., no variables or structures are pointing to it), the object becomes 
# eligible for garbage collection. Python's garbage collector will eventually
# reclaim the memory used by the object.

# In your code, dict1 and dict2 both point to the same dictionary object. 
# If you remove one reference (e.g., dict2 = None), the dictionary object will 
# still exist because dict1 is still pointing to it. The object will only be garbage 
# collected if all references to it are removed.



