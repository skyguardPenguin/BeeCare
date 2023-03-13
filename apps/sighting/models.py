# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|


from django.db import models
# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|


# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|
import datetime
from uuid import uuid4
import os
from pathlib import Path
from apps.member.models import member
from beecare import settings
# |=============================================================|
# |===============|           MODELOS           |===============|
# |=============================================================|

# |=========================================|
# |========|     MODELO FAMILY      |=======|
# |=========================================|

class family (models.Model):
    familyName = models.CharField(max_length=80)
    def __str__(self):
        return self.familyName

# |=========================================|
# |========|    MODELO SUBFAMILY    |=======|
# |=========================================|

class subfamily (models.Model):
    subfamilyName = models.CharField(max_length=80)
    subfamilyFamily = models.ForeignKey(family,on_delete=models.CASCADE)
    def __str__(self):
        return self.subfamilyName

# |=========================================|
# |========|     MODELO GENDER      |=======|
# |=========================================|

class gender (models.Model):
    genderName = models.CharField(max_length=80)
    def __str__(self):
        return self.genderName

# |=========================================|
# |========|     MODELO SPECIES     |=======|
# |=========================================|
class species (models.Model):
    speciesName = models.CharField(max_length=80)
    def __str__(self):
        return self.speciesName

# |=========================================|
# |========|  MODELO BEE (species,  |=======|
# |=========================================|
# |========|   subfamily,family)    |=======|
# |=========================================|

class bee (models.Model):
    beeName = models.CharField(max_length=64)
    beeSpecies = models.ForeignKey(species,on_delete=models.CASCADE)
    beeSubfamily = models.ForeignKey(subfamily,on_delete=models.CASCADE)
    beeGender = models.ForeignKey(gender,on_delete=models.CASCADE)
    def __str__(self):
        return self.beeName
    
# |=| Método antiguo para guardar imagenes de los |=|
# |=| avistamientos realizados por los            |=|
# |=| miembros (cloudinary)                       |=|

# def get_img_sighting(instance,filename):
#     extension = Path(filename).suffix
#     return 'Sightings/sighting_%s/sight.%s' % (instance.sighMember,extension)


# |=| Método actual para guardar imagenes de los  |=|
# |=| avistamientos realizados por los            |=|
# |=| miembros (cloudinary)                       |=|
def get_img_sighting(instance,filename):
    extension = Path(filename).suffix
    today = datetime.datetime.now()
    year = today.strftime("%Y/")
    month = today.strftime("%m/")
    day = today.strftime("%d/")
    time = today.strftime("%H%M%S")
    uuid = uuid4().hex
    route = '%s/%s/%s' % (year,month, day)
    return 'Sightings/%s/%s_%s_%s%s' % (route,instance.sighBee,uuid,time,extension)




# |=========================================|
# |========| MODELO SIGHTING (memb) |=======|
# |=========================================|
####
class sighting (models.Model):
    sighLat = models.DecimalField(max_digits=32,decimal_places=16, blank=True,null=True)
    sighLng = models.DecimalField(max_digits=32,decimal_places=16, blank=True, null=True)
    sighPicture = models.ImageField(upload_to=get_img_sighting,blank=True)
    sighComment = models.CharField(max_length=1024)
    sighDate = models.DateTimeField(auto_now_add=True,auto_now=False)
    sighApproved = models.BooleanField(default=False)
    sighBee = models.ForeignKey(
        bee,
        on_delete=models.CASCADE,
        null=False
        )
    sighMember = models.ForeignKey(member,on_delete=models.CASCADE)
    migrationTest = models.BooleanField(default=True)
    migrationTest2 = models.BooleanField(default=True)
    def __str__(self):
        return "%s %s" % (self.sighDate,self.sighApproved)