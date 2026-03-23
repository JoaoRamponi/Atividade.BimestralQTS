from main import calcular_total
from main import validar_pedido

def test_calcular_total():
    assert calcular_total(2, 3) == 6
    assert calcular_total(9, 9) == 81
    assert calcular_total(3, 9) == 24
    assert calcular_total(5, 4) == 20
    assert calcular_total(22, 1) == 22


def test_validar_pedido():
    assert validar_pedido(0, 0, 0) == 'Pedido inválido'
    assert validar_pedido(10, 2, 15) == 'Pedido Valido'
    assert validar_pedido(5, 1, 9) == 'Pedido Valido'
    assert validar_pedido(40, 11, 3) == 'Pedido Valido'
    assert validar_pedido(1, 19, 0) == 'Pedido inválido'