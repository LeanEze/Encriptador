from django import forms

class TextFileUploadForm(forms.Form):
    file = forms.FileField()