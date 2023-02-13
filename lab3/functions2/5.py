movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def movie_category(movies, name_category):
    list = []
    for i in movies:
        curr_category = i['category']
        if name_category.lower() == curr_category.lower():
            list.append(i)
    return list

def avg_score(movies):
    total_score = 0
    total_movies = len(movies)
    for i in movies:
        total_score =total_score + i['imdb']
    avg_score = total_score/total_movies 
    return avg_score

def avg_score_of_category(movies, name_category):
    category_movies = movie_category(movies,name_category)
    category_avg = avg_score(category_movies)
    return category_avg
print('')
print('Average IMDB of movies in the Suspense catogory is: ')
print(avg_score_of_category(movies, 'Suspense'))
