from django.db import models

#https://docs.djangoproject.com/en/6.0/topics/db/examples/
#https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-types
# TODO: we need to add membership to words and letters, look at the many to many fields and add its own membership

# One user has one waffle
# One waffle has many words
# One word has many letters
# Many letters are in many words

class Waffle(models.Model):
  top_row_word = 
  middle_row_word = 
  bottom_row_word = 
  left_col_word = 
  middle_col_word = 
  right_col_word = 
  

class User(models.Model):
  waffle = models.OneToOneField(Waffle)
    

class Word(models.Model):
  correct_spelling = models.CharField(max_length=5)
  waffle = models.ForeignKey(Waffle, on_delete=models.CASCADE)
  current_letters = models.JSONField(default=list)


class Letter(models.Model):
  character = models.CharField(max_length=1)
  correct_place = models.BooleanField()
  in_word = models.BooleanField()
  word = models.ForeignKey(Word, on_delete=models.CASCADE)