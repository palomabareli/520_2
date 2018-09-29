from behave import step

def soma(x: int, y: int) -> int :
    return x + y

@step('somar "{num1}" com "{num2}" ')  
#context é o atributo da classe de objeto do framework  
def teste_soma(context, num1, num2):
    context.r_soma = soma(int(num1), int(num2))

@step('o resultado deve ser "{esperado}"')    
#contexto, este, recebeu os valores do teste acima
def teste_soma_resultado(context, esperado):
    assert context.r_soma == int(esperado), "descrição do erro"