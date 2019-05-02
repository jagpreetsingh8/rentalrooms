from django.contrib import admin
from owner.models import Owner, User

class OwnerAdmin(admin.ModelAdmin):
    list_display =('id', 'first_name')
    list_display_links =('id', 'first_name')
    search_fields =('name',)
    list_per_page = 25

admin.site.register(Owner, OwnerAdmin)
