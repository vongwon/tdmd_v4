import requests
import pprint
import json
from django.conf import settings
from django.shortcuts import render, redirect
from .models import AllGenres
import pandas as pd

def index(request):
    movies = []

    if request.method == "POST":
        search_url = 'https://api.themoviedb.org/3/search/movie'

        search_params ={
            'query': request.POST['searchtitles'],
            'api_key': settings.TMDB_DATA_API_KEY,
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['results']

        for result in results:
            movie_data ={
                'title' : result['title'],
                'id' : result['id'],
                'thumbnail' : f'https://image.tmdb.org/t/p/w500/{result["poster_path"]}',
                'released': result['release_date'],
                'url' : f'moviedetails'
            }

            movies.append(movie_data)

    context = {
        'movies' : movies
    }
    return render(request, 'apiapp/index.html', context)

def moviedetails(request):
    movies_details = []

    if request.method == "POST":
        movie_id = request.POST['searchid']
        search_url = 'https://api.themoviedb.org/3/movie/' + movie_id

        search_params = {
            'api_key': settings.TMDB_DATA_API_KEY,
        }

        r = requests.get(search_url, params=search_params)

        movie_details_results = r.json()

        pprint.pprint(movie_details_results)

        movie_details_data = {
            'title': movie_details_results['title'],
            'tmdb_id': movie_details_results['id'],
            'thumbnail': f'https://image.tmdb.org/t/p/w500/{movie_details_results["poster_path"]}',
            'released': movie_details_results['release_date'],
            'runtime': movie_details_results['runtime'],
            'overview': movie_details_results['overview'],
            'imdb_id': movie_details_results['imdb_id'],
            #'genres_ids': movie_details_results['genres']['id'],


        }

        movies_details.append(movie_details_data)
        print(movies_details)

    detailcontext = {
        'movies_details': movies_details
    }
    #print(context)
    return render(request, 'apiapp/moviedetails.html', detailcontext)

def addgenre(request):
    genres = []
    api_key = settings.TMDB_DATA_API_KEY
    responseGenre = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key='
                                 + api_key)
    genreResponse = responseGenre.json()  # store parsed json response
    genreList = genreResponse['genres']

    d = []
    e = []

    # masukan genre film ke list
    indeks = 0
    while (indeks < len(genreList)):
        d.append(genreList[indeks]['id'])
        e.append(genreList[indeks]['name'])
        indeks += 1

    genreDF = pd.DataFrame(zip(d, e), columns=['genre_tmdb_id', 'genre_name'])
    genreDF.to_csv('genres_03.csv')
    #genreDF.to_dict(AllGenres)

    genrescontext = {
        'genres': genres
    }
    # print(context)
    return render(request, 'apiapp/genre.html', genrescontext)