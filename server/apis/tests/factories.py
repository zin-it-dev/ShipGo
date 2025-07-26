import factory
from factory.faker import Faker

from ..models import Category, Course, Lesson


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker('word')
    
    
class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name = Faker('sentence', nb_words=3)
    category = factory.SubFactory(CategoryFactory)
    price = Faker('random_int', min=100, max=1000)
    
    
class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson

    course = factory.SubFactory(CourseFactory)
    name = Faker('sentence', nb_words=4)
    content = Faker('paragraph', nb_sentences=3)
