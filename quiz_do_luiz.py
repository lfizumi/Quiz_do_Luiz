
print("Boas vindas ao quiz do luiz!")
pergunta_ao_usuario = input("Deseja comecar? (Sim/Não)")
print(pergunta_ao_usuario)
if pergunta_ao_usuario != "Sim" and pergunta_ao_usuario != "sim":
    quit()
score = 0

print("Começando...")
print("Quando surgiu o primeiro o jogo god of war? \n (A)2005 \n (B)2008 \n (C)2007 \n (D)2009 \n")
resposta_1 = input("Resposta:")

if resposta_1 == "A":
    print("Acertou!")
    score = score + 1
else:
    print("Incorreto!")

print("Em que ano foi lançado o primeiro console PlayStation? \n (A)1993 \n (B)1994 \n (C)1995 \n (D)1996 \n")
resposta_2 = input("Resposta:")

if resposta_2 == "B":
    print("Acertou!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o nome do protagonista da série The Legend of Zelda? \n (A)Zelda \n (B)Ganondorf \n (C)Link \n (D)Epona \n")
resposta_3 = input("Resposta:")

if resposta_3 == "C":
    print("Acertou!")
    score = score + 1
else:
    print("Incorreto!")

print("Em que ano foi lançado o jogo Red Dead Redemption 2? \n(A)2016 \n (B)2017 \n (C)2018 \n (D)2019 \n")
resposta_4 = input("Resposta:")

if resposta_4 == "C":
    print("Acertou!")
    score = score + 1
else:
    print("Incorreto!")

print("Em qual jogo Mario apareceu pela primeira vez? \n (A)Super Mario Bros \n (B)Donkey Kong \n (C)Mario Kart \n (D)Mario Party \n")
resposta_5 = input("Resposta:")

if resposta_5 == "B":
    print("Acertou!")
    score = score + 1
else:
    print("Incorreto!")

print(f" Quiz Finalizado, sua pontução foi de {score}/5")
