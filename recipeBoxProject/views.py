from django.shortcuts import render

from recipeBoxProject.models import RecipeItem
from recipeBoxProject.models import Author

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
    print(recipe)
    return render(request, author_html, {'data': author, 'recipe': recipe})

    
