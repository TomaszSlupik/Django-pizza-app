from django.db import models

class Pizza (models.Model):

    nazwa = models.CharField(max_length=20, null=True, blank=True)
    skladniki = models.TextField(default="")
    cena = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    zdjecie =models.ImageField (upload_to='foty', null=True, blank=True)


def __str__(self):
    return self.nazwa()

def nazwa (self):
    return "{}".format(self.nazwa)


