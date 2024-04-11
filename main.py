class OperacaoMat:
    def adicao(self,valor1,valor2):
        return valor1 + valor2

class Pessoa:
    def __init__(self, Nome,Idade, Cidade) -> None:
        self.Nome = Nome
        self.Idade = Idade
        self.Cidade = Cidade

    def estuda(self):
        print(f' {self.Nome} estuda todos os dias, pois gosta de estar em constante aprendizado.\n')

    def Pontos_fortes(self,condicao):
        if condicao ==1:
            print(f' {self.Nome} Resolve problemas complexos.')
        if condicao ==1:
            print(f' {self.Nome} Possui habilidade analítica.')    
        if condicao ==2:
            print(f' {self.Nome} é extremamente organizado.')
        if condicao ==2:
            print(f' {self.Nome} é proativo.')
        if condicao ==2:
            print(f' {self.Nome} é multitarefa.\n')    

    def Pontos_fracos(self):      
        print(f' {self.Nome} Gosta de estar em constante aprendizado.')
   
        print(f' {self.Nome} Fica chateado com quem não quer fazer seu melhor. T-Rex\n')


if __name__ == "__main__":
    soma =OperacaoMat()
    valor1 = 1
    valor2 = 2 
    resultado = soma.adicao(valor1,valor2)
    print(f"A soma de {valor1} e {valor2} é {resultado}.")