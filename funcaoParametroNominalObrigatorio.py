def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")


for chave, valor in kwargs.items():
    print(f"variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros('São Paulo', idade=40, nome="Dimas")
print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)
