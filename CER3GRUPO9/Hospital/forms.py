from django import forms
from .models import AvanceDiario, Bebe

class AvancesForm(forms.ModelForm):
    class Meta:
        model = AvanceDiario
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget()
        }