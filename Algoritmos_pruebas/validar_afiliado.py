def validar_afiliado(estado):
    if estado == "activo":
        return "Afiliado activo"
    else:
        return "Afiliado no activo"


estado = "activo"
print(validar_afiliado(estado))