import graphene
from graphene_django import DjangoObjectType

from .models import *


# create graph type for each table
class CountriesType(DjangoObjectType) :
    class Meta:
        model = Countries

class DepartmentsType(DjangoObjectType) :
    class Meta:
        model = Departments

class EmployeesType(DjangoObjectType) :
    class Meta:
        model = Employees

class EmployeesType(DjangoObjectType) :
    class Meta:
        model = Employees

class JobHistoryType(DjangoObjectType) :
    class Meta:
        model = JobHistory
        
class JobsType(DjangoObjectType) :
    class Meta:
        model = Jobs


class LocationsType(DjangoObjectType) :
    class Meta:
        model = Locations


class RegionsType(DjangoObjectType) :
    class Meta:
        model = Regions


# Class for graph Query

class Query(graphene.ObjectType):
    
    countries   = graphene.List(CountriesType)
    departments = graphene.List(DepartmentsType)
    employees = graphene.List(EmployeesType)
    jobHistory  = graphene.List(JobHistoryType)
    jobs        = graphene.List(JobsType)
    locations   = graphene.List(LocationsType)
    regions     = graphene.List(RegionsType)

    #create graph resolvers

    # countries resolver
    def resolve_countries(self, info, **kwargs):
        return Countries.objects.all()
    # departments resolver
    def resolve_departments(self, info, **kwargs):
        return Departments.objects.all()
    # employees resolver
    def resolve_employees(self, info, **kwargs):
        return Employees.objects.all()
    # jobHistory resolver
    def resolve_jobHistory(self, info, **kwargs):
        return JobHistory.objects.all()
    # jobs resolvers
    def resolve_jobs(self, info, **kwargs):
        return Jobs.objects.all()
    # location resolvers
    def resolve_locations(self, info, **kwargs):
        return Locations.objects.all()
    # regions resolvers
    def resolve_regions(self, info, **kwargs):
        return Regions.objects.all()