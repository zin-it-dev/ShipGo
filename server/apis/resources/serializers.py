from rest_framework import serializers

from ..models import User, Category, Course, Lesson
from .mixins import SerializerMixin, TagSerializerMixin

class UserSerializer(SerializerMixin):
    class Meta:
        model = User
        fields = SerializerMixin.Meta.fields + ['username', 'email', 'password']
        

class CategorySerializer(SerializerMixin):
    class Meta:
        model = Category
        fields = SerializerMixin.Meta.fields + ['name']
        
        

class CourseSerializer(TagSerializerMixin):
    category = serializers.StringRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Course
        fields = TagSerializerMixin.Meta.fields + ['name', 'price', 'thumbnail', 'category']
        
        
class LessonSerializer(TagSerializerMixin):
    course = serializers.StringRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Lesson
        fields = TagSerializerMixin.Meta.fields + ['name', 'course']
        