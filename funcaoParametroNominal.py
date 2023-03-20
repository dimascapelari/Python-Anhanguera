def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()


# Passagem nominal de parâmetros
texto = converter_maiuscula(flag_maiuscula=True, texto="Dimas")
print(texto)
