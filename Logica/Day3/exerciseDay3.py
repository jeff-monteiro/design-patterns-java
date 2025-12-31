# Validação de idade para CNH
"""
idade_min = int(input("Digite sua idade: "))
possui_cnh = True

def rules_to_rent(possui_cnh, idade_min):
    if(idade_min >= 18 and possui_cnh == True):
        print("Pode obter um carro e dirigir.")
    else:
        print("Não pode obter um carro.")

rules_to_rent(possui_cnh, idade_min)
"""

# Inversão de condição
"""
chovendo = False
nao_chovendo = not chovendo
print("Está chovendo? ", chovendo)
print("Não está chovendo? ", nao_chovendo)
"""

# Cálculo de pagamento e troco
"""
pao = float(input("Insira o primeiro valor: "))
leite = float(input("Insira o segundo valor: "))
cafe = float(input("Insira o terceiro valor: "))

def recebe_dados(item1: float, item2: float, item3: float):
    return item1, item2, item3


def total_compra(item1: float, item2: float, item3: float) -> float:
    return item1 + item2 + item3


def total_troco(valor_pago, total_compra)-> float:
    return valor_pago - total_compra
    

produtos = recebe_dados(pao, leite, cafe)
total = total_compra(*produtos)
troco = total_troco(20, total)

print(f"Total da compra: {total:.2f}")
print(f"O total do seu troco: ", troco)
""" 

#Verificando Aprovação em um Exame
"""
def nota_media():
    nota1 = float(input("Insira sua nota 1: "))
    nota2 = float(input("Insira sua nota 2: "))

    media = (nota1 + nota2) / 2
    return media

def frequencia():
    frequencia = int(input("Insira sua frequência: "))
    return frequencia


def resultado_exame(media, frequencia):
    if(media >= 7 and frequencia >= 80):
        print("Aprovado")
    else:
        print("Reprovado")


media_final = nota_media()
frequencia_final = frequencia()
resultado_final = resultado_exame(media_final, frequencia_final)
"""


# Calcular Oferta Especial
"""
def valor_desconto(quantidade_items, valor_total):

    if(quantidade_items > 10 or valor_total >= 120):
        desconto = valor_total * 0.1
        print("Valor do desconto aplicado! ", desconto)
    else:
        desconto = 0
        print("Não atende a nenhum dos requisitos para desconto!")
        
    return desconto


def valor_pagar_com_desconto(valor_total, desconto):
    total_com_desconto = valor_total - desconto
    return print("Valor pago com desconto: ", total_com_desconto)

quantidade_items = int(input("Quantidade de itens: "))
valor_total = float(input("Valor dos produtos: "))

desconto = valor_desconto(quantidade_items, valor_total)
valor_pagar_com_desconto(valor_total, desconto)
"""


