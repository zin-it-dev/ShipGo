from rest_framework import serializers

from ..models import Tag

class SerializerMixin(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'slug', 'is_active']
        
        
class TagSerializer(SerializerMixin):
    class Meta:
        model = Tag
        fields = SerializerMixin.Meta.fields + ['name']

        
class TagSerializerMixin(SerializerMixin):
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        fields = SerializerMixin.Meta.fields + ['tags']

import abc
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

class ElasticSearchViewSet(viewsets.GenericViewSet):
    serializer_class = None
    document_class = None
    pagination_class = PageNumberPagination

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """Override method: return a Q() expression."""

    @action(detail=False, methods=['get'], url_path=r'search/(?P<query>[^/]+)', url_name='search')
    def search(self, request, query=None):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: \"{query}\"')
            
            results = [hit.to_dict() for hit in response.hits]
            page = self.paginator.paginate_queryset(results, request, view=self)
            
            if page is not None:
                return self.paginator.get_paginated_response(page)

            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
