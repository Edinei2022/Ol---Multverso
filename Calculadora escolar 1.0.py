## Calculadora de mídia de Aluno ##

nota_1 = float(input("Digite a Primeira nota:"))
nota_2 = float(input("Digite a Segunda nota:"))
nota_3 = float(input("Digite a nota Terceira:"))
nota_4 = float(input("Digite a quarta nota:"))
nota = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(nota)
if nota == 10:
    print("Parabêns, vocé foi aprovado com Louvor.")

elif nota >=7:
    print("Aprovado")

elif nota <= 5:
    print("você esta reprovado")

else:
    print("Você esta em recuperação")

## Teste no Browser ##
