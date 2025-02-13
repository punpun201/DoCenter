from django import forms
from gestion.models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'  

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}), 
        }