import csv, json

compromised_users = []

# Open the passwords.csv file and parse it using csv.DictReader
try:
    with open("passwords.csv") as password_file:
      password_csv = csv.DictReader(password_file)

      for row in password_csv:
        password_row = row
        compromised_users.append(password_row['Username'])
except FileNotFoundError:
    print("The file passwords.csv does not exist.")

with open("compromised_users.txt", "w") as compromised_user_file:
  # Iterate over compromised_users, list we created
  for compromised_user in compromised_users:
    compromised_user_file.write("\n" + compromised_user)

with open("compromised_users.txt", "r") as compromised_user_text_file:
  for line in compromised_user_text_file.readlines():
    print(line)

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient":"The Boss",
    "message":"Mission Success"
  }

  json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
