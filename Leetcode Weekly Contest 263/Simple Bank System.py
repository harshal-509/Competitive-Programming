class Bank:

    def __init__(self, balance: List[int]):
        self.ans=balance
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        try:
            m=self.ans[account1-1]
            n=self.ans[account2-1]
            if(money<=self.ans[account1-1]):
                self.ans[account1-1]-=money
                self.ans[account2-1]+=money
                return 1
            else:
                return 0
        except:
            return 0
    def deposit(self, account: int, money: int) -> bool:
        try:
            self.ans[account-1]+=money
            return 1
        except:
            return 0
    def withdraw(self, account: int, money: int) -> bool:
        try:
            if(money<=self.ans[account-1]):
                self.ans[account-1]-=money
                return 1
            else:
                return 0
        except:
            return 0


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)