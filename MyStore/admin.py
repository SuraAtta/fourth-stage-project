from django.contrib import admin
from MyStore.models import Category ,Color,Product,ProductImage,ColorLogo


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(ColorLogo)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    def get_colors(self, obj):
        return ", ".join([c.name for c in obj.colors.all()])

    get_colors.__name__ = "الالوان"

    inlines = [ProductImageAdmin]
    list_display = ["name", "category", "price","stock", "is_available", "show_hide", "created", "updated"]
    list_editable = ["is_available", "show_hide"]
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)

