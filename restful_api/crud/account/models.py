from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User

# Create your models here.

#Custom User Manager
class UserManager(BaseUserManager):
    def create(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email,name, tc and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  name, tc, password=None):
        """
        Creates and saves a superuser with the given email,name, tc and password.
        """
        user = self.create(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user model
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email",max_length=255,unique=True,  )
    name = models.CharField(max_length=200)
    tc =models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
     


# class Item(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField()

#     def __str__(self):
#         return self.name
    

CATEGORY_CHOICES =(
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.TextField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')
    
    def __str__(self):
     return str(self.id)
   