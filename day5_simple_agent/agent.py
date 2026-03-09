# agent.py

import re
from tools import calculator

def is_math_question(query: str):
    math_keywords = ["+", "-", "*", "/", "multiply", "add", "subtract", "divide"]
    return any(keyword in query.lower() for keyword in math_keywords)

def extract_expression(query: str):
    match = re.search(r"(\d+\s*[\+\-\*/]\s*\d+)", query)
    if match:
        return match.group(1)
    return None

def agent_response(query: str):
    if is_math_question(query):
        expression = extract_expression(query)
        if expression:
            result = calculator(expression)
            return f"Tool used: calculator\nAnswer: {result}"
        else:
            return "Tool used: none\nAnswer: I could not detect the math expression."
    else:
        return "Tool used: none\nAnswer: This is a normal question. AI agents are systems that can reason and use tools."

if __name__ == "__main__":
    user_query = input("Enter your question: ")
    response = agent_response(user_query)
    print(response)
