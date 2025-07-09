def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print("The result of the division is ", end='')
        return result
    except ZeroDivisionError:
       return  "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
        
