#admin12345
from django.contrib import admin
from .models import Product
from .models import Bom
from .models import Supplier
from .models import Receiving
from .models import Receiving_detail

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Bom)
admin.site.register(Supplier)
#admin.site.register(Receiving)
#admin.site.register(Receiving_detail)


class BomInline(admin.TabularInline):
    model = Bom
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']
    list_display = ('name','description')
    fieldsets = [
        (None,               {'fields': ['name','description']}),
    ]
    inlines = [BomInline]

admin.site.register(Product,ProductAdmin)




def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class ReceivDetailsInline(admin.TabularInline):
    model = Receiving_detail
    extra = 1
    exclude =['user']

class ReceivingAdmin(admin.ModelAdmin):
    search_fields = ['po','supplier']
    list_filter = ['supplier','transporter']
    list_display = ('po','supplier','transporter')
    fieldsets = [
        (None,               {'fields': ['po','supplier','transporter']}),
    ]
    inlines = [ReceivDetailsInline]
    actions=[make_published]
    #date_hierarchy = 'created_date'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Receiving,ReceivingAdmin)