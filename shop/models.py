from django.db import models
from django.utils import timezone

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
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
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	created_date = models.DateTimeField(
            auto_now_add=True)

	def __str__(self):
		return self.name



class Bom(models.Model):
	product = models.ForeignKey('Product')
	part_number = models.CharField(max_length=30) #4,4S,5S
	description = models.CharField(max_length=50)
	created_date = models.DateTimeField(
            auto_now_add=True)

	def __str__(self):
		return self.part_number


class Receiving(models.Model):
	po = models.CharField(max_length=50)
	supplier = models.ForeignKey('Supplier') #models.ForeignKey('auth.User')
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
	part_number = models.ForeignKey('Bom')
	po_number = models.ForeignKey('Receiving') #models.ForeignKey('auth.User')
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
