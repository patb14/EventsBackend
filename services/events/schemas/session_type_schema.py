import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from events.models import Session


class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        filter_fields = ["name", "start_time", "end_time"]
        fields = ("id", "name", "start_time", "end_time")
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    session = graphene.relay.Node.Field(SessionType)
    all_sessions = DjangoFilterConnectionField(SessionType)


schema = graphene.Schema(query=Query)
