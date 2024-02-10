from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Movie


def movie_list(request):
    rating_filter = request.GET.get('rating_filter', '')
    release_date_filter = request.GET.get('release_date_filter', '')
    movie_type_filter = request.GET.get('movie_type_filter', '')
    director_filter = request.GET.get('director_filter', '')
    search_query = request.GET.get('txt', '')

    movies = Movie.objects.filter(release_date__lte=timezone.now())
    movie_type = Movie.objects.values_list('movie_type__name', flat=True).distinct()
    director = Movie.objects.values_list('director__last_name', flat=True).distinct()

    movies = movies.order_by('-imdb_rating')
    movies = movies.filter(title__icontains=search_query)

    context = {
        'movies': movies,
        'movie_types': movie_type,
        'directors': director,
        'selected_movie_type': movie_type_filter,
        'selected_director': director_filter,
        'selected_rating': rating_filter,
        'selected_release_date': release_date_filter,
        'search_query': search_query,
    }

    return render(request, 'blog/movie_list.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'blog/movie_detail.html', {'movie': movie})


def about_us(request):
    return render(request, 'blog/about_us.html')
