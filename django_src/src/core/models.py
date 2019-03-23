"""
This is core database models file of GoodVUD Web solutions
"""

from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.conf import settings

UPLOAD_DIRECTORY_PROFILEPHOTO = 'images_profilephoto'
UPLOAD_DIRECTORY_SERVICE_MAIN_IMAGE = 'images_service_main_image'
UPLOAD_DIRECTORY_WEB_CATEGORY_MAIN_IMAGE = 'images_web_category_main_image'

class User(AbstractBaseUser, PermissionsMixin):
    """
    User that have access to use the website services.
    """
    GENDER = [
        ('MALE', "MALE"),
        ('FEMALE', "FEMALE"),
        ('TRANSGENDER', "TRANSGENDER"),
        ('PREFER_NOT_TO_SAY', "PREFER_NOT_TO_SAY")
    ]

    upload_directory = 'user_images'

    identifier = models.CharField(max_length=255, null=True, blank=True, unique=True, )


class Services(models.Model):
    """
    This model describes all the services that will be offered by the company. This model have maximum relationship with other models in the database.
    """
    identifier = models.CharField(max_length=255, null=True, blank=True, unique=True, help_text="This is the unique service identifier that will be used in the URL that will be used to point to the service page later on.")
    service_name = models.CharField(max_length=255, null=True, blank=True, help_text="This is the service name offered by the goodvud web solutions.")
    service_base_image = models.ImageField(max_length=255, null=True, blank=True, help_text="This is the base image of the service that will be displayed on all the layouts.")
    service_gallery_images = models.ImageField(max_length=255, null=True, blank=True, help_text="This is the main gallery images of the service that will be displayed in the form of carousel.")
    service_about = models.CharField(max_length=1000, null=True, blank=True, help_text="This contains all the details about the service.")
    service_pricing_start = models.CharField(max_length=25, null=True, blank=True, help_text="This is the starting price rate of the service.")

class WebsiteCategories(models.Model):
    category_name = models.CharField(max_length=255, null=True, blank=True, help_text="This is the website category name.")
    category_content_websites_number = models.CharField(max_length=255, null=True, blank=True, help_text="This is the number of websites falling in this category. This may be zero or more than it.")
    category_starting_price = models.CharField(max_length=25, null=True, blank=True, help_text="This is the starting price of this website category.")
    category_cover_image = models.ImageField(max_length=255, null=True, blank=True, help_text="This is the cover image of the website category that will be displayed in all the major actions.")
    category_gallery_images = models.ImageField(max_length=255, null=True, blank=True, help_text="This is the main carousel image for the website category that will be displayed on the home category page.")
    category_description = models.CharField(max_length=1000, null=True, blank=True, help_text="This is the description of the website category.")

class WebsiteService(models.Model):
