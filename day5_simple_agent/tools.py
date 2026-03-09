# tools.py

def calculator(expression: str):
    """
    Simple calculator tool for math expressions
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
