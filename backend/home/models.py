from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    sasfsdf = models.OneToOneField(
        "home.Test",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_sasfsdf",
    )
    dfsasa = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_dfsasa",
    )
    sadfasf = models.ManyToManyField(
        "home.Fnhgjhjgjh", blank=True, related_name="customtext_sadfasf",
    )
    sdfdsf = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_sdfdsf",
    )
    fdgg = models.BigIntegerField(null=True, blank=True,)
    sdfsdf = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test(models.Model):
    "Generated Model"
    nkhgkhg = models.BigIntegerField()


class Fnhgjhjgjh(models.Model):
    "Generated Model"
    jhgkhgkjhg = models.BigIntegerField()
