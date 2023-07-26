from django.shortcuts import redirect, render
from APP.forms import TextFileUploadForm 
import os




import os

def encriptar(request):
    # Obtener el directorio del escritorio del usuario actual
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Comprobar si se recibió una solicitud POST
    if request.method == 'POST':
        # Crear un formulario basado en la clase TextFileUploadForm
        form = TextFileUploadForm(request.POST, request.FILES)

        # Verificar si el formulario es válido
        if form.is_valid():
            # Obtener el valor del botón de acción (Encriptar o Desencriptar)
            mi_valor = request.POST.get('encriptar')

            # Verificar si el usuario seleccionó "Encriptar"
            if mi_valor == 'Encriptar':
                # Leer el archivo enviado por el usuario
                archivo = form.cleaned_data['file'].read()

                # Convertir el contenido del archivo en una cadena
                nuevo = str(archivo)

                # Eliminar los caracteres de inicio y final (posiblemente '\r\n') de la cadena
                kkk = nuevo[2:-1]

                # Encriptar el texto cambiando cada carácter por el siguiente en el código ASCII
                textoFinal = ''
                for letra in kkk:
                    ascii = ord(letra) 
                    ascii += 1
                    textoFinal += chr(ascii)

                # Guardar el texto encriptado en un nuevo archivo
                with open(desktop + '/texto encriptado.txt', 'w') as destination:
                    destination.write(textoFinal)
            else:
                # Leer el archivo enviado por el usuario
                archivo = form.cleaned_data['file'].read()

                # Convertir el contenido del archivo en una cadena
                nuevo = str(archivo)

                # Eliminar los caracteres de inicio y final (posiblemente '\r\n') de la cadena
                kkk = nuevo[2:-1]

                # Desencriptar el texto cambiando cada carácter por el anterior en el código ASCII
                textoFinal = ''
                for letra in kkk:
                    ascii = ord(letra)
                    ascii -= 1
                    textoFinal += chr(ascii)

                # Guardar el texto desencriptado en un nuevo archivo
                with open(desktop + '/texto desencriptado.txt', 'w') as destination:
                    destination.write(textoFinal)

            # Redirigir a la vista de encriptación después de procesar el formulario
            return redirect('encriptar')
    else:
        # Si no se recibió una solicitud POST, mostrar el formulario vacío
        form = TextFileUploadForm()
        return render(request, 'APP/index.html', {"form": form})

