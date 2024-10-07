#ACTIVIDAD 2 - LOS ULTIMOS CARACTERES RIEN MEJOR
#INGRESO DE DATOS
print("📄 - - - - - BIENVENIDO  - - - - - 📄\n")
cadena = input("Porfavor, ingrese la cadena de carácteres: ")
while len(cadena) < 3:
    cadena = input("Porfavor, ingrese la cadena de carácteres con más de 3 carácteres: ")#para propositos prácticos dada la consigna

#OPERAMOS
primeros = cadena[:3] #desde el principio hasta el 3 indice sin incluirlo
ultimos = cadena[-3:] #desde el 3ero contando desde el final (-1) hasta el final
juntos = primeros+ultimos

#AHORA LA MAGIA
print(f"Los primeros 3: {primeros}\n")
print(f"Los últimos 3: {ultimos}\n")
print(f"Y por último juntos: {juntos}")
