from django import forms
from .models import PersonalInfo, PersonalPrograms, PersonalSecurity


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class PersonalProgramForm(forms.ModelForm):
    class Meta:
        model = PersonalPrograms
        fields = '__all__'


class PersonalSecurityForm(forms.ModelForm):
    class Meta:
        model = PersonalSecurity
        fields = '__all__'