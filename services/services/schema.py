import graphene
from graphene_django import DjangoObjectType

from events.models import Event, Session, Gender, EventLocation

# TODO: STARTING HERE: https://docs.graphene-python.org/projects/django/en/latest/tutorial-relay/#schema

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("id", "name", "start_date", "end_date", "location", "gender", "sessions", "cost")


class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        fields = ("id", "name", "start_time", "end_time")


class GenderType(DjangoObjectType):
    class Meta:
        model = Gender
        fields = ("id", "gender")


class EventLocationType(DjangoObjectType):
    class Meta:
        model = EventLocation
        fields = ("id", "name", "address ")


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)

    def resolve_all_events(root, info):
        return Event.objects.all()


schema = graphene.Schema(query=Query)
