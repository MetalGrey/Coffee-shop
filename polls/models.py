from django.db import models

class Assortment(models.Model):
    
    COFFEE = 'COFFEE'
    TOOLS = 'TOOLS'
    OTHER = 'OTHER'
    PRODUCT_CHOICES = [
        (COFFEE, 'Coffee'),
        (TOOLS, 'Tools'),
        (OTHER, 'Other'),
    ]

    assortment_name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PRODUCT_CHOICES, default=COFFEE)
    assortment_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.assortment_name

class News(models.Model):
    adress = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adress

class Order(models.Model):
    email = models.EmailField(unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    fast_delivery = models.BooleanField(default=False)

    def total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())
    
    def __str__(self):
        return f"Order {self.id} by {self.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.assortment} x {self.quantity} (Order {self.order.id})"