from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import License
from .serializers import VersionSerializer


class AvailableLicense(APIView):
    def get(self, request, **kwargs):
        program_name = kwargs['program']
        license_key = kwargs['license']

        try:
            selected_license = License.objects.get(key=license_key)
        except License.DoesNotExist:
            raise Http404

        latest_version = selected_license.versions.filter(program__name=program_name).latest('version_number')
        serializer = VersionSerializer(latest_version)
        return Response(serializer.data, status=HTTP_200_OK)
