from registration.forms import RegistrationForm
from .models import User
from captcha.fields import CaptchaField

class UserRegistrationForm(RegistrationForm):
    captcha = CaptchaField()
    class Meta:
        model = AppsUser
        fields = ['username', 'first_name', 'last_name', 'password1',
                  'password2', 'email']
