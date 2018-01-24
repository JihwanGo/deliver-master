import string

from django.core.exceptions import ValidationError
from django.db import models


def version_number_validator(value):
    digits_and_period = string.digits + '.'
    if any([(char not in digits_and_period) for char in value]):
        raise ValidationError('A version number must have digits and periods only.')


class Program(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name

    def latest_version(self):
        return self.versions.latest('version_number').version_number


class License(models.Model):
    key = models.CharField(
        max_length=20,
        primary_key=True,
    )
    institution = models.CharField(
        max_length=100,
    )
    allowed_programs = models.ManyToManyField(
        to=Program,
        related_name='licenses',
    )

    # TODO: Need migration

    def __str__(self):
        return '{} ({})'.format(self.institution, self.key)


class Version(models.Model):
    program = models.ForeignKey(
        to=Program,
        related_name='versions',
    )
    version_number = models.CharField(
        max_length=10,
    )
    download_url = models.URLField()
    first_release = models.DateTimeField(
        auto_now_add=True,
    )
    allowed_licenses = models.ManyToManyField(
        to=License,
        related_name='versions',
        blank=True,
    )

    def __str__(self):
        return '{} (v{})'.format(self.program, self.version_number)

    def available_licenses(self):
        return self.program.licenses.all()

    def num_distribution(self):
        return self.allowed_licenses.count()

    class Meta:
        unique_together = [('program', 'version_number')]
