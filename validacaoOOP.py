from main import Pessoa 

#Carregando "herdando" atributos e métodos da classe Pessoa ()
pessoa = Pessoa("Diego",34,"Diadema")

print("Estudo prático sobre Programação orientado a Objetos em Python \n")
#acessando atributos da classe pessoa
print("Acessando atributos da classe pessoa")
nome = pessoa.Nome
idade = pessoa.Idade
cidade = pessoa.Cidade
print(f'O candidato se chama {nome}, possui {idade} anos e reside na cidade de {cidade}.\n')

#Acessando o método "estuda" com condição
print("Acessando o método Estuda()")
pessoa.estuda()

print("Acessando o método Pontos_forte() com condição \n")
print("Pontos forte")
pessoa.Pontos_fortes(1) 
pessoa.Pontos_fortes(2) 

print("Acessando o método Pontos_fracos() sem condição")
print("Pontos fracos")
#Acessando o método "Pontos_fracos" sem condição
pessoa.Pontos_fracos()