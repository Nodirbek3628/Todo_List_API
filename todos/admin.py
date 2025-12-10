from django.contrib import admin
from .models import Task,Category,CustomUser


admin.site.register([Task,Category])