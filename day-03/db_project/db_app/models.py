from django.db import models


# this class is a model which connects to the database
class WordDefinition(models.Model):
    # each attribute we define will be a column in the db

    # CharField means that word will be short text
    word = models.CharField(unique=True, max_length=50)
    # unique means it must be unique in the db
    # max_length means it can only be 50 characters at most

    # TextField is for longer text
    definition = models.TextField()
    use = models.TextField()

    # null=True and blank=True allow this to be null in the DB
    phonetics = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.word}"


class WordExample(models.Model):
    content = models.TextField()
    # ForeignKey will associate this model to another model
    # this model will "belong" to the other model and the other model "has many" of this one
    word = models.ForeignKey(WordDefinition, on_delete=models.CASCADE, related_name="examples")
    # the first argument is the model it belongs to
    # on_delete determines if we delete this if it's "parent" gets deleted
    # related_name determines what the "parent" calls its "children"


class Category(models.Model):
    name = models.CharField()
    # many to many means a category can have many words and words can have many categories
    words = models.ManyToManyField(WordDefinition, blank=True, related_name="categories")



# running CRUD commands via `python manage.py shell`:

# READ ##########################################

# WordDefinition.objects.all() 
#   ---> returns a QuerySet (list) with all word definitions

# WordDefinition.objects.get(word="bagel") 
#   ---> returns a single item if it exists OR a DoesNotExist error


# CREATE ########################################

# my_word = WordDefinition(word="something", definition="something", use="something")
# my_word.save()


# UPDATE ########################################

# my_word.use = "something else"
# my_word.save()


# DELETE / DESTROY ##############################

# my_word.delete()