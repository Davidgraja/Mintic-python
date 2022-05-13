def cliente(id_cliente,nombre,edad,primer_ingreso):
    informacion_cliente = dict(nombre=nombre, edad=edad, atraccion="", apto="",primer_ingreso = primer_ingreso, total_boleta =""  )
    
    descuentoXtreme_sillas = 0.05
    descuentoCarrochocones = 0.07
    # informacionfinal = []
    """validacion"""


    if informacion_cliente.get("edad") > 18 and informacion_cliente.get("primer_ingreso") ==True : 
        atraccion = "X-Treme"
        valorBoleta = 20000
        descuento = valorBoleta * descuentoXtreme_sillas   
        valorTotal = valorBoleta - descuento
        
        informacion_cliente["atraccion"]= atraccion
        informacion_cliente["apto"]= True
        informacion_cliente["total_boleta"] = valorTotal
        # informacionfinal = informacion_cliente
    # return informacionfinal    
    
    
    
    
                
cliente(1 ,"Johana Fernandez" , 20 , True)