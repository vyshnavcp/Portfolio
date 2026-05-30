from django.contrib import admin
from .models import Category,Portfolio,Banner
from django.utils.html import format_html
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'start_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'client_name')
    list_filter = ('start_date',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_preview')
    readonly_fields = ('banner_preview',)

    def banner_preview(self, obj):
        if obj.image_one:
            return format_html(
                '<img src="{}" width="300" style="border-radius:5px;" />',
                obj.image_one.url
            )
        return "No Image"

    banner_preview.short_description = "Banner Preview"