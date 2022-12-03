from InquirerPy import prompt

# Basic usage - Example from InquirerPy
questions = [
    {"type": "input", "message": "What's your name:", "name": "name"},
    {
        "type": "list",
        "message": "What's your favourite programming language:",
        "choices": ["Go", "Python", "Rust", "JavaScript"],
    },
    {"type": "confirm", "message": "Confirm?"},
]
result = prompt(questions)
name = result["name"]
fav_lang = result[1]
confirm = result[2]
print(result)