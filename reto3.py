prueba = (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020')
# prueba = ()
def AutoPartes(ventas:list):    
    if ventas == ():
        return "No hay registro de venta de ese producto"    
    else:
        diccionario={
            "idProducto" : ventas[0],
            "dProducto" : ventas[1],
            "pnProducto" : ventas[2],
            "cvProducto" : ventas[3],
            "sProducto" : ventas[4],
            "nComprador" : ventas[5],
            "cComprador" : ventas[6],
            "fVenta" : ventas[7]        
        }
            
        return f"Producto consultado : {diccionario['idProducto']} Descipcrión {diccionario['dProducto']} #Parte {diccionario['pnProducto']} Cantidad vendida {diccionario['cvProducto']}  Stock {diccionario['sProducto']} Comprador {diccionario['nComprador']} Documento {diccionario['cComprador']} Fecha Venta {diccionario['fVenta']}"
        
        
        


print(AutoPartes(prueba))