print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

TRUE_count_score = lower_case_name1.count("t") + lower_case_name1.count("r") + lower_case_name1.count("u") + lower_case_name1.count("e") + lower_case_name2.count("t") + lower_case_name2.count("r") + lower_case_name2.count("u") + lower_case_name2.count("e")

LOVE_count_score = lower_case_name1.count("l") + lower_case_name1.count("o") + lower_case_name1.count("v") + lower_case_name1.count("e") + lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") + lower_case_name2.count("e")

string_combined_score = str(TRUE_count_score) + str(LOVE_count_score)
int_combined_score = int(string_combined_score)

if int_combined_score < 10 or int_combined_score > 90:
  print(f"Your score is {int_combined_score}, you go together like coke and mentos.")
elif int_combined_score > 40 and int_combined_score < 50:
  print(f"Your score is {int_combined_score}, you are alright together.")
else:
  print(f"Your score is {int_combined_score}.")