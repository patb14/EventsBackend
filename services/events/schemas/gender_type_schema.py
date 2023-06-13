import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from events.models import Gender


class GenderType(DjangoObjectType):
    class Meta:
        model = Gender
        filter_fields = ["gender"]
        fields = ("id", "gender")
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    gender = graphene.relay.Node.Field(GenderType)
    all_genders = DjangoFilterConnectionField(GenderType)


schema = graphene.Schema(query=Query)
