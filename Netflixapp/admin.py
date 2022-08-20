from django.contrib import admin
from .models import MembershipEmail, Signup, netflix_titles

# Register your models here.
admin.site.register(netflix_titles)
admin.site.register(Signup)
admin.site.register(MembershipEmail)