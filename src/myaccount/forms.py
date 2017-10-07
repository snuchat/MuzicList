from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignupForm(forms.Form):
	nickname = forms.CharField(max_length=30, label='nickname')

	def signup(self, request, user):
		up = UserProfile()
		up.user = user
		up.nickname = self.cleaned_data['nickname']
		up.save()