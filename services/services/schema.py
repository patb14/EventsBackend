import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from events.models import Event, Session, Gender, EventLocation


# TODO: We probably want a custom object type. Just so theres default exclude fields like timestamps, etc

class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['name', 'location']
        fields = ("id", "name", "start_date", "end_date", "location", "gender", "sessions", "cost")
        interfaces = (graphene.relay.Node,)


class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        filter_fields = ['name']
        fields = ("id", "name", "start_time", "end_time")
        interfaces = (graphene.relay.Node,)


class GenderType(DjangoObjectType):
    class Meta:
        model = Gender
        filter_fields = ['gender']
        fields = ("id", "gender")
        interfaces = (graphene.relay.Node,)


class EventLocationType(DjangoObjectType):
    class Meta:
        model = EventLocation
        filter_fields = ['name']
        fields = ("id", "name", "address ")
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    event = graphene.relay.Node.Field(EventType)
    all_events = DjangoFilterConnectionField(EventType)


schema = graphene.Schema(query=Query)
