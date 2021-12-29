from django.urls import path
from todo import views as tutorials_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', tutorials_views.index, name='home'),
    path('', tutorials_views.index.as_view(), name='home'),
    path('api/tutorials/', tutorials_views.tutorial_list),
    path('api/tutorials/<int:pk>/', tutorials_views.tutorial_detail),
    path('api/todo/complete/', tutorials_views.todo_list_complete)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)