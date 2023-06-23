from django.shortcuts import redirect, render
from APP.forms import TextFileUploadForm 
import os




def encriptar(request):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    if request.method == 'POST':
        form = TextFileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            mi_valor = request.POST.get('encriptar')
            if mi_valor == 'Encriptar':
                print(mi_valor)
                archivo = form.cleaned_data['file'].read()
                nuevo = str(archivo)
                kkk =nuevo[2:-1]
                textoFinal = ''
                for letra in kkk:
                    ascii = ord(letra) 
                    ascii += 1
                    textoFinal += chr(ascii)
                with open(desktop + '/texto encriptado.txt', 'w') as destination:
                        destination.write(textoFinal)
            else:
                archivo = form.cleaned_data['file'].read()
                nuevo = str(archivo)
                kkk =nuevo[2:-1]
                textoFinal = ''
                for letra in kkk:
                    ascii = ord(letra)
                    ascii -= 1
                    textoFinal += chr(ascii)
                print(nuevo[2:-1])
                with open(desktop + '/texto desencriptado.txt', 'w') as destination:
                        destination.write(textoFinal)

                    
            return redirect('encriptar')
    else:
        form = TextFileUploadForm()
        return render(request, 'APP/index.html',{"form": form})
        
