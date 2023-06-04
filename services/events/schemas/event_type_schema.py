import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from events.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['name', 'location']
        fields = ("id", "name", "start_date", "end_date", "location", "gender", "sessions", "cost")
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    event = graphene.relay.Node.Field(EventType)
    all_events = DjangoFilterConnectionField(EventType)


schema = graphene.Schema(query=Query)
