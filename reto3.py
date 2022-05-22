
prueba = ([
 (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]),



def AutoPartes(ventas):

    diccionario = {}

    for x in range(len(prueba[0])):
        registros=dict(idProducto=prueba[0][x][0], dProducto =prueba[0][x][1] , pnProducto=prueba[0][x][2],cvProducto=prueba[0][x][3], sProducto=prueba[0][x][4],nComprador=prueba[0][x][5], cComprador=prueba[0][x][6], fVenta=prueba[0][x][7] )
        diccionario[x]=registros


    return diccionario
# AutoPartes(prueba)


def consultaRegistro(ventas, idproducto):
    registro = AutoPartes(ventas)    
    
    for i in range(len(registro)):
        print(registro[i].values())    
        
        # if idproducto ==registro[i].get("idProducto"):
        # #    print(registro[i].get("idProducto"))
        #     print(f'Producto consultado :{registro[i].get("idProducto")}  Descipcrión {registro[i].get("dProducto")} #Parte {registro[i].get("pnProducto")} Cantidad vendida {registro[i].get("cvProducto")} Stock {registro[i].get("sProducto")} Comprador {registro[i].get("nComprador")} Documento {registro[i].get("cComprador")} Fecha Venta {registro[i].get("fVenta")}')
           
     
             
    # print(encontradoÇ )  
consultaRegistro(prueba,2564)




  # print(f"Producto consultado : {diccionario['idProducto']} Descipcrión {diccionario['dProducto']} #Parte {diccionario['pnProducto']} Cantidad vendida {diccionario['cvProducto']}  Stock {diccionario['sProducto']} Comprador {diccionario['nComprador']} Documento {diccionario['cComprador']} Fecha Venta {diccionario['fVenta']}")
        













# diccionario= {}

# for x in range(len(prueba[0])):
#     registros=dict(IdProducto=prueba[0][x][0], dProducto =prueba[0][x][1] , pnProducto=prueba[0][x][2],cvProducto=prueba[0][x][3], sProducto=prueba[0][x][4],nComprador=prueba[0][x][5], cComprador=prueba[0][x][6], fVenta=prueba[0][x][7] )
  
    
#     diccionario[x] = registros   
    
    
# # print(diccionario)
#     # for i in range(len(prueba[0]))
    
#     # for y in range(len(prueba[0][x])):
#     #     print(prueba[0][x][y])      

# # for i in range(len(registros)):
# #      print(i)
    
        
#     diccionario= {}

#     for x in range(len(ventas[0])):
#        diccionario[x]= registros=dict(idProducto=ventas[0][x][0], dProducto =ventas[0][x][1] , pnProducto=ventas[0][x][2],cvProducto=ventas[0][x][3], sProducto=ventas[0][x][4],nComprador=ventas[0][x][5], cComprador=ventas[0][x][6], fVenta=ventas[0][x][7] )
    
#     return diccionario

# print(AutoPartes(prueba))



