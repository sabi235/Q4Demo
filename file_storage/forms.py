# forms.py

from django import forms

class MyForm(forms.Form):
    uploaded_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Select a file')
