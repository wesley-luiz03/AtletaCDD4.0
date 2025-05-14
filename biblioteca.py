class Atleta():
    def __init__(self, nome):
            self.nome = nome
            self.aposentado = False
            self.aquecimento = False
    
    def Aquecer(self):
        if self.aquecimento == False:
            print("O atleta está aquecido.")
            self.aquecimento = True
        else:
            print("O atleta já se aqueceu.")
    
    def Aposentar(self):
        if self.aposentado == False:
            print("O atleta está aposentado.")
            self.aposentado = True
        else:
            print("O atleta já está aposentado.")

class Corredor(Atleta):
    def __init__(self, nome):
        super().__init__(nome)
        
    def correr(self):
        if self.aposentado == True:
            print (f"O atleta {self.nome} está aposentado.")
        elif self.aquecimento == False:
            print (f"O atleta {self.nome} precisa aquecer antes.")
        else:
            print (f"O atleta {self.nome} está competindo na modalidade NATAÇÃO!")

class Nadador(Atleta):
    def __init__(self, nome):
         super().__init__(nome)
         
    def nadar(self):
        if self.aposentado == True:
            print(f"O atleta {self.nome} está aposentado.")
        elif self.aquecimento == False:
            print(f"O atleta {self.nome} precisa aquecer.")
        else:
            print(f"O atletica {self.nome} está competindo na modalidade NATAÇÃO!!")

class Ciclista(Atleta):
    def __init__(self, nome):
        super().__init__(nome)

    def ciclismo(self):
        if self.aposentado == True:
            print(f"O atleta {self.nome} está aposentado.")
        elif self.aquecimento == False:
            print(f"O atleta {self.nome} precisa aquecer.")
        else:
            print(f"O atletica {self.nome} está competindo na modalidade CICLISMO!")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome):
        super().__init__(nome)
    