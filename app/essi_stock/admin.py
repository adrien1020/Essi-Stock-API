from django.contrib import admin
from .models import CategoriteLevelTwo, Item, CategoriteLevelOne, Categorite


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['get_categorites_name']

    def get_categorites_name(self, obj):
        return obj.name
    get_categorites_name.short_description = 'name'


class ItemAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_level_1', 'get_level_2', 'marque', 'reference', 'price']

    def get_name(self, obj):
        return obj.category.name
    get_name.short_description = 'category Name'

    def get_level_1(self, obj):
        return obj.category_level_1.name
    get_level_1.short_description = 'category L1'

    def get_level_2(self, obj):
        return obj.category_level_2.name
    get_level_2.short_description = 'category L2'


admin.site.register(CategoriteLevelOne)
admin.site.register(CategoriteLevelTwo)
admin.site.register(Item, ItemAdmin)
admin.site.register(Categorite, CategoryAdmin)
