from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy

class MyUserLoginForm(forms.ModelForm):

    class Meta():
        model=MyUser
        fields=["username","password"]
        # 重写字段样式
        widgets={"password":forms.PasswordInput(attrs={"class":"form-control"}),
                 "username":forms.TextInput(attrs={"class":"form-control"})
                 }
        help_texts={
            "username":gettext_lazy(""),
        }

class MyUserRegistForm(forms.ModelForm):
    class Meta():
        model=MyUser
        fields=["username","password","email"]
        # 重写字段样式
        widgets={"password":forms.PasswordInput(attrs={"class":"form-control"}),
                 "username":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"})
        }
        help_texts={
            "username":gettext_lazy(""),
        }