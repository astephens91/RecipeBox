from django.shortcuts import render, HttpResponseRedirect, reverse

from recipeBoxProject.models import RecipeItem, Author
from recipeBoxProject.forms import AddAuthor, AddRecipeItem


def index(request):
    html = "index.html"

    recipes = RecipeItem.objects.all()

    return render(request, html, {'data': recipes})


def recipe_view(request, id):
    recipe_html = "recipe.html"
    recipe = RecipeItem.objects.filter(id=id)

    return render(request, recipe_html, {'data': recipe})


def author_view(request, id):
    author_html = "author.html"
    author = Author.objects.filter(id=id)
    recipe = RecipeItem.objects.filter(author=id)

    return render(request, author_html, {'data': author, 'recipe': recipe})


def addauthorview(request):
    html = 'generic_form.html'

    if request.method == "POST":
        form = AddAuthor(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthor()

    return render(request, html, {'form': form})


def addrecipeview(request):
    html = 'generic_form.html'

    if request.method == "POST":
        form = AddRecipeItem(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeItem()

    return render(request, html, {'form': form})
