from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from src.employees.models import Employee, Department

admin.site.register(
    Department,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'name',
    ),
    list_display_links=(
        'name',
    ),
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = (
        ('department', TreeRelatedFieldListFilter),
    )
