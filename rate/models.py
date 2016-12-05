from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ObjectDoesNotExist


class Tag(models.Model):
    tag_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "countries"


class Destination(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Preference(models.Model):
    destination = models.ForeignKey(Destination)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return "{} - {}".format(self.destination.name, self.score)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    preferences = models.ManyToManyField(Preference)

    def set_preference(self, dest_name, score):
        try:
            pref = self.preferences.get(destination__name=dest_name)
        except ObjectDoesNotExist:
            pref = None
        if pref is not None:
            if score != -1:
                pref.score = score
                pref.save()
        else:
            dest = Destination.objects.get(name=dest_name)
            if score == -1:
                new_pref = Preference.objects.create(destination=dest, score=0)
            else:
                new_pref = Preference.objects.create(destination=dest, score=score)
            self.preferences.add(new_pref)
            self.save()
