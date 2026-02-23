from User.models import AllowedIP
from django.http import HttpResponseForbidden

class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        print("IP:", ip)
        print("DB:", list(AllowedIP.objects.values_list("ip_address", flat=True)))

        if not AllowedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Forbidden")

        return self.get_response(request)