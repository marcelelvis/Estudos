class conta:
    def __init__(self,i, s):
        self.ID = i
        self.saldo = s
    def deposito(self, v):
        self.saldo += v
    def saque(self,v):
        if self.saldo >= v:
            self.saldo -= v
    def __len__(self, outro):
        if self.ID <= outro.ID:
            return True
        return False
    def __eq__(self, outro):
        if self.ID == outro.ID:
            return True
        return False
    def __ge__(self, outro):
        if self.ID > outro.ID:
            return True
        return False
    def __lt__(self, outro):
        if self.ID < outro.ID:
            return True
        return False
    def __gt__(self, outro):
        if self.ID > outro.ID:
            return True
        return False
    def __ne__(self, outro):
        if self.ID != outro.ID:
            return True
        return False

itau = conta(123, 4000)
bradesco = conta(123, 5000)

#Comparar objetos, devolve um bool
#__le__ x <= y, __eq__ x ==y, __ge__ x>y, __lt__ x<y, __gt__ x > y, __ne__ x != y
#print(itau == bradesco)