class pessoa():
    def __init__(self,nomeAluno,pesoAluno,idadeAluno):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno

        self.estado ="parado"


    def estadoParado(self):
        self.estado = "parado"
        print(f"{self.nome} esta parado!")
    def comer(self):
        if self.estado == "parado":
            self.estado = "comendo"
            print(f"{self.nome} esta comendo ")
        elif self.estado == "comendo":
            print(f"{self.nome} ja esta comendo!")
        else:
            print(f"{self.nome} nao pode comer no momento!")
    def andar(self):
        if self.estado == "parado":
            self.estado = "andando"
            print(f"{self.nome} esta andando")
        elif self.estado == "andando":
            print(f"{self.nome} ja esta andando!")
        else:
            print(f"{self.nome} nao pode andar no momento")
    def falar(self):
            if self.estado == "parado":
                self.estado = "falando"
                print(f"{self.nome} esta falando")
            elif self.estado == "falando":
                print(f"{self.nome} ja esta falando!")
            else:
                print(f"{self.nome} nao pode falar no momento")
