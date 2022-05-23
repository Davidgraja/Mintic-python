
def AutoPartes(ventas):

    diccionario = {}
    for x in range(len(ventas)):
        registros = dict(idProducto=ventas[x][0],dProducto =ventas[x][1],pnProducto=ventas[x][2],cvProducto=ventas[x][3],sProducto=ventas[x][4],nComprador=ventas[x][5], cComprador=ventas[x][6], fVenta=ventas[x][7] )
        
        diccionario[x]=registros


    return diccionario



def consultaRegistro(ventas, idproducto):
   
    registro = ventas
    encontrado=0 ;
    for y in range(len(registro)):
        if idproducto ==registro[y].get("idProducto"):
            encontrado = registro[y].get("idProducto")
      
    if idproducto == encontrado:
        for i in range(len(registro)):
            if idproducto ==registro[i].get("idProducto"):
                print("Producto consultado :",registro[i].get("idProducto")," Descripción ",registro[i].get("dProducto")," #Parte ",registro[i].get("pnProducto")," Cantidad vendida ",registro[i].get("cvProducto")," Stock ",registro[i].get("sProducto")," Comprador",registro[i].get("nComprador")," Documento ",registro[i].get("cComprador")," Fecha Venta ",registro[i].get("fVenta"))
                
    else:
        print("No hay registro de venta de ese producto")
                
           
# codigos externos que pueden ser utiles

# for x in range(len(prueba[0])):
#     registros=dict(IdProducto=prueba[0][x][0], dProducto =prueba[0][x][1] , pnProducto=prueba[0][x][2],cvProducto=prueba[0][x][3], sProducto=prueba[0][x][4],nComprador=prueba[0][x][5], cComprador=prueba[0][x][6], fVenta=prueba[0][x][7] )
      
      
#     # for i in range(len(prueba[0]))
    
#     # for y in range(len(prueba[0][x])):
#     #     print(prueba[0][x][y])      

# # for i in range(len(registros)):
# #      print(i)
    
#     for x in range(len(ventas[0])):
#        diccionario[x]= registros=dict(idProducto=ventas[0][x][0], dProducto =ventas[0][x][1] , pnProducto=ventas[0][x][2],cvProducto=ventas[0][x][3], sProducto=ventas[0][x][4],nComprador=ventas[0][x][5], cComprador=ventas[0][x][6], fVenta=ventas[0][x][7] )
    
