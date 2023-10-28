class Calculadora:

    def __init__(self):
        self.numero_um = 0
        self.numero_dois = 0

    def somar(self):
        self.verifica_numeros()
        return self.numero_um + self.numero_dois
    
    def multiplicar(self):
        self.verifica_numeros()
        return self.numero_um * self.numero_dois
    
    def dividir(self):
        self.verifica_numeros()
        
        if self.numero_dois == 0:
            print("Não é possivel dividir por zero")
            return
        
        return self.numero_um / self.numero_dois
    
    def elevar(self):
        self.verifica_numeros()
        return self.numero_um ** self.numero_dois
    
    def subtrair(self):
        self.verifica_numeros()
        return self.numero_um - self.numero_dois
    
    def verifica_numeros(self):
        if not isinstance(self.numero_um, (int, float)):
            print("O numero um não é válido")
        
        if not isinstance(self.numero_dois, (int, float)):
            print("O numero dois não é válido")

    def solicita_numeros(self):
        self.numero_um = float(input("Qual o primeiro número: "))
        self.numero_dois = float(input("Qual o segundo número: "))