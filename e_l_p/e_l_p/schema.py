import graphene
import graphql_jwt

import api.schema.schema_user
import api.schema.schema_course

from api.schema import (
    schema_user,
    schema_course
)

class Mutation(
    schema_user.Mutation,
    schema_course.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()


class Query(
    schema_user.Query,
    schema_course.Query,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
