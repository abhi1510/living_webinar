from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.template.loader import render_to_string

from web.utils import email_sender, token_manager

USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('author', 'Author'),
    ('watcher', 'Watcher')
)

USER_STATUS_CHOICES = (
    ('unverified', 'Unverified'),
    ('active', 'Active'),
    ('locked', 'Locked'),
    ('inactive', 'Inactive')
)


class Account(models.Model):
    organization_name = models.CharField(max_length=200, unique=True)
    street_address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    zip = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=256)
    last_modified_by = models.CharField(max_length=256)

    def __str__(self):
        return self.organization_name


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    status = models.CharField(max_length=15, choices=USER_STATUS_CHOICES)
    image_file = models.ImageField(null=True, blank=True, upload_to='profile_pics')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='users')
    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='custom_user_created_by')
    last_modified_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='custom_user_modified_by')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=CustomUser)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    # TODO:
    # If user is admin create an account for him/her
    # If user is author attach that with the creator's account
    # If user is watcher don't attach it to any account

    if created:
        if instance.type == 'admin':
            account = Account(organisation_name=instance.email,
                              created_by=instance.email, last_modified_by=instance.email)
            account.save()
            instance.account = account
            instance.save()
        token = token_manager.encode_data({
            'id': instance.id
        })
        subject = 'Thank you for registering with us'
        msg_html = render_to_string('emails/verify-email.html', {
            'email': instance.email,
            'verify_url': '{}/accounts/verify-email/{}'.format(settings.HOST, token)
        })
        email_sender.send_email(subject, msg_html, instance.email)
