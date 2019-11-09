from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        "class" :"form-control",
        "placeholder" :"fullname"
    }))
    email =    forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"Enter Your Email"
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control",
        "placeholder":"Enter Your Content"
    }))
    
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Gmail formate is required")
        
        return email
    
    
class LoginForm(forms.Form):
    username  = forms.CharField(widget=forms.TextInput(attrs={
        "class" :"form-control",
        "placeholder" :"fullname"
    }))
    password  = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" :"form-control",
        "placeholder" :"fullname"
    }))
    
    
class RegisterForm(forms.Form):
    
    username  = forms.CharField(widget=forms.TextInput(attrs={
        "class" :"form-control",
        "placeholder" :"fullname"
        }))
    
    email     = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"Enter Your Email"
        }))

    password  = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" :"form-control",
        "placeholder" :"password"
        }))

    password2  = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" :"form-control",
        "placeholder" :"confirm Password",
        "label":"confirm Password"
        }))
    
    def clean_username(self):
        username =  self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username already taken")
        return username
    
    def clean_email(self):
        email =  self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already taken")
        return email
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        print(password)
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("password must be match.")
        return data