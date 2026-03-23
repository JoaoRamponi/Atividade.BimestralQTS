def calcular_total(quantidade, valor_unitario):
    return quantidade * valor_unitario

def validar_pedido(item, quantidade, valor_unitario):
    if item <= 0:
        return ("Pedido inválido")
    
    elif quantidade <= 0:
        return ("Pedido inválido")
    
    elif valor_unitario <= 0:
        return ("Pedido inválido")

    else:
        return("Pedido Valido")