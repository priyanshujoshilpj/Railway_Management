from django import forms  
from .models import User 


class UserForm(forms.ModelForm):
    class Meta:

        usrType = (
            ('True', True),
            ('False', False)
        )
        coachTypes = (
            ('1st AC', '1st AC'),
            ('2nd AC', '2nd AC'),
            ('3rd AC', '3rd AC'),
            ('Sleeper', 'sleeper')
        )

        model = User
        fields = ("id","name","email","contact","gender","usrStatus",'age','date_of_journey', 'seat', 'coach', 'birthmark', 'usrImg')
        widgets = {
        'id':forms.HiddenInput(),
        'name': forms.TextInput(),
        'email': forms.EmailInput(),
        'contact': forms.NumberInput(),
        'usrStatus': forms.RadioSelect(choices=usrType),
        'age': forms.NumberInput(),
        'date_of_journey': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','required':True}),
        'coach': forms.CheckboxSelectMultiple(choices=coachTypes),
        'birthmark': forms.Textarea(attrs={'rows': 5, 'cols': 30}),
        'usrImg': forms.FileInput(),
        }