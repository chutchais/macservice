#admin12345
from django.contrib import admin
from .models import Product
from .models import Bom
from .models import Supplier
from .models import Receiving
from .models import Receiving_detail
from .models import Inventory

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Bom)

#admin.site.register(Receiving)
#admin.site.register(Receiving_detail)


class SupplierAdmin(admin.ModelAdmin):
	search_fields = ['name','phone_number']
	list_filter = ['name']
	list_display = ('name','description','phone_number','address','email')
	fieldsets = [
		(None,               {'fields': ['name','description','phone_number','address','email']}),
	]
	#inlines = [BomInline]

admin.site.register(Supplier,SupplierAdmin)


class BomInline(admin.TabularInline):
	model = Bom
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	search_fields = ['name','group']
	list_filter = ['name','group']
	list_display = ('name','group','description','bom_count')
	fieldsets = [
		(None,               {'fields': ['name','group','description']}),
	]
	inlines = [BomInline]

admin.site.register(Product,ProductAdmin)




def make_published(modeladmin, request, queryset):
	queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


def move_to_inventory(self, request, queryset):
	for obj in queryset:
		
		for item in obj.receiv_detail_list.all():
			pn=item.bom
			po=item.receiving
			price=item.price
			qty=item.qty
			for i in range(0,qty):
				inv = Inventory(bom=pn,receiving_detail=item,cost=price)
				inv.save()
		obj.status='CLOSE'
		# obj.actived=True
		obj.save()
		# for i in range(1,13) :
		#     lp,created = LockerPort.objects.get_or_create(lockerid = obj, portid = i)
	self.message_user(request, "%s successfully move items to inventory." % obj.po )
move_to_inventory.short_description = "Move data to inventory"

class ReceivDetailsInline(admin.TabularInline):
	model = Receiving_detail
	extra = 1
	exclude =['user']

class ReceivingAdmin(admin.ModelAdmin):
	search_fields = ['po','supplier']
	list_filter = ['status','supplier','trans_name']
	list_display = ('po','supplier','trans_name','trans_id','trans_fee','description','item_count','item_total_price','status')
	fieldsets = [
		(None,               {'fields': ['po','supplier','trans_name','trans_id','trans_fee','description','status']}),
	]
	inlines = [ReceivDetailsInline]
	actions=[move_to_inventory]
	#date_hierarchy = 'created_date'

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

admin.site.register(Receiving,ReceivingAdmin)




class InventoryAdmin(admin.ModelAdmin):
	search_fields = ['sn']
	list_filter = ['status','bom']
	list_display = ('bom','receiving_detail','sn','cost','status')
	fieldsets = [
		(None,               {'fields': ['bom','receiving_detail','sn','cost','status']}),
	]
	#inlines = [ReceivDetailsInline]
	#actions=[make_published]
	#date_hierarchy = 'created_date'

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

admin.site.register(Inventory,InventoryAdmin)