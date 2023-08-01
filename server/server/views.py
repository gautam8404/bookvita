from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


def health_check(request):
    return Response({'status': 'ok'}, status=HTTP_200_OK)
