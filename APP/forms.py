from django import forms

class TextFileUploadForm(forms.Form):
    file = forms.FileField()

class TextFileUploadForm2(forms.Form):
    file = forms.FileField()