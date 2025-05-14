"""
Conditions:
  1. Not more than 12 digits.
  2. No spaces.
  3. No digits.
"""

username = input("Please enter your username: ")
 
if len(username) > 12:
  print("Username should not be more than 12 characters.")
elif not username.find(" ") == -1:
  print("Username should not have spaces.")
elif username.isalpha() == False:
  print("Username should not have digits.")
else:
  print("Username is valid.")
