from django.contrib import admin

from .models import Listing

# Register your models here.

@admin.register(Listing)
class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'realtor', 'title', 'price', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'state', 'city', 'price', 'zipcode')
    list_per_page = 25
# admin.site.register(Listing)
