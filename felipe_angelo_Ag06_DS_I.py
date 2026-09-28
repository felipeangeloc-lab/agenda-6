def calcular_desconto():
    # 1. Entrada de Dados: Solicita ao usuário o valor total da compra
    try:
        valor_compra = float(input("Digite o valor total da compra (R$): "))
        if valor_compra < 0:
            print("O valor da compra não pode ser negativo.")
            return
    except ValueError:
        print("Entrada inválida! Por favor, digite um valor numérico.")
        return

    # 2. Estrutura de Decisão: Utiliza match/case com condições (guards)
    match valor_compra:
        case v if v < 200.00:
            percentual_desconto = 0.05  # 5% de desconto para compras abaixo de R$ 200,00
        case v if v < 300.00:
            percentual_desconto = 0.10  # 10% de desconto para compras de R$ 200,00 até R$ 299,99
        case _:
            percentual_desconto = 0.15  # 15% de desconto para compras a partir de R$ 300,00

    # 3. Processamento: Calcula o valor do desconto e o total a pagar
    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    # 4. Saída de Dados: Exibe os resultados formatados
    print("\n--- RESUMO DA COMPRA ---")
    print(f"Valor original da compra: R$ {valor_compra:.2f}")
    print(f"Desconto aplicado ({int(percentual_desconto * 100)}%): R$ {valor_desconto:.2f}")
    print(f"Valor total a pagar: R$ {valor_final:.2f}")

# Execução da função principal
if __name__ == "__main__":
    calcular_desconto()
