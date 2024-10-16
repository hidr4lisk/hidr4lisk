campeones_del_mundo = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "España",
    2014: "Alemania",
    2018: "Francia",
    2022: "Argentina", 
}

#Deberás crear un diccionario llamado campeones_del_mundo que almacene a los ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2022. Mostrarlo por pantalla. 

print(campeones_del_mundo)

#Luego muestra el ganador del mundial 2006. 

print(f"el Campeón del año 2006 es: {campeones_del_mundo[2006]}")

#Finalmente, agrega un posible ganador del mundial 2026 al diccionario, y muéstralo.

campeones_del_mundo[2026] = "Argentina"
print(campeones_del_mundo)