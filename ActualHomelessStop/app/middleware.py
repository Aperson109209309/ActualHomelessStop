from django.core.cache import cache
# from django.http import JsonResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
# import time

class RateLimitMiddleware(MiddlewareMixin):
    RATE_LIMIT = getattr(settings, 'CHATBOT_RATE_LIMIT')  # requests
    TIME_WINDOW = getattr(settings, 'CHATBOT_RATE_LIMIT_TIME_WINDOW_SECOND')  # 1 hour in seconds

    def process_request(self, request):
        if request.method == 'POST' and 'openai' in request.path:
            user_ip = self.get_client_ip(request)
            cache_key = f"rate_limit_{user_ip}"

            request_count = cache.get(cache_key, 0)

            if request_count >= self.RATE_LIMIT:
                request.META['HTTP_RATE_LIMIT_EXCEEDED'] = True
                # return JsonResponse({'error': 'Rate limit exceeded. Please complete the CAPTCHA.'}, status=429)

            # Increment request count and set expiration
            cache.set(cache_key, request_count + 1, timeout=self.TIME_WINDOW)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
