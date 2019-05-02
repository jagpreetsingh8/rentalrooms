from django.contrib import admin
from owner.models import Owner, User

class RealtorAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', '')
    list_display_links =('id', 'title')
    list_filter =('owner',)
    list_editable =('parking',)
    search_fields =('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Owner)
