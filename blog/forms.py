from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment

class NewUserForm(UserCreationForm):
    username        = forms.CharField( 
                        widget=forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                }
                            )
                        )
    email        = forms.EmailField( 
                        widget=forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                }
                            )
                        )
                    
    password1        = forms.CharField(
                        widget=forms.PasswordInput(
                            attrs={
                                'class': 'form-control',
                                }
                            )
                        )
    password2        = forms.CharField(
                        widget=forms.PasswordInput(
                            attrs={
                                'class': 'form-control',
                                }
                            )
                        )
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2'
            ]


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','rows': 20}),
            'body': forms.Textarea(
                attrs={
                    'row':50,
                    'label': "Comment",
                    }
                    ),
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

        widgets ={
            'title':forms.TextInput(attrs={'class':'create-post-title'}),
            # 'author':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'create-post-body'}),
        }