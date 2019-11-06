RecipeBox
v0.1

Created test reciped with authors.  RecipeItems include titles, descriptions, time required, and instructions.  So far, Authors only contains a name entry and a short bio.  Routing include links to author pages displaying their info and recipes that they've worked on.  Clicking on recipe links routes to the recipe page which displays all the relevant information, including author links.

v0.2

Created forms to add both both recipes and authors.  The author add form is done with regular forms and the recipe is a modelform.  Added css styling capabilities to the application as well.


v0.3

Created user authentication.  Users can log in and out and, depending on their permissions, add new recipes and authors.  Users only need to be logged in to create recipes, however they need staff acess to be able to create authors.  If a user tries to create a new author without staff access, they will be redirected to an error page.