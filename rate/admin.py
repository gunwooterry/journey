from django.contrib import admin
from .models import Tag, Country, Destination


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'tag_id')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

admin.site.register(Tag, TagAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Destination, DestinationAdmin)
