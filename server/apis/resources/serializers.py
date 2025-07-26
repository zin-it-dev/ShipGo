from rest_framework import serializers

from ..models import User, Category, Course, Lesson
from .mixins import SerializerMixin, TagSerializerMixin


class UserSerializer(SerializerMixin):
    class Meta:
        model = User
        fields = SerializerMixin.Meta.fields + ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['role']
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

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
        