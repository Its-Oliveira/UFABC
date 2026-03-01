def verificao(i:int, p:float, td:str, rh_d:str,tr:str,rh_r:str) -> str:
    if i < 16 or i > 69 or p < 50:
        resp = "Doador não satisfaz requisitos mínimos"
    else:
        if rh_r == "-" and rh_d == "+":
            resp = "Tipos sanguíneos incompatíveis"
        else:
            if tr == "A" and (td == "A" or td == "O"):
                resp = "Tipos sanguíneos compatíveis"

            elif tr == "B" and (td == "B" or td == "O"):
                resp = "Tipos sanguíneos compatíveis"

            elif tr == "O" and td == "O":
                resp = "Tipos sanguíneos compatíveis"

            elif tr == "AB" and (td == "B" or td == "O" or td == "A" or td == "AB"):
                resp = "Tipos sanguíneos compatíveis"

            else: 
                resp = 'Tipos sanguíneos incompatíveis'
    return resp

def main():
    idade = int(input())
    peso = float(input())
    tipo_doador = str(input())
    rh_doador = str(input())
    tipo_recep = str(input())
    rh_recep = str(input())

    res = verificao(idade, peso,tipo_doador,rh_doador,tipo_recep,rh_recep)
    print(res)

main()