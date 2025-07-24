from .mixins import AdminMixin
from .inlines import TagCourseInline, TagLessonInline, CourseInline, LessonInline


class CategoryAdmin(AdminMixin):
    inlines = [CourseInline]
    list_display = ['name'] + AdminMixin.list_display
    
    
class CourseAdmin(AdminMixin):
    inlines = [TagCourseInline, LessonInline]
    list_display = ['name'] + AdminMixin.list_display
    
    
class LessonAdmin(AdminMixin):
    inlines = [TagLessonInline]
    list_display = ['name'] + AdminMixin.list_display
    
    
class TagAdmin(AdminMixin):
    list_display = ['name'] + AdminMixin.list_display