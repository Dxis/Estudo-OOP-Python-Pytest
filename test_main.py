from main import * 

#testes unitarios
def teste_soma(): 
    soma = OperacaoMat()
    assert soma.adicao(2,1) == 3 

#testes unitarios
def teste_soma_Valores_negativos(): 
    soma = OperacaoMat()
    assert soma.adicao(-2,-10) == -12

def test_somar_com_String():
    soma = OperacaoMat()
    assert soma.adicao(5, "A") == 8

def test_somar_numeros_negativos():
    soma = OperacaoMat()
    assert soma.adicao(-5, -3) == -8

def test_somar_numero_positivo_e_negativo():
    soma = OperacaoMat()
    assert soma.adicao(-5, 3) == -2

def test_de_erro_de_proposito():
    soma = OperacaoMat()
    assert soma.adicao(0, 3) == -2    