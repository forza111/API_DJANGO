from django.contrib import admin
from .models import Question,Choice,Polls

admin.site.register(Polls)
admin.site.register(Question)
admin.site.register(Choice)


# Register your models here.
