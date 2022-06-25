from django.http import HttpResponse
from typing import List


def options(methods: List[str] = ['GET']):
    def wrap(f):
        def _options(request, *args, **kwargs):
            if request.method == 'OPTIONS':
                return HttpResponse(headers={'Allow': methods})
            return f(request, *args, **kwargs)
        return _options
    return wrap
