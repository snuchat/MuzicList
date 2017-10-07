from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignupForm(forms.Form):
	nickname = forms.CharField(max_length=30, label='nickname')

	def signup(self, request, user):
		# user.first_name = self.cleaned_data['first_name']
		# user.last_name = self.cleaned_data['last_name']
		# user.save()

		up = UserProfile()
		up.user = user
		up.nickname = self.cleaned_data['nickname']
		up.save()