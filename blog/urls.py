from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('about_us/', views.about_us, name='about_us'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)