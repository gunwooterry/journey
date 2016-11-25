from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    tag_id = models.PositiveSmallIntegerField()
    tag_name = models.CharField(max_length=30)


class Country(models.Model):
    name = models.CharField(max_length=30)


class Destination(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, null=True, blank=True)
    tags = models.ManyToManyField(Tag)


class Preference(models.Model):
    destination = models.ForeignKey(Destination)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    preferences = models.ManyToManyField(Preference)
