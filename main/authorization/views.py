from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from .forms import PersonalInfoForm, PersonalProgramForm, PersonalSecurityForm
from django.urls import reverse


# Главная страница регистрации #
def index(request):
    data = {
        'title': 'Главная страница',
        }
    return render(request, 'authorization/reg_1.html', data)


FORMS = [('first', PersonalSecurityForm),
         ('second', PersonalInfoForm),
         ('third', PersonalProgramForm),]

TEMPLATES = {'first': 'authorization/reg_1.html',
             'second': 'authorization/reg_2.html',
             'third': 'authorization/reg_3.html',}


class MultiStepFormSubmission(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, 'users/account_student.html', {'data': form_data})
