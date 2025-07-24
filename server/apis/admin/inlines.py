from django.contrib import admin

from ..models import Course, Lesson


class TagCourseInline(admin.TabularInline):
    model = Course.tags.through
    extra = 3
    verbose_name = 'Tag'
    
    
class TagLessonInline(admin.TabularInline):
    model = Lesson.tags.through
    extra = 3
    verbose_name = 'Tag'
    
    
class CourseInline(admin.StackedInline):
    model = Course
    extra = 2
    
    
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 4