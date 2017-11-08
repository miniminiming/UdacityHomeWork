import media
import fresh_tomatoes

movie1 = media.Movie("Angry Bird",
                     "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1510118511&di=8e0fc4a16dcf0edf4f203e15317baa30&src=http://www.91danji.com/upload/201142/20114214513580.jpg",
                     "https://www.youtube.com/watch?v=1U2DKKqxHgE")
movie2 = media.Movie("Storks",
                     "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1510128641760&di=fdecf86bd94913fa809e567dc897217f&imgtype=0&src=http%3A%2F%2Fimg1.gtimg.com%2Fent%2Fpics%2Fhv1%2F189%2F225%2F2107%2F137065239.jpg",
                     "https://www.youtube.com/watch?v=ZVzL94jZNdU")
movie3 = media.Movie("Rio",
                     "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1510128743968&di=59170aef952975ab9ab86021067bbb8e&imgtype=0&src=http%3A%2F%2Fimg.25pp.com%2Fuploadfile%2Fapp%2Ficon%2F20160731%2F1469966124489411.jpg",
                     "https://www.youtube.com/watch?v=Bf6zeRwk5LE")
movie4 = media.Movie("minions",
                     "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3568029076,2951212495&fm=27&gp=0.jpg",
                     "https://www.youtube.com/watch?v=eisKxhjBnZ0")

movies = [movie1, movie2, movie3, movie4]

fresh_tomatoes.open_movies_page(movies)
