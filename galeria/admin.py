from django.contrib import admin
from galeria.models import Phothography

class ListPhotos(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    list_display_links = ("id", "name")
    list_editable = ("published",)
    search_fields = ("name",)
    list_filter = ("category",)
    list_per_page = 10

admin.site.register(Phothography, ListPhotos)
