<pre><code>     _  _                                    _ 
  __| |(_)__ _ _ _  __ _ ___   _ __ _ _ ___ (_)___ __| |_ 
 / _` || / _` | ' \/ _` / _ \ | '_ \ '_/ _ \| / -_) _|  _|
 \__,_|/ \__,_|_||_\__, \___/ | .__/_| \___// \___\__|\__|
     |__/          |___/      |_|         |__/            
</code></pre>

A Student Study Website.

![Project Preview](preview_images/sc1.png)
![Project Preview](preview_images/s2.png)
![Project Preview](preview_images/sc3.png)
![Project Preview](preview_images/sc4.png)
![Project Preview](preview_images/scr4.png)
![Project Preview](preview_images/scr5.png)

Features
--------

* User Authentication
* ToDo List App
* Homework
* YouTube Search
* Notes Taking
* Dictionary Search Feature
* WikiPedia Search Feature
* Google Books Search Feature



Requirements
------------

* [Django](https://www.djangoproject.com/download/)
* [Pillow](https://pypi.org/project/Pillow/)
* [virtualenv](http://www.virtualenv.org/en/latest/)
* [youtube-search-python](https://pypi.org/project/youtube-search-python/)
* [wikipedia](https://pypi.org/project/wikipedia/)
* [cloudinary](https://pypi.org/project/cloudinary/)
* [Requests](https://pypi.org/project/requests/)

Getting started
---------------
Clone Repository
'''bash
$ git clone https://github.com/Ayomisco/optistud.git
'''

Change Directory to Project File
'''bash
$ cd optistud
'''

Create a virtual enviroment to work inside.

```bash
$ virtualenv my-environment
```

Jump in and turn it on.

```bash
$ cd my-environment
$ . bin/activate
```

Install modules in requirements.txt.

```bash
$ pip install -r requirements.txt
```

Make Migrations.

```bash
$ python manage.py makemigration
$ python manage.py migrate
```
Now that you have setup the project, run it on your local system 

'''bash
$ python manage.py runserver
'''

That is it we're done. Enjoy!!!

