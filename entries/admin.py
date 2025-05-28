from django.contrib import admin
from .models import Profile, Entry

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_per_page = 10
    search_fields = ['id__startswith']
    list_filter = ['id']

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_profile']
    list_per_page = 10
    search_fields = ['id__startswith']
    list_filter = ['id']
    list_select_related = ['profile']

    def get_profile(self, Entry):
        return Entry.profile.id