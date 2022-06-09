from django.contrib import admin

from .models import Category, Wallet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass
