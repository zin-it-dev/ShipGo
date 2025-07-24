from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from elasticsearch_dsl import Q

from .repositories import UserRepository, CategoryRepository, CourseRepository, LessonRepository
from .serializers import UserSerializer, CategorySerializer, CourseSerializer, LessonSerializer
from .paginatiors import StandardResultsSetPagination
from .filters import CourseFilter
from .mixins import ElasticSearchViewSet
from ..documents import CourseDocument


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = UserRepository().get_all()
    serializer_class = UserSerializer
    
    
class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = CategoryRepository().get_all()
    serializer_class = CategorySerializer
    
    
class CourseViewSet(ElasticSearchViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = CourseRepository().get_all()
    serializer_class = CourseSerializer
    document_class = CourseDocument
    pagination_class = StandardResultsSetPagination
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter
    
    def generate_q_expression(self, query):
        return Q("multi_match", query=query, fields=['name^3', 'description'])

    
class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LessonRepository().get_all()
    serializer_class = LessonSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'slug'
    
    def list(self, request, course_slug=None):
        queryset = self.get_queryset().filter(course__slug=course_slug)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, slug=None, course_slug=None):
        queryset = self.get_queryset().filter(slug=slug, course__slug=course_slug)
        lesson = get_object_or_404(queryset, slug=slug) 
        serializer = self.get_serializer(lesson)
        return Response(serializer.data)