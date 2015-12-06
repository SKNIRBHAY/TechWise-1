from django.contrib import admin
from .models import SignUp
from .forms import SignUpUser
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display =["__unicode__", "username"]
    form = SignUpUser
    # class Meta:
    #     model = SignUp
admin.site.register(SignUp, SignUpAdmin)