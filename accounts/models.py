from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not phone:
            raise ValueError(_("The Phone must be set"))
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_confirm = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.phone}"

    class Meta:
        db_table = "account"
        verbose_name = "Account"


class EmailVerifcationCodes(models.Model):
    email = models.EmailField(max_length=254)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = "EmailVerificationCodes"

    def __str__(self) -> str:
        return str(self.code)


status = [
    ("info", "info"),
    ("warning", "warning"),
]