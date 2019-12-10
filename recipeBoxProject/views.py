from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from recipeBoxProject.models import RecipeItem, Author
from recipeBoxProject.forms import AddAuthor, AddRecipeItem, LoginForm, EditRecipeItem
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


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
    favs = author[0].favorites

    return render(request, author_html, {'data': author, 'recipe': recipe, 'favorites': favs})


@login_required
def addauthorview(request):
    html = 'generic_form.html'
    if request.user.is_staff:
        if request.method == 'POST':
            form = AddAuthor(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                u = User.objects.create_user(
                    username=data['name'],
                    password=data['password']
                )
                Author.objects.create(
                    user=u,
                    name=data['name'],
                    bio=data['bio'],
                )
            return HttpResponseRedirect(reverse('homepage'))
        form = AddAuthor()
        return render(request, html, {'form': form})
    return HttpResponseRedirect('/error')


@login_required
def addrecipeview(request):
    html = 'generic_form.html'

    if request.method == "POST":
        form = AddRecipeItem(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeItem()

    return render(request, html, {'form': form})


#########################################################New code added by ethan ebel
def editrecipeview(request, recipe_id):
    recipe = RecipeItem.objects.filter(id=recipe_id).first()

    if request.method == 'POST':
        form = EditRecipeItem(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.description = data['description']
            recipe.time = data['time']
            recipe.instructions = data['instructions']
            recipe.save()

            return redirect('/recipes/{}'.format(recipe.id))
    else:
        form = EditRecipeItem({
            'title': recipe.title,
            'description': recipe.description,
            'time': recipe.time,
            'instructions': recipe.instructions
            })
        context = {'form': form}

        return render(request, 'generic_form.html', context)


def add_favorite(request, recipe_id, author_id):
    recipe = RecipeItem.objects.filter(id=recipe_id).first()
    author = Author.objects.filter(id=request.user.id).first()


    author.favorites.add(recipe)
    author.save()

    return redirect('/author/{}'.format(request.user.id))

##################################################################


def login_view(request):
    html = 'generic_form.html'

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def error_view(request):
    error_html = 'error.html'
    return render(request, error_html)