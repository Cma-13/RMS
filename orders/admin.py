from django.contrib import admin
from .models import Table, Category, MenuItem


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_reserved']
    # list_filter = ('is_reserved',
    # search_fields = ('name',)
    

admin.site.register(Category)
admin.site.register(MenuItem)
