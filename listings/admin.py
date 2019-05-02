from django.contrib import admin
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'price', 'parking', 'list_date', 'owner')
    list_display_links =('id', 'title')
    list_filter =('owner',)
    list_editable =('parking',)
    search_fields =('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)