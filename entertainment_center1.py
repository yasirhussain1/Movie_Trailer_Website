import media  # imports media.py file
import fresh_tomatoes


# creating Movie class instances


wfe = media.Movie("Water For Elephant",
                  "tragedy forces him to leave school",
                  """http://waterforelephantsfilm.com/wp-content/
uploads/2010/12/robertpattinsonwfetrailer.jpg""",
                  "https://www.youtube.com/watch?v=d0DbfQaentM")

gits = media.Movie("Ghost In The Shell",
                   "Major is the first of her kind",
                   """https://s-media-cache-ak0.pinimg.com/
originals/01/2e/8c/012e8ce9e49ab74c2838ca55c1f3e5f5.jpg""",
                   "https://www.youtube.com/watch?v=G4VmJcZR0Yg")

ksi = media.Movie("Kong:Skull Island",
                  """Scientists, soldiers and adventurers unite to
explore a mythical, uncharted island in the Pacific Ocean""",
                  """https://encrypted-tbn0.gstatic.com/images?q=tbn
:ANd9GcSUt3ngGzMEsyzL2K2ZRuMGq0CE-oa4o6oz4W4A4x22DOKt-7AsOw""",
                  "https://www.youtube.com/watch?v=AP0-9FBs2Rs")

ds = media.Movie("Doctor Strange",
                 "Dr Strange's life changes after a car accident.",
                 """http://www.impawards.com/2016/posters/
doctor_strange_ver8_xlg.jpg""",
                 "https://www.youtube.com/watch?v=HSzx-zryEgM")

ti = media.Movie("Three Idiots",
                 "Two friends looking for a lost buddy.",
                 """http://media2.intoday.in/indiatoday/
images/stories/3-idiots_650_012714113147.jpg""",
                 "https://www.youtube.com/watch?v=K0eDlFX9GMc")

u3 = media.Movie("Undisputed 3",
                 "A champion fighter gets transferred to a Ukrainian",
                 """http://www.gstatic.com/tv/thumb/dvdboxart/8090118
/p8090118_d_v8_aa.jpg""",
                 "https://www.youtube.com/watch?v=5tTduaZZI-s")

rh = media.Movie("Rush Hour",
                 "When a Chinese diplomat's daughter is kidnapped in LA.",
                 """https://images-na.ssl-images-amazon.com/images/
I/51%2BHfsxTM5L._SY450_.jpg""",
                 "https://www.youtube.com/watch?v=UuHf24GhINc")

zoo = media.Movie("Zootopia",
                  """From the largest elephant to the smallest shrew,
the city of Zootopia is a mammal metropolis.""",
                  """http://s3.amazonaws.com/kidzworld_photo/images/2016517/02e944eb
-f9a2-4504-822b-7a9da63df96f/zootopia-blu-ray.jpg""",
                  "https://www.youtube.com/watch?v=jWM0ct-OLsM")

# storing the movie instances in a list


movies = [wfe, gits, ksi, ds, ti, u3, rh, zoo]


# following function accepts list as an argument
fresh_tomatoes.open_movies_page(movies)
