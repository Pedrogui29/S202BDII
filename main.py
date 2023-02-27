# Relatorio 1

# Criando Classe Animal:

class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

        def emitir_som(self, som):
            return som

        def mudar_cor(self, corDiferente):
            self.cor = corDiferente
            return corDiferente

# Criando classe elefante se estendendo de animal
class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        return f"Som do elefante: {self.som}"

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho


#Criando elefante
nome = input("Digite o nome do elefante: " + str())
idade = float(input("Digite a idade do elefante: " ))
especie = input("Digite a especie do elefante: " +str())
cor = input("Digite a cor do elefante: " +str())
som = input("Digite o som do elefante: " +str())
tamanho = input("Digite o tamanho do elefante: " +str())

#Condicao para mudar seu tamanho e som caso seja africano
if especie == "Africano":
    if idade < 10:
        tamanho = "pequeno"
        som = "Paaah"
    else:
        tamanho = "grande"
        som = "PAAAAAHHH"


elefante = Elefante(nome, idade, especie, cor, som, tamanho)

#Mostrando os dados do elefante
print("Características do Elefante: " + elefante.nome + ", " + str(elefante.idade) + ", " + elefante.especie
      + ", " + elefante.cor + ", " + elefante.tamanho + ", " + elefante.som)