def personal_details():
# Prompt user for their first name
    while True:
        first_name = input("Enter your first name: ").capitalize()
        if first_name.isalpha():
            all_details.append(f"First name     : {first_name}")
            break
        else:
            print("**Please enter only letters")

# Prompt user for their last name
    while True:
        last_name = input("Enter your last name: ").capitalize()
        if last_name.isalpha():
            all_details.append(f"Last name      : {last_name}")
            break       
        else:
            print("**Please enter only letters")

# Prompt user for their date of birth
    while True:
        date_of_birth = input("Enter your date of birth as DDMMYYYY: ")
        if date_of_birth.isdigit() and len(date_of_birth) == 8:
            all_details.append(f"DOB            : {date_of_birth}")
            break
        else:
            print("**Please enter your DOB with no spaces or dashes")

def contact_details():
# Prompt user for their email address
    while True:
        email = input("Enter your e-mail: ")
        if "@" in email and  "." in email:
            all_details.append(f"E-mail         : {email}")
            break                
        else:
            print("**Please use this format: abc1@def.gh")

# Prompt user for their mobile number
    while True:    
        mobile_number = input("Enter your mobile number: ")
        if len(mobile_number) != 11 or not mobile_number.isdigit():
            print("**Please enter your 11-digit mobile number")
        else:
            all_details.append(f"Mobile number  : {mobile_number}")
            break                

def login_details():
# Prompt user for their username
    while True: 
        username = input("Enter your username: ")
        for i in username:
            for y in special_char:
                if i == y:
                    print("**Please enter only letters and digits")
                    break
        if len(username) < 4:
            print("**Your username should be at least 4 characters long")
        else:    
            all_details.append(f"Username       : {username}")
            break     

# Prompt user for their password
    while True:
        password = input("Enter your password: ")
        if len(password) < 8 or len(password) > 12:
            print("**Your password should contain min 8 charcters and max 12")
        else:
            all_details.append(f"Password       : {password}")
            break               

# Prompt user to re-enter their password for confirmation  
    while True:
        repeat_password = input("Re-enter your password: ")
        if password != repeat_password:
            print("**Your passwords do not match. Try Again")
        else:
            break

def bank_details():
# Prompt user for their title
    while True:
        title = input("Your Title \n1. Mr\n2. Mrs\n3. Miss\nEnter a number (1-3): ")
        if title == "1":
            title = "Mr"
            break
        elif title == "2":
            title = "Mrs"
            break
        elif title == "3":
            title = "Miss"
            break
        else:
            print("**Please select an option between 1 and 3")

# Prompt user for their first name            
    while True:
        first_name = input("Enter your first name: ").capitalize()
        if not first_name.isalpha():
            print("**Please enter only letters")
        else: 
            break

# Prompt user for their last name   
    while True:
        last_name = input("Enter your last name: ").capitalize()  
        if not last_name.isalpha():
            print("**Please enter only letters")
        else:
            all_details.append(f"Account holder : {title} {first_name} {last_name}")
            break

# Prompt user for their account number
    while True:
        account_number = input("Enter your account number: ")
        if not account_number.isdigit or len(account_number) != 8:
            print("**Please enter your 8-digit account number")
        else:
            all_details.append(f"Account number : {account_number}")
            break

# Prompt user for their sort code        
    while True:
        sort_code = input(f"Enter your sort code: ")
        if not sort_code.isdigit() or len(sort_code) != 6:
            print("**Please enter your 6-digit sort code with no spaces or dashes")
        else:
            all_details.append(f"Sort code      : {sort_code}")
            break                

# Initialize global variables to store details
all_details = []

# List of special characters to validate against
special_char = ["!", "£", "$", "%", "^", "&", "*", ")", "(", "_", "-", "+", "=", "]", "{", "}", "[", "@", "'", "~",";",":", "/", "?", ">", "<", ",", "|", "\\", "", "#", "."]

# Begin the application form process
print("-"*40)
print("Gym Membership Application Form")
print("-"*40)

# Collect personal details
print("\033[1m1) Personal Details\033[0m")
personal_details()

# Collect contact details
print("\n\033[1m2) Contact Details\033[0m")
contact_details()

# Collect login details
print("\n\033[1m4) Account Details\033[0m")
login_details()

# Collect bank details
print("\n\033[1m4) Bank Details\033[0m")
bank_details()

# Display the collected details for confirmation    
print("\n\033[1m5) Check your details\033[0m")
print(*all_details,sep='\n')
confirmation = input("Are all details correct? Enter (y/n): ").lower()
if confirmation == "y": # Display Success message
    print("Congrats! You can now access all gym facilities, classes and swimming pool for £25 a month!")
elif confirmation == "n": # Display Failure message
    print("Application did not go through.")
else: # Display Error message for unexpected input
    print("Oops! Something went wrong. Don't worry, you can always come back and try again later.")