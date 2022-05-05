def CDT(usuario , capital , tiempo):
    if tiempo > 2:
        porcentajeIntereses = 0.03
        valorIntereses = (capital * porcentajeIntereses * tiempo) / 12
        valorTotal = valorIntereses + capital
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"

    elif tiempo <= 2:
        porcentaje_de_perdida = 0.02
        valor_A_perder = capital * porcentaje_de_perdida
        valorTotal = capital - valor_A_perder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"


print(CDT("AB1012 ",100000,3))
