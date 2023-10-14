animais = {"gato", "cachorro", "passaro", "cavalo"}
animais.add("peixe")
print(animais)
animais.remove("passaro")
print(animais)
try:
    animais.remove("lagarto")
except KeyError as e:
    print(f"Erro {e}")
animais.discard("lagarto")
print(animais)
animais.pop()
print(animais)
animais.clear()
print(animais)