from django import forms

from .animals import ANIMALS
from .colours import COLOURS

class TestForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput, min_length=8)
    colour = forms.ChoiceField(required=True, choices=COLOURS.CHOICES)
    animal = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=ANIMALS.CHOICES)
    type_of_tiger = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(TestForm, self).clean()
        animal = cleaned_data.get('animal')
        type_of_tiger = cleaned_data.get("type_of_tiger")

        if 'tiger' in animal and type_of_tiger == '':
            self.add_error('type_of_tiger', "Animal Tiger is selected; type of tiger must not be empty.")
