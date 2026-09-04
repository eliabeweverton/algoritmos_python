n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))
n3 = float(input("Digite outra nota: "))
media = (n1 + n2 + n3) / 3
print(f"A média das notas é: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")    
