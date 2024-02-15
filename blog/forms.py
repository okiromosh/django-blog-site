from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields you want to include in the form

        # You can customize widgets and add CSS classes for styling here
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
        }
