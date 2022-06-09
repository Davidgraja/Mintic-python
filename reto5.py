import pandas as pd

rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"


def listaPeliculas(rutaFileCsv:str):
    import pathlib
    
    extencion = pathlib.Path(rutaFileCsv)
    if extencion.suffix ==".csv?raw=true":
        try:
            leer_csv = pd.read_csv(rutaFileCsv)
            dt = pd.DataFrame(leer_csv.pivot_table(index=["Country","Language"],values="Gross Earnings"))
            return dt.head(10)
        except Exception :
            print("Error al leer el archivo de datos")
        
    else:
        print("Extensión inválida.")


print(listaPeliculas(rutaFileCsv))



# def listaPeliculas(rutaFileCsv:str) -> str : 

    
#     if rutaFileCsv.split(".")[-1] =="csv?raw=true":
#         try:
#             leer_csv = pd.read_csv(rutaFileCsv)
#             dt = leer_csv[["Country","Language","Gross Earnings"]]
#             ganacias =dt.pivot_table(index=["Country","Language"])
#             return ganacias.head(10)
#         except:
#             print("Error al leer el archivo de datos.")
        
#     else:
#         print("Extensión inválida.")

#     return


