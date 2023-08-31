from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(CustomUsers)
admin.site.register(TherapistDetail)
admin.site.register(ClientDetail)
admin.site.register(BusinessUnit)
admin.site.register(Services)
admin.site.register(ClientSubscription)
admin.site.register(BookingOrder)
admin.site.register(Transaction)