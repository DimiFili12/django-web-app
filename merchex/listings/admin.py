from django.contrib import admin
from .models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)
    
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type', 'band')
    list_filter = ('sold', 'type')
    search_fields = ('title', 'description')
    ordering = ('-year',)

admin.site.register(Listing, ListingAdmin)