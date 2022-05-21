


prueba = ([
 (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]),

# diccionario= {}

# for x in range(len(prueba[0])):
#     registros=dict(IdProducto=prueba[0][x][0], dProducto =prueba[0][x][1] , pnProducto=prueba[0][x][2],cvProducto=prueba[0][x][3], sProducto=prueba[0][x][4],nComprador=prueba[0][x][5], cComprador=prueba[0][x][6], fVenta=prueba[0][x][7] )
  
    
#     diccionario[x] = registros   
    
    
# print(diccionario)
    
    
    
    
    
    
    
    
    
    # for i in range(len(prueba[0]))
    
    # for y in range(len(prueba[0][x])):
    #     print(prueba[0][x][y])      

# for i in range(len(registros)):
#      print(i)
    
        
def AutoPartes(ventas):
    diccionario= {}

    for x in range(len(ventas[0])):
        registros=dict(IdProducto=ventas[0][x][0], dProducto =ventas[0][x][1] , pnProducto=ventas[0][x][2],cvProducto=ventas[0][x][3], sProducto=ventas[0][x][4],nComprador=ventas[0][x][5], cComprador=ventas[0][x][6], fVenta=ventas[0][x][7] )
  
        diccionario[x]=registros
    
    return diccionario        



print(AutoPartes(prueba))