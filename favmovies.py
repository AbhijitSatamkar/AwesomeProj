import fresh_tomatoes
import moviesite

Iron_Man=moviesite.Movies("Iron Man(2008)","Sci_Fi Movie","img/Ironman.JPG","https://www.youtube.com/watch?v=8hYlB38asDY")
ratatouille=moviesite.Movies("Ratatouille","Animation","https://projectedrealities.files.wordpress.com/2014/01/ratatouillec.jpg","https://www.youtube.com/watch?v=bKedSHDpkvI")
schindler_list=moviesite.Movies("Schindler's List","WWII movie",
                                "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                                "https://www.youtube.com/watch?v=JdRGC-w9syA")

movies=[Iron_Man,ratatouille,schindler_list]

fresh_tomatoes.open_movies_page(movies)

#Iron_Man.show_trailer()