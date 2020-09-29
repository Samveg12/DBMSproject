from django.contrib import admin
from .models import countries,disaster,safehaven,transport,final

admin.site.register(countries)
admin.site.register(disaster)
admin.site.register(safehaven)
admin.site.register(transport)
admin.site.register(final)

