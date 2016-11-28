from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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


class PreferenceManager(models.Manager):
    def create_preference(self, dest, score):
        pref = self.create(destination=dest, score=score)
        return pref


class Preference(models.Model):
    destination = models.ForeignKey(Destination)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    objects = PreferenceManager()


class UserProfileManager(models.Manager):
    def create_profile(self, user):
        profile = self.create(user=user)
        return profile


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    preferences = models.ManyToManyField(Preference)
    objects = UserProfileManager()

    def set_preference(self, dest_name, score):
        is_scored_before = False
        for pref in self.preferences.all():
            if pref.destination.name == dest_name:
                if score != -1:
                    pref.score = score
                    pref.save()
                is_scored_before = True
                break
        if not is_scored_before:
            dest = Destination.objects.get(name=dest_name)
            if score == -1:
                new_pref = Preference.objects.create_preference(dest, 0)
            else:
                new_pref = Preference.objects.create_preference(dest, score)
            self.preferences.add(new_pref)
        self.save()
