from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from news.models import News
from academics.models import OnlineTutorialTips, AcademicSlides, PastQuestions
from django.utils import timezone

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        last_name,
        index_number,
        graduation_year,
        phone,
        password,
        **extra_fields,
    ):
        """
        Create and save a user with the given email and password.
        """
        if not phone:
            raise ValueError(_("The Phone must be set"))
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            index_number=index_number,
            phone=phone,
            graduation_year=graduation_year,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, index_number, graduation_year, phone, password, **extra_fields
    ):
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
        return self.create_user(
            phone=phone,
            index_number=index_number,
            password=password,
            graduation_year=graduation_year,
            **extra_fields,
        )


class CustomUser(AbstractUser):
    username = None
    email = None
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    phone = PhoneNumberField(unique=True)
    index_number = models.CharField(_("index number"), unique=True, max_length=255)
    """
    dont take user level which becomes complicated since it has
    to be incraesed every year for each user which will affect the system perfomance
    """
    # current year subtracted from graduation_year will give you the user level
    graduation_year = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_confirm = models.BooleanField(default=False)

    USERNAME_FIELD = "index_number"

    REQUIRED_FIELDS = ["first_name", "last_name", "graduation_year", "phone"]

    objects = CustomUserManager()

    def get_level(self):
        try:
            # levels should be in hundreds
            diff = int(self.graduation_year) - int(timezone.now().year)
            level = (4 - diff) * 100
            return f"{level}"
        except Exception:
            return "level unavailable, please check your graduation_year"

    def __str__(self) -> str:
        return f"{self.phone}"

    class Meta:
        db_table = "account"
        verbose_name = "Account"


class PhoneVerifcationCodes(models.Model):
    phone = PhoneNumberField(unique=True, null=True, blank=False)
    code = models.CharField(max_length=10, null=True, blank=False)
    expires_in = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = "PhoneVerificationCodes"

    def save(self, *args, **kwargs) -> None:
        self.expires_in = timezone.now() + timezone.timedelta(minutes=10)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.code)


class UserSavedBlogs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blogs = models.ManyToManyField(to=News)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_saved_blogs"


class UserSavedSlides(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slides = models.ManyToManyField(to=AcademicSlides)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_saved_slides"


class UserSavedOnlineTutorialTips(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    online_tips = models.ManyToManyField(to=OnlineTutorialTips)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_saved_online_tutorial_tips"


class UserSavedPastQueations(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    past_questions = models.ManyToManyField(to=PastQuestions)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_saved_past_questions"
