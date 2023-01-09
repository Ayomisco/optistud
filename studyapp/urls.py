from django.urls import path
from .views import *
from user_auth.views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('notes/', notes, name='notes'),
    path('delete_note/<int:pk>/', DeleteNote, name='delete-note'),

    path('notes_detail/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('delete_homework/<int:pk>/', HomeworkDelete, name='delete-homework'),
    path('homework/', Homeworks, name='homework'),
    path('update_homework/<int:pk>/', update_homework, name='update_homework'),

    path('youtube/', Youtube, name='youtube'),
    path('todo/', Todo, name='todo'),
    path('update_todo/<int:pk>/', update_todo, name='update-todo'),
    path('delete_todo/<int:pk>/', delete_todo, name='delete-todo'),
    
    path('books/', books, name='books'),
    path('dictionary/', Dictionary, name='dictionary'),
    path('wikipedia/', Wiki, name='wiki'),
    path('conversion/', Conversion, name='conversion'),
    

    # path('login/', ToDo, name='login'),
    path('help/', Help, name='help'),








]

# handler500 = 'myappname.views.error_500'
# handler403 = 'myappname.views.error_403'
# handler400 = 'myappname.views.error_400'