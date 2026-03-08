def tabuleiro(n:int) -> str:
    tabuleiro_completo = ''
    for i in range(n):
        linha = ''
        if i % 2 ==0:
            for j in range(n):
                if j % 2 == 0:
                    linha = linha + 'o'
                else:
                    linha = linha + '*'
            tabuleiro_completo += linha + '\n'
        else:
            for j in range(n):
                if j % 2 == 0:
                    linha = linha + '*'
                else:
                    linha = linha + 'o'
            tabuleiro_completo += linha + '\n'
    return tabuleiro_completo
        
def main():
    numero = int(input())
    resultado = tabuleiro(numero)
    print(resultado)

main()