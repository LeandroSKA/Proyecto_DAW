from dataclasses import field
from django import forms
from .models import alumno, profesor, ciclo, asignatura

class newAlumnoForm(forms.ModelForm):

    class Meta:
        model = alumno
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(newAlumnoForm,self).__init__(*args, **kwargs)
        self.fields['ciclo'].empty_label = "Seleccion"

class newProfesorForm(forms.ModelForm):

    class Meta:
        model = profesor
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(newProfesorForm,self).__init__(*args, **kwargs)

class newCicloForm(forms.ModelForm):

    class Meta:
        model = ciclo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(newCicloForm,self).__init__(*args, **kwargs)


class newAsignaturaForm(forms.ModelForm):

    class Meta:
        model = asignatura
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(newAsignaturaForm,self).__init__(*args, **kwargs)
        self.fields['profesor'].empty_label = "Seleccion"
        self.fields['ciclo'].empty_label = "Seleccion"


