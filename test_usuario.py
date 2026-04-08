from main import calcular_total
from main import validar_pedido

def test_calcular_total_certo():
    assert calcular_total(10, 15) == 150
    
def test_validar_pedido_sucesso():
    assert validar_pedido(10, 2, 4) == 'Pedido Valido'

def test_validar_pedido_errado():
    assert validar_pedido(1, 9, 0) == 'Pedido inválido'