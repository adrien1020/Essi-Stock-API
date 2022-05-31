from django.contrib import admin
from .models import CategoriteLevelTwo, Item, CategoriteLevelOne, Categorite


class CategoriteAdmin(admin.ModelAdmin):
    list_display = ['get_categorite_name']

    def get_categorite_name(self, obj):
        return obj.name
    get_categorite_name.short_description = 'name'


class CategoriteLevelOneAdmin(admin.ModelAdmin):
    list_display = ['get_categorites_name']

    def get_categorites_name(self, obj):
        return obj.name
    get_categorites_name.short_description = 'name'


class CategoriteLevelTwoAdmin(admin.ModelAdmin):
    list_display = ['get_categorites_name']

    def get_categorites_name(self, obj):
        return obj.name

    get_categorites_name.short_description = 'name'


class ItemAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_level_1', 'get_level_2', 'marque', 'reference', 'price']

    def get_name(self, obj):
        return obj.categorite.name
    get_name.short_description = 'categorites'

    def get_level_1(self, obj):
        return obj.categorite_level_1.name
    get_level_1.short_description = 'categorites level One'

    def get_level_2(self, obj):
        return obj.categorite_level_2.name
    get_level_2.short_description = 'categorites level two'


admin.site.register(CategoriteLevelOne, CategoriteLevelOneAdmin)
admin.site.register(CategoriteLevelTwo, CategoriteLevelTwoAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Categorite, CategoriteAdmin)
