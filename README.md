# BookED

**Sources :**

-https://collegeai.com/

-https://newsapi.org/

-https://www.youtube.com/watch?v=qDwdMDQ8oX4

-https://getbootstrap.com/docs/4.0/utilities/flex/?

**Start virtualenv**

- py -m pip install --user virtualenv

- py -m venv booked_env

- .\env\Scripts\activate

- pip install -r requirements.txt

- deactivate

**Packages Used :**

- py -m pip install Django

- pip install newsapi-python

- pip install Pillow

- pip install django-filter

- pip install django-crispy-forms

- pip install django-allauth

- pip install django-dirtyfields

- pip install django-simple-captcha

- pip install django-utils-six

- pip install djangorestframework-jwt

**Extra Links :**

Pagination/filtering solution = https://www.youtube.com/watch?v=dkJ3uqkdCcY , https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html

Models Reference = https://docs.djangoproject.com/en/3.1/topics/db/models/

select2 = https://select2.org/configuration/options-api , https://www.youtube.com/watch?v=8VYx-cNF1lU

filter ajax video = https://www.youtube.com/watch?v=8VYx-cNF1lU&t=1503s

**API:**

Documentation:

- https://www.django-rest-framework.org/api-guide/settings/ (api django framework)

- https://jpadilla.github.io/django-rest-framework-jwt/ (jwt auth api)

  - Create Token : curl -X POST -d "username=rex&password=zebra12345" http://127.0.0.1:8000/api/auth/token-auth/

  - Create Post:

                    curl -g -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InJleCIsImV4cCI6MTYwNTU4NjAxMSwiZW1haWwiOiJpc3R2YW5mOEBob3RtYWlsLmNvbSJ9.c8jO9470QKiGw-nDLug-iXNrgzt9iWg4aOAv62D6KnM"  -d '{
                        "title": "Hello",
                        "content": "Hiiiiii",
                        "schools": 1,
                        "course": 1,
                        "classes": [1],
                        "isbn": 232323,
                        "semester": 3,
                        "visible": false
                    }' http://127.0.0.1:8000/api/posts/create/?type=post
