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
