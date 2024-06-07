def func(stack, elements):
    for i in range(len(elements)):
        if elements[i] in stack:
          stack.remove(elements[i])
        if elements[i] == "":  
            elements[i] = stack.pop()

# Example usage
stack = ["a", "b", "c", "d", "e", "f"]
elements = ["", "e", "d", "", "", ""]
func(stack, elements)
print("Updated elements:", elements)
print("Updated stack:", stack)