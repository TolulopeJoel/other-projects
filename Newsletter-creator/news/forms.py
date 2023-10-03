from django import forms

from .models import NewsLetter, Post

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('title', 'posts', 'ready')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'posts': forms.CheckboxSelectMultiple(attrs={'class': 'form-control w-50'}),
        }
    posts = forms.ModelMultipleChoiceField(
        queryset=Post.objects.filter(validated=True, status='draft'),
        widget=forms.CheckboxSelectMultiple
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'source', 'image', 'validated')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image url (optional)'}),
        }