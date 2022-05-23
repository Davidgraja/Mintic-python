
# prueba = ([
#  (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
#  (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
#  (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
#  (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]),

prueba2 = ([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]),

prueba3 = ([
 (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
 (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
 (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
 (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]),


def AutoPartes(ventas):

    diccionario = {}

    for x in range(len(ventas[0])):
        registros=dict(idProducto=ventas[0][x][0], dProducto =ventas[0][x][1] , pnProducto=ventas[0][x][2],cvProducto=ventas[0][x][3], sProducto=ventas[0][x][4],nComprador=ventas[0][x][5], cComprador=ventas[0][x][6], fVenta=ventas[0][x][7] )
        diccionario[x]=registros


    return diccionario

# print(AutoPartes(prueba2))


def consultaRegistro(ventas, idproducto):

    registro = AutoPartes(ventas) 
    encontrado=0 ;
    for y in range(len(registro)):
        if idproducto ==registro[y].get("idProducto"):
            encontrado = registro[y].get("idProducto")
      
    if idproducto == encontrado:
        # print("hay elementos encontrados")
        for i in range(len(registro)):
            # print(registro[i].values())    
            if idproducto ==registro[i].get("idProducto"):
                # print(registro[i].get("idProducto"))
                print(f'Producto consultado : {registro[i].get("idProducto")}  Descipcrión {registro[i].get("dProducto")} #Parte {registro[i].get("pnProducto")} Cantidad vendida {registro[i].get("cvProducto")} Stock {registro[i].get("sProducto")} Comprador {registro[i].get("nComprador")} Documento {registro[i].get("cComprador")} Fecha Venta {registro[i].get("fVenta")}')
    else:
        print("No hay registro de venta de ese producto")
                
           
     
             
consultaRegistro(prueba3,2010)




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



