def calcular_desconto(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if valor_pedido >= 100:
        return valor_pedido * 0.10

    return 0