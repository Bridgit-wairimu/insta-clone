from django import forms
from .models import Post, Comment, User,Profile

class NewPostForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)

    class Meta:
        model = Post
        fields = ('image', 'caption')


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)



class EditProfileForm(forms.ModelForm):
	picture = forms.ImageField(required=False)
	first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
	last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=False)
	location = forms.CharField(widget=forms.TextInput(), max_length=25, required=False)
	url = forms.URLField(widget=forms.TextInput(), max_length=60, required=False)
	profile_info = forms.CharField(widget=forms.TextInput(), max_length=260, required=False)

	class Meta:
		model = Profile
		fields = ('picture', 'first_name', 'last_name', 'location', 'url', 'profile_info')




class SignupForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True,)
	email = forms.CharField(widget=forms.EmailInput(), max_length=100, required=True,)
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Confirm your password.")

	class Meta:

		model = User
		fields = ('username', 'email', 'password')

class InstaLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')