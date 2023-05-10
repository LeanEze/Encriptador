from django import forms




class RenombrarArchivoInput(forms.ClearableFileInput):
    def get_context(self, name, value, attrs):
        attrs['name'] = 'mi_nuevo_nombre'
        return super().get_context(name, value, attrs)
    
    
class TextFileUploadForm(forms.Form):
    file = forms.FileField(widget=RenombrarArchivoInput())