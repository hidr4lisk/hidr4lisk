# Crear un conjunto en Python que posea los siguientes elementos: 
#   rojo, blanco, azul.
# Posteriormente, agrega a nuestro set de colores, los valores: 
#   violeta y dorado
# Elimina los colores: 
#   celeste, blanco y dorado

conjunto = {"rojo","blanco","azul"}
print(conjunto)
conjunto.add("violeta")
conjunto.add("dorado")
print(conjunto)
conjunto.discard("celeste")
conjunto.discard("blanco")
conjunto.discard("dorado")
print(conjunto)