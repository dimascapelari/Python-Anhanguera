# O parâmetro flag_minuscula possui True como valor default
def converter_minuscula(texto, flag_minuscula=True):
    if flag_minuscula:
        return texto.upper()
    else:
        return texto.lower()


texto1 = converter_minuscula(
    flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")
print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")
