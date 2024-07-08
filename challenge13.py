#Cuenta bancaria: Implementa una clase CuentaBancariacon métodos para depositar y consultar el saldo.


class Bankaccount:
    def __init__(self):
        self.balance = 0
        
    def deposit_money(self, deposit):
        self.balance += deposit
        
    def check_balance(self):
        print(f"Tenes disponible {self.balance} gs en tu cuenta")
        
        
bankaccount = Bankaccount()
bankaccount.deposit_money(int(input(f"Cuanto dinero quieres depositar en tu cuenta?")))
bankaccount.check_balance()
