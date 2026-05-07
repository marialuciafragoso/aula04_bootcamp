#NOME DO USUÁRIO:
def pegar_nome() -> str:
    while True:
        nome = input("Digite seu nome: ")
        if nome.isdigit():
            print("Não insira números!")
        elif len(nome) == 0:
            print("Digite seu nome novamente!")
        elif nome.isspace():
            print("Digite seu nome novamente!")
        else:
            return nome 
        
#SALARIO DO USUARIO:
def pegar_salario() -> float:
    while True:
        try :
            salario = float(input("Digite seu salario: "))

            if salario < 0:
                print("Insira um numero positivo")
            else:
                return salario
            
        
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")
            
#BONUS DO USUARIO
def pegar_bonus() -> float:
    while True:
        try:
            porcentagem_do_bonus = float(input("porcentagem do bonus em %: ").replace(",","."))
            if  porcentagem_do_bonus < 0:
                print("Bônus não pode ser negativo")
            else:
                return porcentagem_do_bonus

        except ValueError:
            print("Apenas números, por favor!")
            
#CÁLCULO DO VALOR DO BONUS 
def calcular_valor_do_bonus (salario: float, porcentagem_do_bonus: float) -> float:
    return 1000 + salario * porcentagem_do_bonus / 100 


def exibir_resultado(usuario: dict) -> None:
    print(f"O usuário {usuario['nome']} possui bônus de {usuario['bonus_valor']}")
    print(f"O salário total do usuário {usuario['nome']} é de {usuario['salario_total']}")


