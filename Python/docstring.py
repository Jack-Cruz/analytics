def add_binary(x, y):
    """
    Return the sum of two decimal numbers in binary digits.
    
        Parameters:
            x (int): A decimal integer
            y (int): Another decimal integer
        
        Returns:
            binary_sum (str): Binary string of the sum of y and y
    """
    
    binary_sum = bin(x+y)[2:]
    return binary_sum

print(add_binary.__doc__)