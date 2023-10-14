#VERIFICANDO O PRODUTO MAIS VENDIDO
def resumo_vendas (vendas_smartphone, vendas_smartwhat):
    total_vendas = vendas_smartphone + vendas_smartwhat
    mais_vendido = "Smartphone" if vendas_smartphone > vendas_smartwhat else "Smartwhat"
    return total_vendas, mais_vendido

total, produto_vendido = resumo_vendas(150, 100)
print (f"Total de vendas = {total}")
print (f"Produto mais vendido {produto_vendido}\n")

#---------------------------------------------------------
#APONTANDO A VENDA DIÁRIA DE APARELHOS
vendas_semana = [(70,65),(80,82),(90,88)]
for vendas_smartphone, vendas_smartwhat in vendas_semana:
    print (f" FORAM VENDIDOS {vendas_smartphone} SMARTPHONES  E {vendas_smartwhat} SMARTWHATCHES ")
print()
# ------------------------------------------------------------------------------
#TROCANDO OS VALORES PARA CORREÇÃO

vendas_segunda = (70,65)
vendas_correta = (65, 70)
vendas_segunda= vendas_correta
print(f'OS VALORES CORRIGIDOS DAS VENDAS DE SEGUNDA SÃO: {vendas_segunda}')
