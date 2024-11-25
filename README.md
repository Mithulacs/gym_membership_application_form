# Gym Membership Application Form

## Overview

This project implements a command-line application for collecting user details in order to register for a gym membership. It gathers personal contact, login, and bank details from the user.

## Table of Contents

1. Features
2. Requirements
3. Installation Instructions
4. Usage
5. Code Structure
6. Function Documentation

***

## Features

* Collects personal information (first name, last name, date of birth).
* Gathers contact details (email, mobile number).
* Registers login details (username, password).
* Captures bank information (account holder name, account number, sort code).

## Requirements

* Python 3.x

## Installation Instructions

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository or copy the code into a Python environment.
3. Run the script in your terminal or command prompt.

## Usage

1. Execute the script.
2. Follow the prompts to enter your details.
3. At the end of the inputs, confirm your details to complete the application process.

## Code Structure

The code is divided into several functions, each dedicated to collecting specific sets of information. The primary functions are:

* `personal_details()`: Gathers personal information.
* `contact_details()`: Collects contact details.
* `login_details()`: Registers the user's login credentials.
* `bank_details()`: Captures bank-related information.

The collected details are stored in a global list named `all_details`.

## Function Documentation

### `personal_details()`

Collects the user's personal information.

#### Details:

* Prompts for the first name, last name, and date of birth.
* Ensures the first and last names consist only of alphabetic characters.
* Validates the date of birth format as DDMMYYYY, ensuring it's an 8-digit number.

***

### `contact_details()`

Gathers the user's contact information.

#### Details:

* Prompts for an email address and mobile number.
* Validates the email format for the presence of "@" and ".".
* Ensures the mobile number is exactly 11 digits.

***

### `login_details()`

Captures the user's login credentials.

#### Details:

* Prompts for a username and password.
* Validates the username for minimum length and checks for special characters.
* The password must be between 8 and 12 characters.
* Confirms the password by prompting the user to re-enter it for verification.

***

### `bank_details()`

Collects banking information from the user.

#### Details:

* Prompts for a title, first name, last name, account number, and sort code.
* Validates the title selection as a numeric input (1-3).
* Ensures account numbers are 8 digits and sort codes are 6 digits.

***

### Global Variables

* `all_details`: A list that stores all collected user information.
* `special_char`: A list of special characters used to validate email and username inputs.

***

## Example Interaction

```plaintext
Enter your first name: Sam
Enter your last name: Rossi
Enter your date of birth as DDMMYYYY: 01011990
...
Are all details correct? Enter (y/n): y
Congrats! You can now access all the gym facilities, classes and swimming pool for £25 a month!


---
```
