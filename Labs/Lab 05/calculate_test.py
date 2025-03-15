class Bank():
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, initial_balance):
        self.accounts[account_id] = initial_balance

    def get_account_balance(self, account_id):
        return self.accounts[account_id]
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts and amount > 0:
            self.accounts[account_id] += amount
    
    def withdraw(self, account_id, amount):
        if account_id in self.accounts and 0 < amount <= self.accounts[account_id]:
            self.accounts[account_id] -= amount
import unittest 

class BankTest(unittest.TestCase):
    def setup(self):
        self.bank = Bank()
        self.bank.add_account('123', 100)
    def test_add_account(self):
        self.bank.add_account('1234', 200)
        self.assertEqual(self.bank,get_account_balance('1234'), 200)
    def test_deposit(self):
        self.bank.deposit('123', 50)
        self.assertEqual(self.bank.get_account_balance('123'), 150)
    def test_withdraw(self):
        self.bank.withdraw('123', 30)
        self.assertEqual(self.bank.get_account_balance('123'), 70)
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
            
