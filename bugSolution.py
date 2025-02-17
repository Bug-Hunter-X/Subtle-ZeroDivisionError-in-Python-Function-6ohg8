def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return a / b
    except ZeroDivisionError:
        return float('inf') #Or handle the error as per requirements

result = function_with_uncommon_error(10, 0) 