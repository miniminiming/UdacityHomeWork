import media
import fresh_tomatoes

movie1 = media.Movie("Angry Bird","https://en.wikipedia.org/wiki/The_Angry_Birds_Movie#/media/File:The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=1U2DKKqxHgE")
movie2 = media.Movie("Storks","https://upload.wikimedia.org/wikipedia/en/1/13/Storks_%28film%29_poster_2.jpg","https://www.youtube.com/watch?v=ZVzL94jZNdU")
movie3 = media.Movie("Rio","https://upload.wikimedia.org/wikipedia/en/b/bb/Rio2011Poster.jpg","https://www.youtube.com/watch?v=Bf6zeRwk5LE")
movie4 = media.Movie("minions","https://en.wikipedia.org/wiki/Minions_(film)#/media/File:Minions_poster.jpg","https://www.youtube.com/watch?v=eisKxhjBnZ0")

movies =[movie1,movie2,movie3,movie4]

fresh_tomatoes.open_movies_page(movies)