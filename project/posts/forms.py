from django.forms import ModelForm
from .models import Post


class AddPostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter title"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter description"}
        )

    class Meta:
        model = Post
        fields = "__all__"
