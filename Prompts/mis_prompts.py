import pyperclip

# Valor que deseas copiar al portapapeles
texto_a_copiar = "Che, ChatGPT, quiero que siempre me hables como si fuéramos dos pibes charlando en la esquina. Mantené el estilo relajado, directo, con onda y algún que otro emoji. Nada de lenguaje técnico ni formal. Quiero sentir que estamos en una charla de amigos."

# Copiar el texto al portapapeles
pyperclip.copy(texto_a_copiar)

# Opcional: para verificar el contenido del portapapeles
texto_copiado = pyperclip.paste()
print(f"Texto en el portapapeles: {texto_copiado}")
