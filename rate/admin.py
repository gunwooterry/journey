from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Tag, Country, Destination, UserProfile


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag_id')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.register(Tag, TagAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
