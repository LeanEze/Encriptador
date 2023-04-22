def encriptar(texto):
    print('el texto a encriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal


def desencriptar(texto):
    print('el texto a desencriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo,'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('el arachivo se encripto correctamente')

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo,'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('el arachivo se desencripto correctamente')

respuestaEoD = input('presione "E" para encriptar, o "Q" para desencriptar: ')
rutaArchivo = input('ingrese ruta del archivo: ')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)