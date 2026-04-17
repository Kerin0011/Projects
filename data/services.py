import json
# Save the task list to a JSON file
def save_data(task):
    with open("task.json", "w") as file:
        json.dump(task, file)

# Load tasks from the JSON file or return an empty list if not found
def load_data():
    try:
        with open("task.json", "r") as file:
            return json.load(file)
    except:
        return []
    