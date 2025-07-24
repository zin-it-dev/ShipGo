from django.db import models
from django.conf import settings
from django.utils import timezone


class AuditMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created_by',
        editable=False
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_modified_by'
    )
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.date_modified = timezone.now()
        
        if 'user' in kwargs:
            user = kwargs.pop('user')
            if not self.pk:
                self.created_by = user
            self.modified_by = user
        
        super().save(**kwargs)
        
        
class SlugMixin(models.Model):
    slug = models.SlugField(default='', null=False, blank=True)

    class Meta:
        abstract = True
        
        
class StatusMixin(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Active')
    
    class Meta:
        abstract = True
        
        