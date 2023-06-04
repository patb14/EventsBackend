import graphene

from events.schemas import event_type_schema
from events.schemas.all_schema_types import EVENTS_SCHEMA_TYPES


class Query(event_type_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,
                         types=EVENTS_SCHEMA_TYPES)
