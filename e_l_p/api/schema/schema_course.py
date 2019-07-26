from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import (
    staff_member_required, login_required
)

from api.models.users import User
from api.models.courses import (
    Course, CourseContent, CourseRating, CurriculumPackage
)

# to create curriculum packages,
# create a curriculum_package object
# then create courses and add the foregn_key to the packages

class CurriculumPackageType(DjangoObjectType):
    class Meta:
        model = CurriculumPackage


class CreateCurriculumPackage(graphene.Mutation):
    curriculum = graphene.Field(CurriculumPackageType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()

    @staff_member_required
    def mutate(self, info, name, description):
        user = info.context.user
        curriculum = CurriculumPackage(
            name=name,
            description=description,
            user=user
        )
        curriculum.save()

        return CreateCurriculumPackage(curriculum=curriculum)


class Mutation(graphene.ObjectType):
    create_curriculum_package = CreateCurriculumPackage.Field()


class Query(graphene.ObjectType):
    curriculum_packages = graphene.List(CurriculumPackageType)

    @login_required
    def resolve_curriculum_packages(self, info, **kwargs):
        return CurriculumPackage.objects.all()
