# daily_reminder.py
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Use match case to respond differently based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Check if the task is time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
if time_bound == "no":
    message += " Consider completing it when you have free time"

print(message)
