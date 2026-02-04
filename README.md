# 🏦 Mouli Banking System

## 📌 Description
Mouli Banking System is a console-based banking application developed using Python and Object-Oriented Programming (OOP).  
It performs basic banking operations such as adding customers, depositing money, withdrawing money, and viewing account details.

---

## ✨ Features
- ➕ Add new customer with minimum deposit ₹500
- 💰 Deposit money
- 💸 Withdraw money
- 👤 View single customer details
- 📋 View all customers
- 🔒 Prevent duplicate accounts (phone number as unique key)
- ⚠️ Input validation using try-except

---

## 🛠 Technologies Used
- 🐍 Python 3
- 🧠 OOP (Class and Object)
- 📚 Dictionary Data Structure
- 🧪 Exception Handling
- 📟 Menu-Driven Program

---

## 🏗 Program Structure

### 👤 Customer Class
- Stores customer details
- Handles deposit operation
- Handles withdraw operation
- Displays current balance

### 🏦 Store Class
- Manages all customers
- Stores customers using dictionary
- Performs banking transactions

---

## 🗂 Data Storage Method

Customers are stored in a dictionary:

```python
self.bank = {}
```

Each customer is stored using phone number as a unique key:

```python
self.bank[phone] = Customer(name, balance, phone, addr)
```

⚡ Average access time complexity: O(1)

---

## ▶️ How to Run

1. Install Python 3
2. Run the file:

```bash
python filename.py
```

3. Choose options:
- A → Add Member
- B → Deposit
- C → Withdraw
- D → Show Member
- E → Show All Members
- F → Exit

---

## 🚀 Future Improvements
- 📜 Add transaction history
- 🔐 Add password authentication
- 💾 Save data using file handling (JSON / database)
- 📈 Add interest calculation
- 🖥 Convert to GUI application

---

## 👨‍💻 Author
**Moulisankar S**  
B.E Computer Science Engineering (AI & ML)  
Sengundhar Engineering College
