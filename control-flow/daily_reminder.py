# Task Reminder App

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
print()
match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Remider: '{task}' is a {priority} priority task that requires immediate attention today!"
            )
        else:
            print(
                f"Remider: '{task}' is a {priority} priority task. Consider completing it when you have free time."
            )

    case "medium":
        if time_bound == "yes":
            print(
                f"Remider: '{task}' is a {priority} priority task that requires immediate attention today!"
            )
        else:
            print(
                f"Remider: '{task}' is a {priority} priority task. Consider completing it when you have free time."
            )

    case "low":
        if time_bound == "yes":
            print(
                f"Remider: '{task}' is a {priority} priority task that requires immediate attention today!"
            )
        else:
            print(
                f"Remider: '{task}' is a {priority} priority task. Consider completing it when you have free time."
            )