tot18 = totH = totM20 = 0
print("-"*25)
print("CADASTRE UMA PESSOA")
print("-"*25)
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo == "M":
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 +=1
    print("-"*25)
    cont = " "
    while cont not in "SN":
        cont = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        continue
    if cont == "N":
        print("====== FIM DO PROGRAMA ======")
        print(f"Total de pessoas com mais de 18 anos: {tot18}")
        print(f"Ao todo temos {totH} homens cadastrados")
        print(f"E temos {totM20} mulheres com menos de 20 anos")
        break       