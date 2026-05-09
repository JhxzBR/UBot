import re

def responder(entrada):
    if re.search(r"\b(olá|oi|Olá|ola|Ola|Oi)\b", entrada):
        return "Olá, sou a UBot, como posso ajudar."
    elif re.search(r"\b(tudo bem|Tudo bem|blz|de boa|como vai|eai)\b", entrada):
        return "Tudo bem, e com você?E como posso te ajudar."
    else:
        return "Não entendi, digite Olá para começar a conversar comigo."

print("Bem-vindo(a) ao UBot, digite Sair para sair.")

while True:
    user_input = input("Você: ").lower()
    if user_input == "sair":
        print("UBot: Tchau, até a próxima!")
        break
    resposta = responder(user_input)
    print(f"UBot: {resposta}")