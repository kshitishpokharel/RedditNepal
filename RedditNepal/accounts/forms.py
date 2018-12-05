from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "UserName"
        self.fields['email'].label = "Enter your email"
        self.fields['password1'].label = "Enter the password"
        self.fields['password2'].label = "Re-Enter the password"
