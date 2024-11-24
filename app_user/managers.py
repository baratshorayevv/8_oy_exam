from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError


class UserModelManager(UserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """Oddiy foydalanuvchi yaratish"""
        if not email:
            raise ValidationError("Email kiritish majburiy")
        if not first_name:
            raise ValidationError("First name kiritish majburiy")
        if not last_name:
            raise ValidationError("Last name kiritish majburiy")

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        """Superuser yaratish"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)


class CustomerManager(UserModelManager):
    """Customer ma'lumotlarini boshqaruvchi manager"""
    def get_queryset(self):
        return super().get_queryset().filter(is_customer=True)


class AdminManager(UserModelManager):
    """Admin ma'lumotlarini boshqaruvchi manager"""
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)
