from django.shortcuts import render
from APP.forms import TextFileUploadForm

# Create your views here.


def miEncriptador(request):
    if request.method == 'POST':
        form = TextFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Aquí puedes realizar las operaciones necesarias con el archivo
            # Para obtener el contenido del archivo, puedes hacer:
            archivo = form.cleaned_data['file'].read()
            # print('el texto a encriptar es: ' + archivo)
            textoFinal = ''
            for letra in archivo:
                ascii = ord(letra)
                ascii += 1
                textoFinal += chr(ascii)

            # Luego puedes procesar el contenido según tus necesidades

    else:
        form = TextFileUploadForm()

    return render(request, 'APP/index.html', {"form":form})


    def desencriptar(texto):
        print('el texto a desencriptar es: ' + texto)
        textoFinal = ''
        for letra in texto:
            ascii = ord(letra)
            ascii -= 1
            textoFinal += chr(ascii)
        return textoFinal


    def desencriptarArchivo(rutaArchivo):
        archivo = open(rutaArchivo, 'r')
        texto = archivo.read()
        archivo.close()
        textoDesencriptado = desencriptar(texto)

        archivo = open(rutaArchivo,'w')
        archivo.write(textoDesencriptado)
        archivo.close()
        print('el arachivo se desencripto correctamente')

    if respuestaEoD == 'E' or respuestaEoD == 'e':
        encriptarArchivo(rutaArchivo)
    else:
        desencriptarArchivo(rutaArchivo)




def encriptador(request):
    return render(request, 'APP/index.html')