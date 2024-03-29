from django.contrib import admin
from .models import Realtor


# Register your models here.

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'hire_date', 'is_mvp')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_editable = ('is_mvp',)
    list_per_page = 25
# admin.site.register(Realtor)
