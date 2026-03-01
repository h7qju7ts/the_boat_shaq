from django.contrib import admin
from .models import Boat, Brand, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = (
        "name", "brand", "category", "price",
        "year", "length_ft", "is_available", "is_featured", "created_at"
    )    
    list_filter = ("is_available", "is_featured", "category", "brand", "year")
    search_fields = ("name", "short_description", "description")
    autocomplete_fields = ("brand", "category")
    prepopulated_fields = {"slug": ("name",)} 
    