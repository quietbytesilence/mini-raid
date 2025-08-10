with open("parte1.txt", "r") as arquivo1:
    p1 = arquivo1.read().strip().replace(' ','')
with open("parte2.txt", "r") as arquivo2:
    p2 = arquivo2.read().strip().replace(' ','')
with open("parte3.txt", "r") as arquivo3:
    p3 = arquivo3.read().strip().replace(' ','')

def calcular_paridade(p1, p2, p3):
    paridade = ""
    for p, q, r in zip(p1, p2, p3):
        bit_paridade = int(p) ^ int(q) ^ int(r)
        paridade += str(bit_paridade)
    return paridade

paridade = calcular_paridade(p1, p2, p3)

print("Calculando paridade....")

with open("paridade.txt", "w") as pari:
    pari.write(f'{paridade}')

print("paridade calculada\n\n")

arquivo1.close()
arquivo2.close()
arquivo3.close()

input("Tudo pronto, se quiser pode testar\napagando um arquivo e tocando em <ENTER>")

print("Certo, agora vamos ver qual arquivo foi apagado..")

def recuperar(op):
    if op ==1:
        rec = calcular_paridade(p2, p3, paridade)

    if op ==2:
        rec = calcular_paridade(p1, p3, paridade)

    if op ==3:
        rec = calcular_paridade(p1, p2, paridade)
    print(f'Conteúdo do arquivo {op} recuperado com sucesso')

    print(f'\nConteúdo:\n{rec}')
    with open(f"parte{op}.txt", "w") as novo:
        novo.write(f"{rec}")
    print("\nConteúdo Reecrito")


try:
    with open("parte1.txt", "r") as arquivo1:
        p1 = arquivo1.read().strip().replace(' ','')
except:
    recuperar(1)

try:   
    with open("parte2.txt", "r") as arquivo2:
        p2 = arquivo2.read().strip().replace(' ','')
except:
    recuperar(2)

try:    
    with open("parte3.txt", "r") as arquivo3:
        p3 = arquivo3.read().strip().replace(' ','')
except:
    recuperar(3)



