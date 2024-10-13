#el KARMA, ambos inician en 0 pero su valor nunca disminuye a lo largo del juego, nuestras desiciones nos acompañan todo el camino.

nivel_karma_positivo = 1 #aumenta con las decisiones positivas hasta nivel 3
#al llegar a 4, multiplica por 2||al llegar a 7 multiplica por 3||esos valores no disminuyen
valor_karma_positivo = 1 #este es el valor que cambia al subir de nivel| 1 | 2 | 3|

nivel_karma_negativo = 1 #aumenta con las decisiones negativas hasta nivel 3
#al llegar a 4, multiplica por 2||al llegar a 7 multiplica por 3||esos valores no disminuyen 
valor_karma_negativo = 1 #este es el valor que cambia al subir de nivel| 1 | 2 | 3|

#los valores positivos suman para el karma positivo, los negativos para el karma negativo
karma_desicion = 0 #este valor suma o resta a nuestro karma  depende de la desicion
desicion = 0 # puede tomar los valores 1 y -1, luego vuelve a 0 || 1 positiva || -1 negativa

karma_adquirido = 0 #cambia cada vez que se toma una desicion

karma = 0 #este es el que cambia con cada desición
# el karma total inicia en 0 también, pero a diferencia de los otros, puede tomar valores negativos. 

#luego de cada desicion se hace :
#karma += karma_adquirido




