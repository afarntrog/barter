from django import forms


class ProductPostForm(forms.Form):
    product_title = forms.CharField(max_length=500, required=False)
    product_description = forms.CharField(widget=forms.Textarea, required=False)
    images = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    tags = forms.CharField(max_length=500, required=False)

# Add option to temporaly hide post