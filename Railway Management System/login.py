import tkinter as tk

class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.logged_in = False
        self.load_credentials()

    def load_credentials(self):
        try:
            with open('credentials.txt', 'r') as file:
                data = file.readlines()
                if data:
                    self.username, self.password = data[0].strip().split(',')
        except FileNotFoundError:
            pass

    def save_credentials(self):
        with open('credentials.txt', 'w') as file:
            file.write(f"{self.username},{self.password}")

    def login(self, username, password):
        if self.username is None or self.password is None:
            print("Welcome, user!")
            self.username = username
            self.password = password
            self.logged_in = True
            self.save_credentials()
            return True
        elif username == self.username and password == self.password:
            print("Login successful!")
            self.logged_in = True
            return True
        else:
            print("Invalid username or password.")
            return False

class Expense:
    def __init__(self,date,category,amount,is_repeated,is_big,payment_method):
        self.date = date
        self.category = category
        self.amount = amount
        self.is_repeated = is_repeated
        self.is_big = is_big
        self.payment_method = payment_method

class ExpenseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
def main():
    root=tk.Tk()
