from django.db import models
from django.utils import timezone
from django.db.models import F, FloatField, Sum

# Create your models here.
class Supplier(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	created_date = models.DateTimeField(
			auto_now_add=True)
	modified_date = models.DateTimeField(
			blank=True, null=True,auto_now=True)

	def publish(self):
		self.modified_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class Product(models.Model):
	IP = 'IPHONE'
	IPAD = 'IPAD'
	IMAC = 'IMAC'
	MACBOOK = 'MACBOOK'
	OTHER ='OTHER'
	GROUP_CHOICES = (
		(IP, 'iPhone'),
		(IPAD, 'iPad'),
		(IMAC, 'iMac'),
		(MACBOOK,'MacBook'),
		(OTHER,'Other')
	)
	name = models.CharField(max_length=50)
	group = models.CharField(max_length=50,choices=GROUP_CHOICES,default=IP) 
	description = models.CharField(max_length=50)
	created_date = models.DateTimeField(
			auto_now_add=True)

	def __str__(self):
		return self.name

	def bom_count(self):
		return self.bom_list.count()
	bom_count.short_description="Total Parts"



class Bom(models.Model):
	product = models.ForeignKey('Product',related_name='bom_list',blank=True,null=True)
	part_number = models.CharField(max_length=30) 
	description = models.CharField(max_length=50)
	created_date = models.DateTimeField(
			auto_now_add=True)

	class Meta:
		ordering = ['product']

	def __str__(self):
		return ('%s : %s' % (self.product,self.description))


class Receiving(models.Model):
	OPEN = 'OPEN'
	CLOSE = 'CLOSE'
	STATUS_CHOICES = (
		(OPEN, 'Open'),
		(CLOSE, 'Close')
	)
	po = models.CharField(max_length=50)
	supplier = models.ForeignKey('Supplier',related_name='receiving_list',blank=True,null=True) 
	trans_name = models.CharField(max_length=50,blank=True,null=True)
	trans_id = models.CharField(max_length=50,blank=True,null=True)
	trans_fee = models.IntegerField(default=0)
	description = models.CharField(max_length=200,blank=True,null=True)
	status = models.CharField(max_length=50,choices=STATUS_CHOICES,default=OPEN) 
	created_date = models.DateTimeField(
			auto_now_add=True)
	modified_date = models.DateTimeField(
			blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.po

	def item_count(self):
		return self.receiv_detail_list.count()
	item_count.short_description="Total Items"

	def item_total_price(self):
		return self.receiv_detail_list.aggregate(price_per_po=Sum(F('price')*F('qty'),output_field=FloatField())).get('price_per_po')
	item_total_price.short_description="Total Price"


class Receiving_detail(models.Model):
	bom = models.ForeignKey('Bom',related_name='receiv_bom_list',blank=True,null=True)
	receiving = models.ForeignKey('Receiving',related_name='receiv_detail_list',blank=True,null=True) 
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	qty = models.IntegerField(default=0)
	created_date = models.DateTimeField(
			auto_now_add=True)
	modified_date = models.DateTimeField(
			blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User' ,blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.bom))

	def total_price(self):
		return self.aggregate(total_price=Sum(F('price')*F('qty'),output_field=FloatField())).get('total_price')
	total_price.short_description="Total Price"


class Inventory(models.Model):
	IN = 'IN'
	SOLD = 'SOLD'
	CLIAM = 'CLIAM'
	SCRAP = 'SCRAP'
	OTHER ='OTHER'
	STATUS_CHOICES = (
		(IN, 'Inventory'),
		(SOLD, 'Sold out'),
		(CLIAM, 'Cliam'),
		(SCRAP,'Scrapped'),
		(OTHER,'Other')
	)
	bom = models.ForeignKey('Bom',related_name='inv_list',blank=True,null=True)
	receiving_detail = models.ForeignKey('Receiving_detail',related_name='receive_inv_list',blank=True,null=True)
	sn = models.CharField(max_length=200,blank=True,null=True)
	cost = models.DecimalField(max_digits=5, decimal_places=2)
	status = models.CharField(max_length=50,choices=STATUS_CHOICES,default=IN) 
	created_date = models.DateTimeField(
			auto_now_add=True)
	modified_date = models.DateTimeField(
			blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User' ,blank=True,null=True)

	def __str__(self):
		return ('OK')