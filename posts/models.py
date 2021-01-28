""" Archivo que genera los modelos con clases
Generacion de los campos de la base de dato usando django en lugar de sql
"""
#Django
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

    #RelationShip Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    #otra forma de hacerlo seria colocar solo Profile e importar el modelo 


    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)
        #la primer variable es por que esta en la misma clase
        #la segunda variable es por que viene de la llamada viene desde la clase User 
        # donde el parametro username ya esta definido 
