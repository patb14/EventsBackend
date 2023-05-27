from django import forms

from events.models import GENDER_CHOICES, YOB_CHOICE, POSITION_CHOICES, LOP_CHOICES, Event


class RegisterForm(forms.Form):
    camp_selection = forms.ModelChoiceField(queryset=Event.objects.all())
    player_name = forms.CharField()
    player_gender = forms.ChoiceField(choices=GENDER_CHOICES)
    player_year_of_birth = forms.ChoiceField(choices=YOB_CHOICE)
    level_of_play = forms.ChoiceField(choices=LOP_CHOICES)
    position = forms.ChoiceField(choices=POSITION_CHOICES)

    def add_to_cart(self):
        print("ADDED TO CART!")
