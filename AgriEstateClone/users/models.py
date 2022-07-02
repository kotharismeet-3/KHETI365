from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from PIL import Image
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email Requierd!")
        if not username:
            raise ValueError("Username required!")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    userid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #
    USERNAME_FIELD = 'email'
    #
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=85)
    last_name = models.CharField(max_length=85)
    recovery_email = models.EmailField(blank=True)
    img = models.ImageField(default='avatar.png', upload_to='media')

    def __str__(self):
        return self.user.username

    # https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.img.path)

        if(image.height > 300 or image.width > 300):
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.img.path)
