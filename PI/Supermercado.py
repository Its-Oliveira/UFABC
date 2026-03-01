def caixa(q:int,p:float,soma_q: int,soma_valor:float):

    total = q*p
    soma_valor += total
    soma_q += q

    return soma_q, soma_valor

def main():
    soma_quantidade = 0
    valor_total = 0

    cont = 0
    while cont == 0:
        quantidade = int(input())
        if quantidade != 0:
            prec_unit = float(input())
            soma_quantidade,valor_total = caixa(quantidade,prec_unit,soma_quantidade,valor_total)
        else:
            cont+=1

    if soma_quantidade == 1:
        print(f'Foi comprado 1 item, totalizando R${valor_total:.2f}')
    else:
        print(f'Foram comprados {soma_quantidade} itens, totalizando R${valor_total:.2f}')
    
        
    
main()