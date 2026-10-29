# ==============================================================================
# DESAFIO NÍVEL 1 — PDV COM DESCONTOS PROGRESSIVOS
# Regras aplicadas sem uso de bibliotecas externas, funções (def) ou try/except
# ==============================================================================

# Lista para guardar o histórico de compras do dia
historico_compras = []

print("==========================================")
print("   BEM-VINDO AO SISTEMA DE PDV (CAIXA)    ")
print("==========================================")
print("Digite 0 no valor da compra para encerrar.\n")

# 5. Loop de compras: permite várias compras seguidas
while True:
    # 1. Entrada do valor da compra (número decimal)
    valor_original = float(input("Digite o valor da compra (R$): "))

    # O loop termina quando o usuário digitar 0 no valor da compra
    if valor_original == 0:
        break

    # 7. Validação simples: se o valor for negativo, avisa e pede novamente
    if valor_original < 0:
        print("Aviso: O valor da compra não pode ser negativo. Tente novamente.\n")
        continue

    # 1. Entrada da idade do cliente (número inteiro)
    idade = int(input("Digite a idade do cliente: "))

    # 7. Validação simples: se a idade for negativa, avisa e pede novamente
    if idade < 0:
        print("Aviso: A idade do cliente não pode ser negativa. Tente novamente.\n")
        continue

    # Começamos o cálculo com o valor original da compra
    valor_com_desconto = valor_original

    # 2. Regra 1 — Desconto por idade:
    # Se a idade for maior ou igual a 65 anos, aplica 20% de desconto
    if idade >= 65:
        valor_com_desconto = valor_com_desconto * 0.80

    # 3. Regra 2 — Desconto por valor:
    # Se o valor JÁ COM O DESCONTO DE IDADE for maior que 100 reais,
    # aplica mais 10% de desconto sobre esse valor
    if valor_com_desconto > 100:
        valor_com_desconto = valor_com_desconto * 0.90

    # Calcula quanto o cliente economizou nesta compra
    desconto_concedido = valor_original - valor_com_desconto

    # 4. Exibe o valor final no console formatado em reais com duas casas decimais
    print(f"Valor final: R$ {valor_com_desconto:.2f}\n")

    # 6. Guarda os dados da compra na lista usando .append()
    registro_compra = [valor_original, idade, desconto_concedido, valor_com_desconto]
    historico_compras.append(registro_compra)

# ==============================================================================
# 6. HISTÓRICO E RESUMO FINAL DO DIA
# ==============================================================================
quantidade_compras = len(historico_compras)
total_bruto = 0.0
total_descontos = 0.0
total_final = 0.0

# Soma os valores percorrendo a lista de compras registradas
for compra in historico_compras:
    total_bruto = total_bruto + compra[0]
    total_descontos = total_descontos + compra[2]
    total_final = total_final + compra[3]

print("\n==========================================")
print("            RESUMO DO DIA                 ")
print("==========================================")
print(f"Quantidade de compras registradas: {quantidade_compras}")
print(f"Total bruto:                       R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos:     R$ {total_descontos:.2f}")
print(f"Total final:                       R$ {total_final:.2f}")
print("==========================================")
