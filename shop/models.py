from django.db import models
from django.utils import timezone

# Create your models here.
class Supplier(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=50)
	email = models.CharField(max_length=200)
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



class Bom(models.Model):
	product = models.ForeignKey('Product',related_name='bom_list',blank=True,null=True)
	part_number = models.CharField(max_length=30) 
	description = models.CharField(max_length=50)
	created_date = models.DateTimeField(
			auto_now_add=True)

	def __str__(self):
		return self.part_number


class Receiving(models.Model):
	po = models.CharField(max_length=50)
	supplier = models.ForeignKey('Supplier',related_name='receiving_list',blank=True,null=True) 
	transporter = models.CharField(max_length=50)
	transport_fee = models.IntegerField(default=0)
	description = models.CharField(max_length=200)
	created_date = models.DateTimeField(
			auto_now_add=True)
	modified_date = models.DateTimeField(
			blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.po


class Receiving_detail(models.Model):
	part_number = models.ForeignKey('Bom',related_name='receiv_bom_list',blank=True,null=True)
	po_number = models.ForeignKey('Receiving',related_name='receiv_detail_list',blank=True,null=True) 
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	qty = models.IntegerField(default=0)
	created_date = models.DateTimeField(
			auto_now_add=True)
	modified_date = models.DateTimeField(
			blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User' ,blank=True,null=True)

	def __str__(self):
		return self.description


