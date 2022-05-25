lista = [28,36,43,52,61,75,84,97]
usuario = int(input("ingrese un numero --->"))
mensaje = ""
for i in lista:
   suma = i + usuario

   if suma == 100:
      mensaje ="cumple"
  
  
if mensaje =="cumple":
   print("cumple con la condicion")  
else :
   print("No se cumple con la condicion")  
   