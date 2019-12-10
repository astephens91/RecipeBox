from django import forms
from recipeBoxProject.models import RecipeItem


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)


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


class EditRecipeItem(forms.ModelForm):

    class Meta:
        model = RecipeItem
        fields = [
            'title',
            'description',
            'time',
            'instructions'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)