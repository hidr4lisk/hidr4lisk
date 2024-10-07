proyectos = ["página web", "aplicación web", "app personal"]
print(f"Mis proyectos: \n{proyectos}")
tipo_proyectos = (type(proyectos))
cantidad_proyectos = (len(proyectos))
elemento = proyectos.index("aplicación web")
print(elemento)

amigo = input("Arriba las manos, dame tu mejor idea: ")
proyectos += [amigo]
print(proyectos)
