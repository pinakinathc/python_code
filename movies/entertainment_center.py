import media
import fresh_tomatoes

toy_story=media.Movie(
	"Toy Story",
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

#print (toy_story.storyline)
avatar=media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/bO/Avatar-Teaser-Poster.jpg",
	"http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailor()
school_of_rock=media.Movie(
	"Schools of Rock",
	"Using rock music to learn",
	"http://upload.wikipedia.org/wikipedia/en/1/11/School_of_Rock_poster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille=media.Movie(
	"Ratatouille",
	"A rat is a chef in Paris",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris=media.Movie(
	"Midnight in PAris",
	"Going back in time to meet authors",
	"http://upload.wikimedia.org/wikipedia/em/9/9f/Midnight_in_paris_Poster.jpg",
	"https://www.youtube.com/watch?v=atLg2wQQxuU")

hunger_games=media.Movie(
	"Hunger Games",
	"A really real reality show",
	"http://upload.wikimedia.org/wikipedia/en/4/42/Hunger-GamesPoster.jpg",
	"https://www.youtube.com/watch?v=PbA63a7HObo")	

movies=[toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
#fresh_tomatoes.open_movies_page(movies)	
#print (media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
