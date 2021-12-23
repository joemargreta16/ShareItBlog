from blog.models import Comment, Post
from django import forms

# Create your forms here.


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Leave a comment', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control mt-6',
        'placeholder': 'Comment here...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'thumbnail',
            'image_url',
            'content',
            'categories',
            'tags',
        )

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'author_id', 'type': 'hidden'}),
        }


class PostBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'thumbnail',
            'image_url',
            'content',
            'categories',
            'tags',
        )

        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'author_id', 'type': 'hidden'}),
        }


class ReplyForm(forms.ModelForm):
    content = forms.CharField(label='Leave a reply', widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control mt-6',
        'placeholder': 'Reply here...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)
