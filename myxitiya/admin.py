from django.contrib import admin
from myxitiya.models import Item, Spider
# Register your models here.

class ItemLine(admin.StackedInline):
    model = Spider
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = ["type"]
    list_display = ["id", "type", "name"]
    search_fields = ["name"]
    inlines = [ItemLine]

admin.site.register(Item, ItemAdmin)
admin.site.register(Spider)