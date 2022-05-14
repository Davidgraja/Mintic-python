def cliente(id_cliente,nombre,edad,primer_ingreso):
    informacion_cliente= dict(id_cliente= id_cliente, nombre= nombre,edad=edad,primer_ingreso=primer_ingreso)
      
    descuentoXtreme_sillas = 0.05
    descuentoCarrochocones = 0.07    
    informacion_final = dict(nombre = informacion_cliente["nombre"],edad=informacion_cliente["edad"],atraccion="",apto= "", primer_ingreso=informacion_cliente["primer_ingreso"], total_boleta="" )
    
    """validacion"""

    #> de 18 años:
    if informacion_cliente.get("edad") > 18 and informacion_cliente.get("primer_ingreso") ==True : 
        atraccion = "X-Treme"
        valorBoleta = 20000
        descuento = valorBoleta * descuentoXtreme_sillas   
        valorTotal = valorBoleta - descuento
        
        informacion_final["atraccion"]= atraccion
        informacion_final["apto"]= True
        informacion_final["total_boleta"] = valorTotal
    
    elif informacion_cliente.get("edad") > 18 and informacion_cliente.get("primer_ingreso") == False:
        atraccion = "X-Treme"
        valorBoleta = 20000
        informacion_final["atraccion"]= atraccion
        informacion_final["apto"]= True
        informacion_final["total_boleta"] = valorBoleta
        
    # >= 15 y <= 18 :
    elif informacion_cliente.get("edad") >= 15 and informacion_cliente.get("primer_ingreso") == True:
        atraccion = "Carros chocones"
        valorBoleta = 5000
        descuento = valorBoleta * descuentoCarrochocones   
        valorTotal = valorBoleta - descuento
        
        informacion_final["atraccion"]  = atraccion
        informacion_final["apto"]=True
        informacion_final["total_boleta"]=valorTotal
        
    elif  informacion_cliente.get("edad") >= 15 and informacion_cliente.get("primer_ingreso") == False:
        atraccion = "Carros chocones"
        valorBoleta = 5000
        informacion_final["atraccion"]  = atraccion
        informacion_final["apto"]=True
        informacion_final["total_boleta"]=valorBoleta 
    
    elif informacion_cliente.get("edad") >= 7  and informacion_cliente.get("primer_ingreso") == True:
        atraccion = "Sillas voladoras"
        valorBoleta = 10000
        descuento = valorBoleta * descuentoXtreme_sillas  
        valorTotal = valorBoleta - descuento
        
        informacion_final["atraccion"]  = atraccion
        informacion_final["apto"]=True
        informacion_final["total_boleta"]=valorTotal 
        
    elif informacion_cliente.get("edad") >= 7  and informacion_cliente.get("primer_ingreso") == False:
        atraccion = "Sillas voladoras"
        valorBoleta = 10000
        descuento = valorBoleta * descuentoXtreme_sillas  
        valorTotal = valorBoleta - descuento
        
        informacion_final["atraccion"]  = atraccion
        informacion_final["apto"]=True
        informacion_final["total_boleta"]=valorBoleta 
        
        
    else:
        informacion_final["apto"] = False
        informacion_final["atraccion"]  = "N/A"
        informacion_final["total_boleta"] ="N/A"
        
        
    return informacion_final
    
    
                
print(cliente(4 ,"Tatiana Ruiz" ,18,False ))

