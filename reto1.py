def CDT(usuario , capital , tiempo):
    if tiempo > 2:

        #calculo de los intereses ganados:
        porcentajeIntereses = 0.03
        valorIntereses = (capital * porcentajeIntereses * tiempo) / 12
        valorTotal = valorIntereses + capital
        print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {int(valorTotal)}")

    elif tiempo <= 2:
        #calculo de la perdida de interses:
        porcentaje_de_perdida = 0.02
        valor_A_perder = capital * porcentaje_de_perdida
        valorTotal = capital - valor_A_perder
        print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {int(valorTotal)}")

calculoCdt("AB1012",1000000,3)
