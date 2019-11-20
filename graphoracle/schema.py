import graphene

import hr.schema

class Query(hr.schema.Query,graphene.ObjectType):
    pass

schema=graphene.Schema(query=Query)