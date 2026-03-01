Valor_total = 0
qtd_total = 0
cont = 0

while cont == 0:
    quantidade = int(input())
    if quantidade != 0:
        prec_unit = float(input())
        prec_total = quantidade * prec_unit
        Valor_total += prec_total
        qtd_total += quantidade
    else:
        cont+=1

if qtd_total == 1:
    print(f'Foi comprado {qtd_total} item, totalizando R${Valor_total:.2f}')
else:
    print(f'Foram comprados {qtd_total} itens, totalizando R${Valor_total:.2f}')