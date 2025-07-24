from django.contrib import admin

from .paginatiors import StandardResultsSetPagination

class AdminMixin(admin.ModelAdmin):
    readonly_fields = ["date_created", "created_by", "date_modified", "modified_by"]
    list_display = ['is_active']
    date_hierarchy = 'date_created'
    prepopulated_fields = {'slug': ['name']}
    list_per_page = StandardResultsSetPagination.page_size
    exclude = ['tags']