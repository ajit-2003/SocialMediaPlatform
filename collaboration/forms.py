from django import forms
from .models import Document, Group

# forms.py
class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'content']

class DocumentEditForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['content']
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']