import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from events.models import EventLocation


class EventLocationType(DjangoObjectType):
    class Meta:
        model = EventLocation
        filter_fields = ['name']
        fields = ("id", "name", "address ")
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    event = graphene.relay.Node.Field(EventLocationType)
    all_events = DjangoFilterConnectionField(EventLocationType)


schema = graphene.Schema(query=Query)
