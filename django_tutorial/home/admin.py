from django.contrib import admin
from .models import department ,users,login,Leave_apply,Leave_request
from.models import Leave_request

# Register your models here.
admin.site.register(department)
admin.site.register(users)
admin.site.register(login)
admin.site.register(Leave_apply)
admin.site.register(Leave_request)

