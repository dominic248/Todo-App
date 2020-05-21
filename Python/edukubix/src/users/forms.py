from django import forms  

from django.contrib.auth.forms import ReadOnlyPasswordHashField
  

from django.contrib.auth import get_user_model
User=get_user_model() 

class UserAdminForm(forms.ModelForm): 
    password = ReadOnlyPasswordHashField(
      label= ("Password"),
      help_text= ("Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"password/\">this form</a>."))   
    class Meta:  
        model = User  
        fields = "__all__" 