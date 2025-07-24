from django.contrib import admin

from .sec import UserAdmin
from .base import CategoryAdmin, CourseAdmin, LessonAdmin, TagAdmin
from ..models import Category, User, Course, Lesson, Tag

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag, TagAdmin)