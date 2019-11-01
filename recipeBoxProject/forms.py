from django import forms
from recipeBoxProject.models import Author, RecipeItem


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=50)


class AddRecipeItem(forms.ModelForm):
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # title = forms.CharField(max_length=100)
    # description = forms.CharField(widget=forms.Textarea)
    # time = forms.IntegerField()
    # instructions = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = RecipeItem
        fields = [
            'author',
            'title',
            'description',
            'time',
            'instructions'
        ]