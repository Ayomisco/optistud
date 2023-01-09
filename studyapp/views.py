import random
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests

from studyapp.forms import *
from user_auth.models import Profile

# import inner modules
from .models import *
# Create your views here.
import wikipedia


#importing django timezone from utils
from django.utils import timezone

from django.contrib import messages
# Django Mail
from django.core.mail import send_mail
from base import settings

# View
from django.views import generic
from django.views.generic import View, TemplateView, ListView, DetailView

from youtubesearchpython import VideosSearch






# Errors

def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'500.html',  status=500)


def index(request):
  
    
    
    context = {
      

    }
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render(context, request))
    # return render(request, 'dashboard.html')




def Dashboard(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
   
    
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile

    }
    template = loader.get_template('dashboard.html')
    
    return HttpResponse(template.render(context, request))
    # return render(request, 'dashboard.html')



def notes(request):

    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    else:
        profile = Profile.objects.get(user=request.user)
        form = NotesForm()
        

        # Notes form
        if request.method == "POST":
            form = NotesForm(request.POST)
            if form.is_valid():
                user = request.user
                title= request.POST['title']
                description = request.POST['description']
                notes = Notes(user=user, title=title, description=description)
                notes.save()

            messages.success(request, f"Notes Added by {request.user.username} Successfully ")
            return redirect('notes')
        else:
            form = NotesForm()

        notes = Notes.objects.filter(user=request.user)

        context = {
            'notes': notes,
            'form': form,
            'profile': profile,

        }
        template = loader.get_template('notes.html')
        
        return HttpResponse(template.render(context, request))


def DeleteNote(request, pk=None):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    else:
        Notes.objects.get(id=pk).delete()
        messages.success(request, f"Notes deleted by {request.user.username} Successfully ")
        return redirect('notes')
    

class NoteDetailView(DetailView):
    model = Notes
    template_name = 'notes_detail.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context
    
    
    # return HttpResponse(template.render(context, request))

# @login_required
def Homeworks(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")

    form = homeworkForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = True
            except:
                finished = False

            user = request.user
            subject = request.POST['subject']
            title = request.POST['title']
            description = request.POST['description']
            due = request.POST['due']
            
            # is_finished = request.POST['is_finished']
            homework = Homework(user=user,
             subject=subject,
              title=title, 
             description=description, 
             due=due, 
             is_finished=finished)
            # print('Successfully added')
            
            homework.save()
            messages.success(request, f"Homework Added by {request.user.username} Successfully ")
            return redirect('homework')

    else:
        form = homeworkForm()
        # print(f'Not Successfully added {subject}, {title}')

        



    homework = Homework.objects.filter(user=request.user)

    # Checking if homwork is done or not
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    profile = Profile.objects.get(user=request.user)
    template = loader.get_template('homework.html')
    
    context = {
        'homework': homework,
        'homework_done': homework_done,
        'form': form,
        'profile': profile

    }
    
    return HttpResponse(template.render(context, request))


def HomeworkDelete(request,pk=None):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    Homework.objects.get(id=pk).delete()
    messages.success(request, f"Notes deleted by {request.user.username} Successfully ")
    return redirect('homework')

# Youtube View
def Youtube(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    # Creating form object
    if request.method == "POST":
        form = DashboardSearchForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)

            context = {
                'form': form,
                'results': result_list
            }
        return render(request, 'youtube.html', context)
    else:
        profile = Profile.objects.get(user=request.user)
        form = DashboardSearchForm()
    template = loader.get_template('youtube.html')
    context = {
        'form': form,
        'profile': profile

    }
    
    return HttpResponse(template.render(context, request))



def Todo(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
                
            except:
                finished = False
            user = request.user
            todos = ToDo(
                user = user,
                title = request.POST['title'],
                is_finished = finished
            )
            todos.save()
            messages.success(request, f"ToDo Added by {request.user.username.capitalize()} successfully!!!" )
            return redirect('todo')

    else:
        form = TodoForm()
    todo = ToDo.objects.filter(user=request.user)

    # Checking if there's any todo available and that has not being finished
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False

    template = loader.get_template('todo.html')
    context = {
        'todo': todo,
        'form': form,
        'todo_done': todos_done,
        'profile': profile
        
    }
    
    return HttpResponse(template.render(context, request))

# Updating Todo Is Finished
def update_todo(request, pk=None):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    todo = ToDo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')


# Deleting ToDo
def delete_todo(request, pk=None):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    ToDo.objects.get(id=pk).delete()
    return redirect("todo")



# books 
def books(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    
    if request.method == "POST":
        form = DashboardSearchForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                'authors': answer['items'][i]['volumeInfo'].get('authors'),
                'description': answer['items'][i]['volumeInfo'].get('description'),
                'pageCount': answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories': answer['items'][i]['volumeInfo'].get('categories'),
                'rating': answer['items'][i]['volumeInfo'].get('ratingsCount'),
                'thumbnail': answer['items'][i]['volumeInfo'].get('imageLinks').get("thumbnail"),
                'preview': answer['items'][i]['volumeInfo'].get('previewLink'),

            }
            result_list.append(result_dict)
            context = {
                'form': form,
                'results': result_list,
            }
        return render(request, 'books.html', context)

    form = DashboardSearchForm()

    profile = Profile.objects.get(user=request.user)
    template = loader.get_template('books.html')
    context = {
        'form': form,
        'profile': profile
    }
    return HttpResponse(template.render(context, request))


# Dictionary 
def Dictionary(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")

    if request.method == "POST":
        form = DashboardSearchForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
        
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][1]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][1]['synonyms']
            antonyms = answer[0]['meanings'][1]['antonyms']


            context = {
                'form': form,
                'input':  text,
                'phonetics': phonetics,
                'audio': audio,
                'definition': definition,
                'example': example,
                'synonyms': synonyms,
                'antonyms': antonyms
            }
            
        except Exception as error:
            # print(error)
            print(error)

            context = {
                'form': form,
                'input':  '',
            }

        return render(request, 'dictionary.html', context)
    else:
        form = DashboardSearchForm()
        profile = Profile.objects.get(user=request.user)
        template = loader.get_template('dictionary.html')
        context = {
        'form': form,
        'profile': profile
        }
    return HttpResponse(template.render(context, request))



# Wikipedia
def Wiki(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    if request.method == 'POST':
        text = request.POST['text']
        form = DashboardSearchForm(request.POST)

        try:
            search = wikipedia.page(text,auto_suggest=False, redirect=True, preload=False)
            context = {
            'text': text,
            'form': form,
            'title': search.title,
            'link': search.url,
            'details': search.content,
            }
            return render(request, 'wiki.html', context)

            # p = wikipedia.page(string)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            search = wikipedia.page(s)

            # p = wikipedia.page(s)
            context = {
                'text': text,
                'form': form,
                'title': search.title,
                'link': search.url,
                'details': search.summary,
            }
            return render(request, 'wiki.html', context)
    form = DashboardSearchForm()

    profile = Profile.objects.get(user=request.user)
    template = loader.get_template('wiki.html')
    context = {
        'form': form,
        'profile': profile
    }
    return HttpResponse(template.render(context, request))



def Conversion(request):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context = {
                'form': form,
                'm_form': measurement_form,
                'input': True
            }
            if 'input' in request.POST:
                first  = request.POST['measure1']
                second = request.POST['measure2']
                answer = ''
                if input == int(input) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input} yard = {int(input)*3} foot'
                    if first == 'foot' and second == 'yard':
                        answer = f'{input} foot = {int(input)/3} yard'
                    ccontext = {
                        'form': form,
                        'm_form': measurement_form,
                        'input': True,
                        'answer': answer,
                    }
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionLengthForm()
            context = {
                'form': form,
                'm_form': measurement_form,
                'input': True
            }
            if 'input' in request.POST:
                first  = request.POST['measure1']
                second = request.POST['measure2']
                answer = ''
                if input == int(input) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input} pound = {int(input)*0.453592} foot'
                    if first == 'kilogram' and second == 'pound':
                        answer = f'{input} kilogram  = {int(input)/2.20462} pound'
                    context = {
                        'form': form,
                        'm_form': measurement_form,
                        'input': True,
                        'answer': answer,
                    }    

    else:



        form = ConversionForm()
        profile = Profile.objects.get(user=request.user)
        template = loader.get_template('conversion.html')
        
        context = {
            'form': form,
            'input': False,
            'profile': profile
        }
        return HttpResponse(template.render(context, request))
















# Help Viewa
def Help(request):

    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    if request.method == 'POST':
        form = HelpForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = loader.render_to_string('emails/contactForm.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'subject': subject,
                'message': message
            })
            
            message = form.save(commit=False)
            # saving it base on timezone
            message.message_date = timezone.now()
            form.save()

            subject = 'Optistu Help Center'
            contact_message = "%s : %s via %s "%(subject, name, email)
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'fayomide324@gmail.com']
            send_mail(subject, contact_message, from_email, to_email, fail_silently=False, html_message=html)
            # send_mail('The contact form subject', 'This is the message', 'francisayomide878@gmail.com', {'fayomide324@gmail.com'}, html_message=html)
            contactmessages = messages.success(request,"Message Sent Successfully")
            return redirect('help')
    
    else:
        contactmessages = messages.error(request,"Message not successfully sent please try again")
        form = HelpForm()


    profile = Profile.objects.all()
    template = loader.get_template('help.html')
    
    context = {
        'form': form,
        'contactmessages': contactmessages,

    }
    
    return HttpResponse(template.render(context, request))


def update_homework(request, pk=None):
     if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
     homework = Homework.objects.get(id=pk)
     if homework.is_finished == True:
        homework.is_finished = False
     else:
        homework.is_finished = True
     homework.save()
     return redirect('homework')