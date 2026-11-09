import pytest
from src.regras_localeats import calcular_desconto

# Testes para a função calcular_desconto

def test_calcular_desconto_pedido_acima_de_100():
    resultado = calcular_desconto(150)
    assert resultado == 15


def test_calcular_desconto_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-50)