#from django.urls import hello_world
from django.contrib import admin
from django.urls import path, include
#from .views import NoteCreateView
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NoteViewSet

from .views import *
from . import views 


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'notes', NoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list-create'),
    path('notes/', views.NoteViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='category-list-create-update-destroy'),
    path('order_notes/latest/', views.OrderNotesByLatestView.as_view(), name='order-notes-latest'),
    path('filter_notes/unfinished/', views.FilterUnfinishedNotesView.as_view(), name='filter-unfinished-notes'),
    path('filter_notes/overdue/', views.FilterOverdueNotesView.as_view(), name='filter-overdue-notes'),
    path('filter_notes/done/', views.FilterDoneNotesView.as_view(), name='filter-done-notes'),
    path('sort_notes/due_date/', views.SortNotesByDueDateView.as_view(), name='sort-notes-due-date'),
    path('sort_notes/priority/', views.SortNotesByPriorityView.as_view(), name='sort-notes-priority'),
    path('sort_notes/created_time/', views.SortNotesByCreatedTimeView.as_view(), name='sort-notes-created-time'),
    path('export/pdf/', views.exportNotes_to_pdf, name='exportNotes_pdf'),
    path('export/pdf/', views.exportNotes_to_csv, name='exportNotes_csv'),
    path('send_mail/', views.send_notesList_email, name='send_mail'),
    
]

