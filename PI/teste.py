def tabuleiro(n:int) -> str:
    tabuleiro_completo = ''
    for i in range(n):
        linha = ''
        for j in range(n):
                if (i + j) % 2 == 0:
                    linha = linha + 'o'
                else:
                    linha = linha + '*'
        tabuleiro_completo += linha + '\n'
        
    return tabuleiro_completo
        
def main():
    numero = int(input())
    resultado = tabuleiro(numero)
    print(resultado)

main()