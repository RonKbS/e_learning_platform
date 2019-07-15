from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import superuser_required

from .models.users import User


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    # define the data to be returned to client
    user = graphene.Field(UserType)

    class Arguments:
    # define the data to be received from the client
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, email, password):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @superuser_required
    def resolve_users(self, info, **kwargs):
        return User.objects.all()
