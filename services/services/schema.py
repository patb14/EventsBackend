import graphene
from graphene_django import DjangoObjectType

from events.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("id", "name", "start_date", "end_date", "location", "gender", "times", "cost")


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)

    def resolve_all_events(root, info):
        return Event.objects.all()


schema = graphene.Schema(query=Query)
