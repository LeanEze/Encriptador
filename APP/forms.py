from django import forms




# Crear una subclase de ClearableFileInput para personalizar el widget de carga de archivos
class RenombrarArchivoInput(forms.ClearableFileInput):
    def get_context(self, name, value, attrs):
        # Cambiar el atributo 'name' del widget para que sea 'mi_nuevo_nombre'
        attrs['name'] = 'mi_nuevo_nombre'
        return super().get_context(name, value, attrs)

# Crear un formulario para cargar archivos de texto
class TextFileUploadForm(forms.Form):
    # Agregar un campo FileField al formulario y usar el widget personalizado RenombrarArchivoInput
    file = forms.FileField(widget=RenombrarArchivoInput())
