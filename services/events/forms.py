from django import forms

from events.models import EventTime
from events.models.event_model import Event
from events.models.gender_model import Gender
from events.models.level_of_play_model import LevelOfPlay
from events.models.player_position_model import PlayerPosition

YOB_CHOICE = [
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
]


class RegisterForm(forms.Form):
    camp_selection = forms.ModelChoiceField(queryset=Event.objects.all())
    time_slot = forms.ModelChoiceField(queryset=EventTime.objects.none())
    player_name = forms.CharField()
    player_gender = forms.ModelChoiceField(queryset=Gender.objects.all().exclude(gender="Co-ed"))
    player_year_of_birth = forms.ChoiceField(choices=YOB_CHOICE)
    level_of_play = forms.ModelChoiceField(queryset=LevelOfPlay.objects.order_by("id"))
    position = forms.ModelChoiceField(queryset=PlayerPosition.objects.all())