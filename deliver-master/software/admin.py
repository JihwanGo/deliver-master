from django.contrib import admin

from .models import License, Program, Version


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'latest_version',
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'first_release',
        'download_url',
        'num_distribution',
    )
