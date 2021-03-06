from django import forms
# from django.core.exceptions import NON_FIELD_ERRORS
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password

from .models import Registration, AdmissionProcess
from apps.student.models import Inscription


EMPTY_ITEM_ERROR = "Ce champ est obligatoire."

class RegistrationForm(forms.ModelForm):
    GENDERS =(
        ('homme', 'Homme'),
        ('femme', 'Femme')
        )
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.RadioSelect())

    class Meta:
        model = Registration
        fields = '__all__'
        labels = {
            'first_name': 'Prenom',
            'last_name': 'Nom',
            'gender': 'Genre',
            'date_of_birth': 'Date de Naissance',
            'nationality': 'Nationalié',
            'fathers_name': 'Nom du père',
            'mothers_name': 'Nom de la mère',
            'address': 'Adresse',
            'phone_number': 'Numéro de Téléphone',
            'email': 'Email',
            'birth_certificate_number': "Numéro Carte d'identité",
            'guardian_name': 'Nom du tuteur',
            'guardian_phone': 'Numero de téléphone du tuteur',
            'guardian_email': 'Email du tuteur',
            'guardian_address': 'Adresse du tuteur',
            'school_origin': "Ecole d'origine",
            'image': 'Choisir une image'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-element' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-element' }),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control form-element',
                                            'id':'datepicker'}),
            'nationality': forms.Select(attrs={'class': 'form-control form-element'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'birth_certificate_number': forms.TextInput(
                                                    attrs={'class': 'form-control form-element'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_email': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'guardian_address': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'school_origin': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'image': forms.FileInput(attrs={"accept":".jpg, .jpeg, .png"}),
            'active_year': forms.TextInput(attrs={'class': 'form-control form-element',
                                            'readonly':'readonly'}),
            'class_level': forms.Select(attrs={'class': 'form-control form-element'}),
        }

        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }


class AdmissionProcessForm(forms.ModelForm):
    CHOICES =(
        ('approuvé', 'Approuvé'),
        ('rejeté', 'Rejeté'))
    commitee_decision = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = AdmissionProcess
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'pass_bac': "Not are not unique.",
        #     }
        # }
        fields = '__all__'
        exclude = ['user']
        labels = {
            'registree_number': 'Numero de saisie',
            'registree_name': 'Personne saisie',
            'pass_admission_test': 'Note requise au test d\'admission obtenu',
            'pass_medical_test': 'A passé son examen medical',
            'commitee_decision': 'Decision du comité d\'admission',
            'comment': 'Ajouter un commentaire',
            }
        widgets = {
            'registree': forms.TextInput(), # attrs={'class':'hide'}),
            'registree_number': forms.TextInput(attrs={'class': 'form-control form-element', 
                                                'readonly':'readonly'}),
            'registree_name': forms.TextInput(attrs={'class': 'form-control form-element', 
                                              'readonly':'readonly'}),
            'pass_bac': forms.CheckboxInput(attrs={'class':'checkbox-input bac-checkbox',
                                    "oninvalid":"this.setCustomValidity('Ce champest obligatoire')", 
                                    "oninput":"setCustomValidity('')"}),
            'pass_admission_test': forms.CheckboxInput(attrs={ 'class':'checkbox-input',
                                    "oninvalid":"this.setCustomValidity('Ce champ est obligatoire')", 
                                    "oninput":"setCustomValidity('')"}),
            'pass_medical_test': forms.CheckboxInput(attrs={'class':'checkbox-input',
                                    "oninvalid":"this.setCustomValidity('Ce champ est obligatoire')", 
                                    "oninput":"setCustomValidity('')"}),
            # 'commitee_decision': forms.RadioSelect(),
            'comment':forms.Textarea(attrs={'class': 'form-control admis-process-comment', 
                                    'required':False})
            # 'approved_by_commitee': forms.CheckboxInput(attrs={'required':True, 
            #     'class':'checkbox-input',
            #             "oninvalid":"this.setCustomValidity('Ce champ est obligatoire')", 
            #             "oninput":"setCustomValidity('')"}),
            # 'admission_denied': forms.CheckboxInput(attrs={'class':'checkbox-input'}),
            }


class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields ='__all__'
        exclude = ['user']
        widgets = {}
        