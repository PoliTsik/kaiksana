from django.contrib import admin
from .models import Actor, MovieType, Director, Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director', 'get_actors', 'movie_type', 'release_date',
                    'imdb_url', 'image', 'imdb_rating', 'my_rating', 'summary')

    def get_actors(self, obj):
        return ", ".join([actor.name for actor in obj.stars.all()])
    get_actors.short_description = 'Stars'

admin.site.register(Actor)
admin.site.register(MovieType)
admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
