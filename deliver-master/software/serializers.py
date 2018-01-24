from rest_framework.serializers import ModelSerializer

from .models import License, Program, Version


class LicenseSerializer(ModelSerializer):
    class Meta:
        model = License
        fields = (
            'key',
        )


class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'name',
        )


class VersionSerializer(ModelSerializer):
    class Meta:
        model = Version
        fields = (
            'version_number',
            'download_url',
        )
