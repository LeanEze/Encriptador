from django.shortcuts import redirect, render
from APP.forms import TextFileUploadForm ,TextFileUploadForm2

# Create your views here.


def encriptar(request):
    if request.method == 'POST':
        form = TextFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            archivo = form.cleaned_data['file'].read()
            nuevo = str(archivo)
            kkk =nuevo[2:-1]
            textoFinal = ''
            for letra in kkk:
                ascii = ord(letra)
                ascii += 1
                textoFinal += chr(ascii)
            print(nuevo[2:-1])
            with open('C:/Users/Rodrigo/Desktop/ejercicios/miprueba.txt', 'w') as destination:
                    destination.write(textoFinal)
                    
            return render(request, 'APP/index.html')
    else:
        form = TextFileUploadForm()
        return render(request, 'APP/index.html',{"form": form})
        


def desencriptamiento(request):
    if request.method == 'POST':
        form2 = TextFileUploadForm2(request.POST, request.FILES)
        if form2.is_valid():
            uploaded_file = request.FILES['file']
            archivo = form2.cleaned_data['file'].read()
            nuevo = str(archivo)
            kkk =nuevo[2:-1]
            textoFinal = ''
            for letra in kkk:
                ascii = ord(letra)
                ascii -= 1
                textoFinal += chr(ascii)
            print(nuevo[2:-1])
            with open('C:/Users/Rodrigo/Desktop/ejercicios/miprueba.txt', 'w') as destination:
                    destination.write(textoFinal)

            return redirect(request, 'APP/index.html',{"form2": form2})
    else:
        form2 = TextFileUploadForm2()
        return render(request, 'APP/index.html',{"form2": form2})


#     def desencriptar(texto):
#         print('el texto a desencriptar es: ' + texto)
#         textoFinal = ''
#         for letra in texto:
#             ascii = ord(letra)
#             ascii -= 1
#             textoFinal += chr(ascii)
#         return textoFinal


#     def desencriptarArchivo(rutaArchivo):
#         archivo = open(rutaArchivo, 'r')
#         texto = archivo.read()
#         archivo.close()
#         textoDesencriptado = desencriptar(texto)

#         archivo = open(rutaArchivo,'w')
#         archivo.write(textoDesencriptado)
#         archivo.close()
#         print('el arachivo se desencripto correctamente')

#     if respuestaEoD == 'E' or respuestaEoD == 'e':
#         encriptarArchivo(rutaArchivo)
#     else:
#         desencriptarArchivo(rutaArchivo)




def encriptador(request):
    return render(request, 'APP/index.html')