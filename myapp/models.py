from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name= models.CharField(max_length=100, blank=True)
    last_name= models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=100 , blank=True )
    stripe_session_id = models.CharField(null= True, blank=True , max_length=100)
    is_paid = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.email
    
class ImageUploadCloudinary(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')  

    def __str__(self):
        return self.title
