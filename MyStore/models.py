import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from PIL import Image

# Create your models here.

"""
Product
    - id
    - name
    - banner
    - description
    - category (fk)
    - colors (fk)
    - price
    - stock
    - is available (bool) (if false, puts out of stock label)
    - show/hide (bool) 
    - created (date)
    - updated (date)
    - images (fk)
    
###################
Category
    - id
    - name
    
###################
ProductImage
    - product
    - image
    
###################
Colors
    - id
    - name
    -color-code
    


"""
User = get_user_model()

            
class Category(models.Model):
    name = models.CharField("اسم الفئة", max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فئة'
        verbose_name_plural = 'الفئات'
        
class Product(models.Model):
    name = models.CharField("اسم المنتج", max_length=50)
    banner = models.ImageField("الصورة", upload_to="banners/")
    description = models.TextField("الوصف", blank=True)
    category = models.ForeignKey(Category, verbose_name="الفئة", on_delete=models.CASCADE)
    colors = models.ManyToManyField('MyStore.Color', verbose_name='الالوان', related_name='products')
    price = models.IntegerField("السعر")
    stock = models.IntegerField("عدد القطع بالمخزن")
    is_available = models.BooleanField("متوفر؟", default=True)
    show_hide = models.BooleanField("اظهر هذا المنتج", default=True)
    created = models.DateTimeField("تاريخ الانشاء", editable=False, auto_now_add=True)
    updated = models.DateTimeField("تاريخ التحديث", editable=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated']
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.banner.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.banner.path)
            

            
class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField("صورة", upload_to='images/')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'صورة منتج'
        verbose_name_plural = 'صور المنتج'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
       
            
class Color(models.Model):
    name = models.CharField("اسم اللون", max_length=50)
    color_code = models.CharField("رمز اللون (HEX)", max_length=12, help_text="ادخل اللون مثل: OxFF45B9EE")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'لون'
        verbose_name_plural = 'الالوان'

    @property
    def modify_color_code(self):
        self.color_code = self.color_code.lstrip('#')
        self.color_code = f"0xFF{self.color_code.upper()}"
        return self.color_code

class Item(models.Model):
    user = models.ForeignKey(to=User, verbose_name='user', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_ordered = models.BooleanField('is ordered', default=False)

    def __str__(self):
        return f''

class Cart(models.Model):
    user = models.ForeignKey(to=User, verbose_name='user', related_name='carts', on_delete=models.CASCADE)
    items = models.ManyToManyField('MyStore.Item', verbose_name='items', related_name='carts')
    is_ordered = models.BooleanField('is ordered', default=False)
    total = models.IntegerField('total', blank=True, null=True)

    def __str__(self):
        return f"{self.user.name}: د.ع {self.total}"

    class Meta:
        verbose_name = 'عربة'
        verbose_name_plural = 'العربات'

    @property
    def cart_total(self):
        return sum(i.product.price * i.quantity for i in self.items.all())
    
class Wishlist(models.Model):
    user = models.ForeignKey(to=User, verbose_name='user', related_name='favs', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product', related_name='favs', on_delete=models.CASCADE)
    is_fav = models.BooleanField('is favorite', default=False)
