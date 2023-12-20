from django import forms
from .models import Add_task


class AddtaskForm(forms.ModelForm):
    class Meta:
        model = Add_task
        fields = '__all__'

        class DateInput(forms.DateInput):
            input_type = 'date'

        widgets= {
            'task': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Tasks'}),
            'priority': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Priority'}),
            'date': DateInput(attrs={'class':'form-control'}),
        }

        labels = {
            'task': '',
            'priority': '',
            'date':''
        }

        