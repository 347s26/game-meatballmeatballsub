from django.db import models

#https://docs.djangoproject.com/en/6.0/topics/db/examples/
#https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-types
# TODO: we need to add membership to words and letters, look at the many to many fields and add its own membership

# One user has one waffle
# One waffle has one of each word in a specific position
# One word has many letters
# Many letters are in many words

class Waffle(models.Model):
  # think about on_delete
  top_row_word = models.OneToOneField('Word', on_delete=models.DO_NOTHING)
  middle_row_word = models.OneToOneField('Word', on_delete=models.DO_NOTHING)
  bottom_row_word = models.OneToOneField('Word', on_delete=models.DO_NOTHING)
  left_col_word = models.OneToOneField('Word', on_delete=models.DO_NOTHING)
  middle_col_word = models.OneToOneField('Word', on_delete=models.DO_NOTHING)
  right_col_word = models.OneToOneField('Word', on_delete=models.DO_NOTHING)
  num_turns_left = models.IntegerField()

class User(models.Model):
  waffle = models.OneToOneField(Waffle)
    


# We need a foreign key for the many to one relationship between words and letters
# Words can only have one letter per index, letters can be in multiple words
# After much math we added foreign key to word
class Word(models.Model):
  correct_spelling = models.CharField(max_length=5)
  letter1 = models.ForeignKey('Letter', on_delete=models.CASCADE)
  letter2 = models.ForeignKey('Letter', on_delete=models.CASCADE)
  letter3 = models.ForeignKey('Letter', on_delete=models.CASCADE)
  letter4 = models.ForeignKey('Letter', on_delete=models.CASCADE)
  letter5 = models.ForeignKey('Letter', on_delete=models.CASCADE)


class Letter(models.Model):
  character = models.CharField(max_length=1)
  correct_place = models.BooleanField()
  in_word = models.BooleanField()