from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    #평균점수 높은순
    movies = sorted(movies, key=lambda m: m.average_score(), reverse=True)
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        score = int(request.POST['score'])
        Rating.objects.create(movie=movie, score=score)
        return redirect('movies:movie_ressult', pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_result(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_result.html', {'movie':movie})

def movie_rate(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        score = int(request.POST['score'])
        Rating.objects.create(movie=movie, score=score)
        return redirect('movies:movie_result', pk=pk)
    return render(request, 'movies/movie_rate.html', {'movie': movie})
