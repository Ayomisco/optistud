
from django import forms
from .models import  *

class HelpForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': 'Enter your name'}), max_length=150, required=True)
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 
                            'placeholder': '+234893332'}),required=True)

    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 
                            'placeholder': 'name@site.com'}), max_length=150, required=True)

    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': 'Title of Message'}), max_length=150, required=True)


    message= forms.CharField(max_length=1500,
                            widget= forms.Textarea
                            (attrs={'class':'form-control', 
                            'placeholder': 'Enter message', 'rows':3}), required=True)
    class Meta:
        model = Help
        fields = ('name', 'phone','email', 'subject', 'message')


class NotesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': 'Enter title'}), max_length=150, required=True)

    description = forms.CharField(max_length=1500,
                            widget= forms.Textarea
                            (attrs={'class':'form-control', 
                            'placeholder': 'Enter notes', 'rows':3}), required=True)
    class Meta:
        model = Notes
        fields = ('title', 'description')



class homeworkForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': 'Enter subject name'}), max_length=150, required=True)

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': 'Give your homework a title'}), max_length=150, required=True)

    description = forms.CharField(max_length=1500,
                            widget= forms.Textarea
                            (attrs={'class':'form-control', 
                            'placeholder': 'Enter notes', 'rows':3}), required=True)
   
    due = forms.DateTimeField(widget=forms.NumberInput(attrs={'class':'form-control', 'type':'date'}), required=True)

    is_finished  = forms.BooleanField(required=False)

   
    class Meta:
        model = Homework
        fields = ('subject', 'title', 'description', 'due', 'is_finished')


class DashboardSearchForm(forms.Form):
    text = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Enter your query here...'})))


class TodoForm(forms.ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
                            'placeholder': 'Enter your ToDo here'}), max_length=150, required=True)

    is_finished  = forms.BooleanField(required=False)

    class Meta:
        model = ToDo
        fields = ['title', 'is_finished']

class ConversionForm(forms.Form):
        CHOICES = [('length', 'Length'), ('mass', 'Mass')]
        measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ' mr-3 mb-3'}))

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard', 'Yard'), ('foot', 'Foot')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs= {'type': 'number', 'placeholder': 'Enter the Number to be converted'}
    ))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES,
            attrs={}
        )
    )  

    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES,
            attrs={}
        )
    )  

class ConversionMassForm(forms.Form):
    CHOICES = [('pound', 'Pound'), ('kilogram', 'Kilogram')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput(
        attrs= {'type': 'number', 'placeholder': 'Enter the Number to be converted'}
    ))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES,
            attrs={}
        )
    )  

    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES,
            attrs={}
        )
    ) 