import json
from difflib import get_close_matches

def load_data(file_path:str):
    data = json.load(open(file_path, 'r'))
    return data

def save_data(data:dict, file_path:str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_best_match(user_input:str, questions:list[str]) -> str | None :
    matches = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

def get_answer(question:str, data:dict) -> str | None:
    for i in data:
        if question.lower() == i["question"].lower():
            return i["answer"]
        
def main():
    data = load_data("data.json")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit" or user_input.lower() == "quit":
            break

        best_match = find_best_match(user_input, [i["question"] for i in data["questions"]])

        if best_match:
            print(f"Bot: {get_answer(best_match, data['questions'])}")
        else:
            print("Bot: Sorry, I don't understand that. Please teach me.")
            new_answer = input("Tye the answer or 'skip' to skip: ")

            if new_answer.lower() != "skip":
                data["questions"].append({"question": user_input, "answer": new_answer})
                save_data(data, "data.json")
                print("Bot: Thanks for teaching me.")

if __name__ == "__main__":
    main()