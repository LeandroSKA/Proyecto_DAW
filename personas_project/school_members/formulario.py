from dataclasses import field
from django import forms
from .models import alumno

class newPeopleForm(forms.ModelForm):

    class Meta:
        model = alumno
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(newPeopleForm,self).__init__(*args, **kwargs)
        self.fields['ciclo'].empty_label = "Seleccion"