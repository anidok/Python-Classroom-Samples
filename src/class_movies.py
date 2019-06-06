from datetime import date


# pylint: disable=too-many-instance-attributes
class Movie:
    # pylint: disable=too-many-arguments
    def __init__(self, name, rating, director, budget, description, actor: str = None, earnings: int = None, release_date: date = None):
        self.name = name
        self.rating = rating
        self.director = director
        self.budget = budget
        self.description = description
        self.actor = actor
        self.earnings = earnings

        release_date = date.today()
        self.release_date = release_date

    def good_movie(self):
        if self.rating >= 4:
            return"Good Movie"
        return "Average Movie"


TOY_STORY = Movie("ToyStory2", 4, "John Lasseter , Lee Unkrich , Ash Brannon", "90 millon USD",
                  "When Woody is toy-napped by a greedy toy collector and is nowhere to be found,\
                   \nBuzz and his friends set out to rescue him.\nBut Woody too is tempted by the idea of becoming immortal in a museum.")

print("Title : " + TOY_STORY.name)
print("Rating : " + str(TOY_STORY.rating))
print("Director : " + TOY_STORY.director)
print("Budget : " + str(TOY_STORY.budget))
print("Description :  " + TOY_STORY.description)
print("Comment: " + TOY_STORY.good_movie())
