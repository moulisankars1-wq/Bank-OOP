from datetime import datetime


class Customer:
    MINIMUM_BALANCE = 500

    def __init__(self, name, balance, phone, address):
        self.name = name
        self.balance = balance
        self.phone = phone
        self.address = address
        self.history = []

        self._add_history(
            "ACCOUNT_OPENED",
            balance,
            self.balance
        )

    def _add_history(self, transaction_type, amount, balance_after):
        self.history.append({
            "type": transaction_type,
            "amount": amount,
            "balance": balance_after,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than 0."

        self.balance += amount

        self._add_history(
            "DEPOSIT",
            amount,
            self.balance
        )

        return True, f"₹{amount} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."

        if amount > self.balance:
            return False, "Insufficient balance."

        if self.balance - amount < self.MINIMUM_BALANCE:
            return False, (
                f"Minimum balance of ₹{self.MINIMUM_BALANCE} "
                "must be maintained."
            )

        self.balance -= amount

        self._add_history(
            "WITHDRAW",
            amount,
            self.balance
        )

        return True, f"₹{amount} withdrawn successfully."

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def show_details(self):
        print("\n--------- CUSTOMER DETAILS ---------")
        print(f"Name     : {self.name}")
        print(f"Phone    : {self.phone}")
        print(f"Address  : {self.address}")
        print(f"Balance  : ₹{self.balance}")
        print("------------------------------------")

    def show_history(self):
        if not self.history:
            print("No transactions found.")
            return

        print("\n------------- TRANSACTION HISTORY -------------")

        for transaction in self.history:
            print(
                f"{transaction['time']} | "
                f"{transaction['type']:<15} | "
                f"Amount: ₹{transaction['amount']:<8} | "
                f"Balance: ₹{transaction['balance']}"
            )

        print("------------------------------------------------")


class Store:
    def __init__(self):
        self.bank = {}

    def add_member(self, name, phone, address, initial_balance):
        if phone in self.bank:
            return False, "Customer already exists."

        if initial_balance != Customer.MINIMUM_BALANCE:
            return False, (
                f"Initial deposit must be exactly "
                f"₹{Customer.MINIMUM_BALANCE}."
            )

        customer = Customer(
            name,
            initial_balance,
            phone,
            address
        )

        self.bank[phone] = customer

        return True, f"{name}'s account opened successfully."

    def find_customer(self, phone):
        return self.bank.get(phone)

    def deposit_money(self, phone, amount):
        customer = self.find_customer(phone)

        if customer is None:
            return False, "Customer does not exist."

        return customer.deposit(amount)

    def withdraw_money(self, phone, amount):
        customer = self.find_customer(phone)

        if customer is None:
            return False, "Customer does not exist."

        return customer.withdraw(amount)

    def show_member(self, phone):
        customer = self.find_customer(phone)

        if customer is None:
            print("Customer does not exist.")
            return

        customer.show_details()

    def show_all_members(self):
        if not self.bank:
            print("No members found.")
            return

        print("\n============== ALL MEMBERS ==============")

        for customer in self.bank.values():
            print(
                f"Name: {customer.name} | "
                f"Phone: {customer.phone} | "
                f"Balance: ₹{customer.balance}"
            )

        print("==========================================")

    def show_history(self, phone):
        customer = self.find_customer(phone)

        if customer is None:
            print("Customer does not exist.")
            return

        customer.show_history()


def get_phone():
    while True:
        phone = input("Enter phone number: ").strip()

        if not phone.isdigit():
            print("Phone number must contain digits only.")
            continue

        if len(phone) != 10:
            print("Phone number must contain exactly 10 digits.")
            continue

        return phone


def get_amount():
    while True:
        amount = input("Enter amount: ").strip()

        try:
            amount = int(amount)

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid numeric amount.")


def get_name():
    while True:
        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain letters only.")
            continue

        return name


def get_address():
    while True:
        address = input("Enter your address: ").strip()

        if not address:
            print("Address cannot be empty.")
            continue

        return address


def add_member(store):
    print("\n========== ADD MEMBER ==========")

    name = get_name()
    phone = get_phone()

    if store.find_customer(phone):
        print("Customer already exists.")
        return

    address = get_address()

    print(
        f"Initial deposit required: "
        f"₹{Customer.MINIMUM_BALANCE}"
    )

    initial_balance = get_amount()

    success, message = store.add_member(
        name,
        phone,
        address,
        initial_balance
    )

    print(message)


def deposit_money(store):
    print("\n========== DEPOSIT ==========")

    phone = get_phone()

    if store.find_customer(phone) is None:
        print("Customer does not exist.")
        return

    amount = get_amount()

    success, message = store.deposit_money(
        phone,
        amount
    )

    print(message)

    if success:
        customer = store.find_customer(phone)
        print(f"New balance: ₹{customer.balance}")


def withdraw_money(store):
    print("\n========== WITHDRAW ==========")

    phone = get_phone()

    if store.find_customer(phone) is None:
        print("Customer does not exist.")
        return

    amount = get_amount()

    success, message = store.withdraw_money(
        phone,
        amount
    )

    print(message)

    if success:
        customer = store.find_customer(phone)
        print(f"New balance: ₹{customer.balance}")


def show_member(store):
    print("\n========== SHOW MEMBER ==========")

    phone = get_phone()
    store.show_member(phone)


def show_history(store):
    print("\n========== TRANSACTION HISTORY ==========")

    phone = get_phone()
    store.show_history(phone)


def main():
    store = Store()

    while True:
        print("\n")
        print("======================================")
        print("        MOULI BANKING SYSTEM")
        print("======================================")
        print("A. Add Member")
        print("B. Deposit Amount")
        print("C. Withdraw Amount")
        print("D. Show Member")
        print("E. Show Transaction History")
        print("F. Show All Members")
        print("G. Exit")
        print("======================================")

        choice = input("Enter option: ").strip().upper()

        if choice == "A":
            add_member(store)

        elif choice == "B":
            deposit_money(store)

        elif choice == "C":
            withdraw_money(store)

        elif choice == "D":
            show_member(store)

        elif choice == "E":
            show_history(store)

        elif choice == "F":
            store.show_all_members()

        elif choice == "G":
            print("\nThank you for using Mouli Banking System!")
            break

        else:
            print(
                "Invalid option. "
                "Please choose A, B, C, D, E, F, or G."
            )


if __name__ == "__main__":
    main()
