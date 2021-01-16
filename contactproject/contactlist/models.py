from django.db import models

# Information about the contacts
class Contact(models.Model):
    # create 4 attributes
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment = models.TextField()

    def to_string(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.comment