from django.contrib import admin
from .models import Profile, Entry

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_per_page = 10
    search_fields = ['id']
    list_filter = ['id']

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_profile']
    list_per_page = 10
    search_fields = ['title__istartswith']
    list_filter = ['user']
    list_select_related = ['user']

    def get_profile(self, Entry):
        return Entry.profile.id