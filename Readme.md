![GitHub repo size](https://img.shields.io/github/repo-size/A1dricAP/Social)
[![GitHub issues](https://img.shields.io/github/issues/A1dricAP/Social)](https://github.com/A1dricAP/Social/issues)
<img src="https://img.shields.io/badge/django-v3.1.0-yellow"/>
<img src="https://img.shields.io/badge/license-MIT-blue">

# Social App

## Django framework and React

This app is a social media categorised one. The main purpose is to learn Django framework.

You need to create separate apps for the parts of the project. There is a blog app that consists of `views.py` and `urls.py`.

The `urls.py` file, basically is used to map the urls to the corresponding function in `view.py`.

---

There exists a `templates` folder within the `blog` folder; responsible for mapping out the results to be displayed to the user, via the `urls.py`.

---

instead of hardcoding the url path in the html tags,

```
href="/"

href="about/"
```

we can use url patterns; by declaring the name of the path in the tags. shown below.

```
href="{% url 'blog-home'%}"

href="{% url 'blog-about'%}"
```

> 'blog-home'

> 'blog-about'

are defined in `urls.py`

> path('', views.home, name='blog-home')

> path('about/', views.about, name='blog-about')

---

## Admin privilegdes:

For admin priviledges, we've to create a super user. For this, migrations need to be added. This is done by the following steps:

1. run the migrate command
   > python manage.py migrate
2. make the migrations in the folder.
   > python manage.py makemigration
3. run the last command
   > python manage.py createsuperuser
4. and then follow along with the prompts in the terminal.

---

## Database:

_Using SQLite Database for development and use PostgreSQL database for production._

We've to run `migrations`; inorder to update the database with any changes.

> python manage.py makemigrations

Django will automatically create the backend SQL for us, to view the sql code running, use the command in the terminal:

> python manage.py sqlmigrate <name_of_rootfolder> <name_of_initial.py>

## To query database from the terminal

```
* if you want to query your database from the terminal, first step is to open the python django shell
-> python manage.py shell

* then import the specific models from the project folder.
-> from <app>.<folder_name> import <model_name>

* to run functions, set the db content to a variable.
-> <user_variable_name>=User.objects.filter(username="aldric_ap")

* then to make a post, first assign it a variable,
-> <post_variable_name>= Post(title="", content="", author=<user_variable_name>)

* after creating post, save it.
-> <post_variable_name>.save()

* to view the posts, use the following:
-> Post.objects.all()

* if you want to view the content of your post, create a new variable of that post and view it.
-> post = Post.objects.first() // creating the post instance.
-> post.content // to display the content of the post.

* if we want to retrieve all the post from one specific user, then we can use the following command:
-> user.post_set.all() -> <user_variable_name>.post_set.all()
Because we're creating two instances, one of user and other of post. So we can use those two instances to retrieve their respective info.

* if i want to create a new post directly using the current user, use the following:
-> user.post_set.create(title="new post", content="post content")
```

---

# **Notes**

```
within models.py file; django already has an authentication system along with a user model that it has created for us. For now we're not gonna make a new model, but only a post model. and this will be a class that inherits from django model class.

first we declare a class and inherit from `models.Model`. Each class is gonna be its own table in the database.

there are attributes. where each attribute is basically a different field in the database.
The following attributes are present:

-> title - (this is gonna be a character field with maximum length set to 100.)

-> content - (this is gonna be a text field to take in multiple lines of input from user.)

-> date_posted - (using the datetimefield() along with the default moethod of timezone imported into this file.)

-> author - (importing the User model to use it along with this entity. and setting the on_delete function to delete the post if user is deleted.)

Why are migrations useful?
-> Migrations are useful because it allows us to make changes to the database even after the database has been created, containing data.

Inorder for the posts to be visible on our admin page, we need to import Post model in admin.py.

```

---
