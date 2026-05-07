import valores
for f in range(3):
    funcionario = {
    "nome": valores.pegar_nome(),
    "salario": valores.pegar_salario(),
    "bonus": valores.pegar_bonus()
    }

    funcionario["bonus_valor"] = valores.calcular_valor_do_bonus(funcionario["salario"], funcionario["bonus"])
    funcionario["salario_total"] = funcionario["salario"] + funcionario["bonus_valor"]

    valores.exibir_resultado(funcionario)