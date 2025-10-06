# 💻 Net Banking Application (Python)

## 📋 Overview
The **Net Banking App** is a simple command-line Python application that simulates basic online banking operations.  
Users can register, log in, deposit money, withdraw funds, check balances, and view transaction histories — all stored locally as text files.  
This project demonstrates **file handling**, **object-oriented programming (OOP)**, **data validation**, and **user authentication** in Python.

---

## 🚀 Features
✅ **User Registration & Login System**  
- Secure user credentials stored locally (`customer_details` file).  
- Password validation (minimum 8 characters, at least one uppercase letter and one digit).  

✅ **Banking Operations**  
- Deposit funds  
- Withdraw funds  
- View account balance  
- View transaction history  

✅ **Transaction Logging**  
- Each user has a dedicated transaction file (`<username>_transaction`).  
- Every transaction includes a timestamp, description, and updated balance.  

✅ **Error Handling & Validation**  
- Handles invalid inputs gracefully.  
- Ensures file existence and data integrity on each session.

---

## 🧩 Project Structure
Net_banking app.py # Main Python application
├── customer_details # Stores registered user credentials
├── <username>_transaction # Automatically generated transaction files
└── README.md # Project documentation


---

## 🧠 Key Concepts Used
- **Classes & Objects (OOP)**
- **File Handling** (read, write, append)
- **Data Persistence** using text files
- **Input Validation**
- **Error & Exception Handling**
- **Dynamic File Management** using `os` module
- **Timestamp Management** using `datetime` module

---

## ⚙️ How It Works
### 🔹 1. Registration
- User enters a unique username and a strong password.
- Password rules:
  - At least 8 characters long
  - Contains one uppercase letter
  - Contains one digit
- If successful, details are saved in `customer_details`.

### 🔹 2. Login
- User logs in using their credentials.
- Credentials are verified from `customer_details`.

### 🔹 3. Banking Menu
After login, the user can:
1. **Deposit** money  
2. **Withdraw** money  
3. **Check Balance**  
4. **View Transaction History**  
5. **Logout**

Each transaction is recorded in `<username>_transaction`.

---

## 💾 Example Run
- Welcome to net banking app!
    ----Mainmenu----
- 1.Register
- 2.Login
- 3.Exit

- Choose your option(1-3): 1
- Enter your username: Sanjai
- Character must be 8 or more and contain at least one digit and one uppercase letter
- Enter your password: Sanjai123
- Strong password
- Registered Successfully

Choose your option(1-3): 2
Enter your username: Sanjai
Enter your password: Sanjai123
Login Successfully

1.Deposit
2.Withdraw
3.Check Balance
4.Transaction History
5.Logout
