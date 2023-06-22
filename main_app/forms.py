from django import forms
from .models import PetTable, PetImage

class PetNameForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['name']
        labels = {
            'name': 'What is your pet\'s name?',
        }


class PetActivityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['activity_level']
        labels = {
            'activity_level': 'How much does your dog like being walked?',
        }

class PetSociabilityForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['sociability']
        labels = {
            'sociability': 'How social is your pet?',
        }

class PetSizeForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['size']
        labels = {
            'size': 'What size is your pet?',
        }

class PetAgeForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['age']
        labels = {
            'age': 'How old is your pet?',
        }


class PetWeightForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['weight']
        labels = {
            'wight': 'What weight is your pet?',
        }

class PetHealthStatusForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['healthStatus']
        labels = {
            'healthStatus': 'How would you describe your pet\'s health?',
        }

class PetEnergyLevelForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['energy_level']
        labels = {
            'energy_level': 'How would you describe your pet\'s energy levels?',
        }

class PetVaccinationInformationForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['vaccinationInformation']
        labels = {
            'vaccinationInformation': 'Is your pet vaccinated?',
        }

class PetMonthlyCostForm(forms.ModelForm):
    class Meta:
        model = PetTable
        fields = ['monthlyCost']
        labels = {
            'monthlyCost': 'What do you spend on average each month on essentials for your pet? Think food, vet bills, grooming, etc. £',
        }


class PetPromptsForm(forms.ModelForm):
    url = forms.ModelMultipleChoiceField(queryset=PetImage.objects.all(), required=False)
    class Meta:
        model = PetTable
        fields = ['prompt1', 'a1', 'prompt2', 'a2', 'prompt3', 'a3', 'url']
       
class PetImageForm(forms.ModelForm):
    class Meta:
        model = PetImage
        fields = ['url']
        labels = {
            'url': 'Please upload an image of your pet',
        }