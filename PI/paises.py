def calculo_idh(a:str,b:float):
    if b >= 0.80:
        resp = (f'{a} possui IDH muito alto')
    elif b >= 0.70:
        resp = (f'{a} possui IDH alto')
    elif b >= 0.55:
        resp = (f'{a} possui IDH médio')
    else:
        resp = (f'{a} possui IDH baixo')

    return resp

def main():
    resposta_final = ''
    n = int(input())
    for i in range(0,n):
        pais = str(input())
        idh = float(input())
        resposta = calculo_idh(pais,idh)
        resposta_final += resposta+'\n'
        
    print(resposta_final)

main()
    