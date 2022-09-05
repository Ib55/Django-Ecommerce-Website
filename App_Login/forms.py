from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from App_Login.models import Profile,User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2')