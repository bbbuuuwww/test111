from django.contrib import admin
from myxitiya.models import Item, Spider
# Register your models here.

class ItemLine(admin.StackedInline):
    model = Spider
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    list_per_page = 10  # 限制每页显示的数量
    list_filter = ["type"] # 右侧显示的过滤器
    list_display = ["id", "type", "name"] # 查询结果显示的字段
    search_fields = ["name"] # 用于搜索
    inlines = [ItemLine]

admin.site.register(Item, ItemAdmin)
admin.site.register(Spider)