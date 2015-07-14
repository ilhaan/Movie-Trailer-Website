import media #Import 'Movie()' class
import fresh_tomatoes #Imported for open_movies_page() function

#Instances of the class 'Movie()' are created below for the seven movies selected for this project

dark_knight = media.Movie("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.", "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", "https://www.youtube.com/watch?v=yQ5U8suTUw0", "2008")

furious_7 = media.Movie("Furious 7", "Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.", "http://t1.gstatic.com/images?q=tbn:ANd9GcReedjA2vJSO4_6GDpsI3PShvbRqfAAEv03qaJ9qOxtiLZX0Jx7", "https://www.youtube.com/watch?v=yISKeT6sDOg", "2015")

spiderman = media.Movie("Spider-Man", "When bitten by a genetically modified spider, a nerdy, shy, and awkward high school student gains spider-like abilities that he eventually must use to fight evil as a superhero after tragedy befalls his family.", "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg", "https://www.youtube.com/watch?v=O7zvehDxttM", "2002")

primal_fear = media.Movie("Primal Fear", "An altar boy is accused of murdering a priest, and the truth is buried several layers deep.", "https://upload.wikimedia.org/wikipedia/en/f/f7/Primal_Fear.jpg", "https://www.youtube.com/watch?v=PnmTi7hSjrA", "1996")

rush_hour = media.Movie("Rush Hour", "Two cops team up to get back a kidnapped daughter.", "https://upload.wikimedia.org/wikipedia/en/5/55/Rush_hour_ver2.jpg", "https://www.youtube.com/watch?v=JMiFsFQcFLE", "1998")

terminator = media.Movie("The Terminator", "A human-looking indestructible cyborg is sent from 2029 to 1984 to assassinate a waitress, whose unborn son will lead humanity in a war against the machines, while a soldier from that war is sent to protect her at all costs.", "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg", "https://www.youtube.com/watch?v=lHz95RYUbik", "1984")

iron_man = media.Movie("Iron Man", "After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight evil.", "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", "https://www.youtube.com/watch?v=KAE5ymVLmZg", "2008")

#A list of the of all the instances created above
movies = [dark_knight, furious_7, spiderman, primal_fear, rush_hour, terminator, iron_man]

#List of movies is passed to open_movies_page() functon in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
