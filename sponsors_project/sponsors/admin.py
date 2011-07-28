from django.contrib import admin

from sponsors.models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pub_date')
    fields = ['name', 'slug', 'pub_date']
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    search_fields = ['name']

admin.site.register(Sponsor, SponsorAdmin)
