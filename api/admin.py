from django.contrib import admin
from .models import Profile, Thread, Post, User, Pin, Claim


# Register your models here.
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Pin)
# admin.site.register(Claim)