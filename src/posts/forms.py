from django import forms
from .models import Post
from gallery.models import GalleryImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover_image', 'body', 'location_name', 'country', 'travel_types', 'published']
        labels = {
            'title': 'Заглавие',
            'cover_image': 'Корица',
            'body': 'Разказ',
            'location_name': 'Конкретна локация',
            'country': 'Държава',
            'travel_types': 'Тип пътуване',
            'published': 'Публикуван',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 12, 'class': 'form-control'}),
            'travel_types': forms.CheckboxSelectMultiple(),
        }


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'caption']
        labels = {'image': 'Снимка', 'caption': 'Надпис'}


GalleryFormSet = forms.modelformset_factory(
    GalleryImage,
    form=GalleryImageForm,
    extra=5,
    can_delete=True,
)
