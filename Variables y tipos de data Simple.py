
#Regla basicas
#Los nombres de las variables solo pueden contener letras, números y guiones bajos

#Pueden comenzar con una letra o un guión bajo, pero no con un número
#paises_1 pero no a 1_paises.
paises_1=0 #formato correcto
1_paises=0 #si vemos aparece con una cruz


#No se permiten espacios en los nombres de las variables.
variable a=0 # tampoco se permiten espacios en las variables

#Evite el uso de palabras clave de Python y nombres de funciones como nombres de variables
print=0


#nombres de las variables
#capitales_paises es mejor que c_p 
#largo_nombre  es mejor que largo_del_nombre_de_las_personas

#tener cuidado con la i latina minuscula y la O mayuscula


print("Python es un lenguaje de programación.") #cremillas
print('Python es un lenguaje de programación.') #apostrofe
print("Python es un lenguaje de 'programación'.")#cremillas y apostrofes


#metodos basicos
nombre='martin'
print(nombre)
print(nombre.upper())

nombre='MaRtIn'
print(nombre.lower())

nombre='martin'
print(nombre.capitalize())


nombre='martin'
apellido='kostner'
nombre_completo=f'{nombre}{apellido}' #la f corresponde a format para completar la string con las variables correspondientes.

print('%s %s tiene que realizar los quehaceres del hogar'%(nombre,apellido))
     
      
print('Youtube')
print('\tYoutube')

print('lista de tareas:/n sacar a pasear a mi perro/n ir de compras/n andar en bicicleta')
#vemos que algo ocurrio

print('lista de tareas:\n sacar a pasear a mi perro\n ir de compras\n andar en bicicleta')

#combinación de ambos
print('lista de tareas:\n\t sacar a pasear a mi perro\n\t ir de compras\n\t andar en bicicleta')


nombre='Martin '
#Metodo 
print(nombre.rstrip()) 

nombre=' Martin'
#Metodo 
print(nombre.lstrip()) 

nombre=nombre.lstrip()
print(nombre)
