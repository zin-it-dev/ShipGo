from django.db import models

class Role(models.TextChoices):
    ADMIN = 'admin', 'Administrator'
    STUDENT = 'student', 'Student'
    INSTRUCTOR = 'Instructor', 'Instructor'
    

class ContentType(models.TextChoices):
    DOCUMENT = 'DOC', 'Document'
    VIDEO = 'VID', 'Video'
    QUIZ = 'QUIZ', 'Quiz'