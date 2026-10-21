# CS 1101 Unit 7 Assignment: University Workshop Feedback Manager

# Question 1: String Cleaning and Standardization
print("=== QUESTION 1 ===")
raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
print("Original Raw Feedback:", raw_feedback)

step1_text = raw_feedback.strip().lower()
step2_text = step1_text.replace("speaker", "presenter")
cleaned_spacing = " ".join(step2_text.split())
final_cleaned_feedback = cleaned_spacing.title()
print(f"Final Cleaned Feedback: {final_cleaned_feedback}\n")


# Question 2: File Input, Output, and Appending
print("=== QUESTION 2 ===")
feedback_list = [
    "The Presenter Was Great But The Room Was Cold",
    "Interactive Sessions Were Very Helpful And Engaging",
    "Great Workshop Overall With Practical Examples"
]

with open("feedback.txt", "w") as file:
    for item in feedback_list:
        file.write(item + "\n")

print("--- Reading feedback.txt (Initial Entries) ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

new_feedback = "The Venue Was Easy To Find And Well Organized\n"
with open("feedback.txt", "a") as file:
    file.write(new_feedback)

print("\n--- Reading feedback.txt (After Appending) ---")
with open("feedback.txt", "r") as file:
    print(file.read().strip())
print("\n")


# Question 3: Exception Handling
print("=== QUESTION 3 ===")
try:
    print("Attempting to Open and Read Feedback File Safely...")
    with open("feedback.txt", "r") as file:
        content = file.read()
        print("File contents loaded successfully.")
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed.")
print("\n")


# Question 4: String Analysis and Summary Report Generation
print("=== QUESTION 4 ===")
great_count = 0
total_feedback = 0

try:
    with open("feedback.txt", "r") as file:
        lines = file.readlines()
        total_feedback = len(lines)
        for line in lines:
            if "great" in line.lower():
                great_count += 1
except FileNotFoundError:
    total_feedback = 0
    great_count = 0

summary_content = (
    "=== Workshop Feedback Summary ===\n"
    f"Total Feedback: {total_feedback}\n"
    f"Mentions of 'Great': {great_count}\n"
)

with open("summary.txt", "w") as summary_file:
    summary_file.write(summary_content)

print("--- Generated Workshop Feedback Summary Report ---")
print(summary_content.strip())