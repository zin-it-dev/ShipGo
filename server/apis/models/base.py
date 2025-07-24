from django.db import models

from .mixins import AuditMixin, SlugMixin, StatusMixin
from .enums import ContentType


class Category(StatusMixin, SlugMixin, AuditMixin):
    name = models.CharField(unique=True, max_length=80)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    
class Tag(StatusMixin, SlugMixin, AuditMixin):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"#{self.name}"
    
    
class Base(StatusMixin, SlugMixin, AuditMixin):
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True
    
    
class Course(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Lesson(Base):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    content = models.TextField()
    content_type = models.CharField(
        max_length=10,
        choices=ContentType.choices,
        default=ContentType.DOCUMENT
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'course'], name='unique_lesson_course')
        ]
    
    def __str__(self):
        return self.name