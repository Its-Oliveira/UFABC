def pim(n:int) -> str:
    cont = 1
    resp = ''
    for i in range(0,n):
        resp += f'{cont} {cont+1} {cont+2} PIM \n'
        cont+=4
    return resp

def main():
    n = int(input())
    resposta = pim(n)
    print(resposta)
        
main()