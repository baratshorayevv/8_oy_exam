from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from app_user.managers import UserModelManager, CustomerManager, AdminManager


class UserModel(AbstractUser):
    # Kerakli maydonlar
    username = models.CharField(max_length=100, null=True, blank=True)  # Username ixtiyoriy
    email = models.EmailField(max_length=150, unique=True)  # Email majburiy va unikal
    first_name = models.CharField(max_length=150)  # Ism
    last_name = models.CharField(max_length=150)  # Familiya
    image = models.ImageField(upload_to='Admin/image', blank=True, null=True)  # Rasm

    # Qo'shimcha bayroqlar
    is_customer = models.BooleanField(default=False)  # Customer uchun flag
    is_admin = models.BooleanField(default=False)  # Admin uchun flag

    # Foydalanuvchini email orqali autentifikatsiya qilish
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Guruhlar va ruxsatnomalar
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True
    )

    # Manager
    objects = UserModelManager()

    @property
    def full_name(self):
        """To‘liq ism-familiyani qaytaradi"""
        return f"{self.last_name}, {self.first_name}"

    def __str__(self):
        return self.full_name


class Admin(UserModel):
    """Admin proksi modeli"""
    objects = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_customer = False
        self.is_admin = True
        self.is_staff = True
        self.is_superuser = True  # Admin superuser bo‘lishi kerak
        super().save(*args, **kwargs)


class Customer(UserModel):
    """Customer proksi modeli"""
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_customer = True
        self.is_admin = False
        self.is_staff = False
        self.is_superuser = False
        super().save(*args, **kwargs)
