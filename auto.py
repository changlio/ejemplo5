import subprocess
import random 
#import sys
     
cmd1 = "programa.c"
cmd2 = "funciones.c" 

print ("Este es el escript de python\n") 
#subprocess.run(["gcc",cmd,"-o","sumador1"]) #For Compiling 
subprocess.run(["gcc",cmd1, cmd2,"-o","sumador1"]) 

comando1=[2,2,14,16,20]
comando2=[2,4,random.randint(1,5),16]
print(comando2)


#for valor1 in comando1:
for i, valor1 in enumerate(comando1, start=1):
  print('el valor1 es:', i)
  #print('el valor1 es:', valor1) 
  for valor2 in comando2:
	  try:
	    #resultado=subprocess.run(["./a.out", "16","3"])
	   resultado=subprocess.run(["./sumador1", str(valor1),str(valor2)],check=True) #es check aqui o lo de la siguientelinea   
	   #resultado.check_returncode()
	  except subprocess.CalledProcessError as e:
	   print("Codigo de error =", e.returncode)
	   print(e.output)




