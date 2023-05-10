# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django import forms

# |=========================================|
# |=====|     REFERENCIAS A MODELOS   |=====|
# |=========================================|
from .models import subfamily,family,gender,species,bee,sighting,field

# |=========================================|
# |=====|       BIBLIOTECAS EXTRA      |=====|
# |=========================================|
import requests
import apps.gallery.service as service
from decouple import config
# |=============================================================|
# |===============|       FORMULARIOS           |===============|
# |=============================================================|

# |=========================================|
# |=====| FORMULARIO DE SUBFAMILYFORM |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class SubfamilyForm(forms.ModelForm):
    class Meta:
        model = subfamily
        fields = [
            "subfamilyName",
        ]

# |=========================================|
# |=====|   FORMULARIO DE FAMILYFORM  |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class FamilyForm(forms.ModelForm):
    class Meta:
        model = family
        fields = [
            "familyName",
        ]

# |=========================================|
# |=====|   FORMULARIO DE GENDERFORM  |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class GenderForm(forms.ModelForm):
    class Meta:
        model = gender
        fields = [
            "genderName",
        ]

# |=========================================|
# |=====|  FORMULARIO DE SPECIESFORM  |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = species
        fields = [
            "speciesName",
        ]

# |=========================================|
# |=====|    FORMULARIO DE BEEFORM    |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class BeeForm(forms.ModelForm):
    class Meta:
        model = bee
        fields = [
            "beeName",
        ]

# |=========================================|
# |=====|  FORMULARIO DE SIGHTINGFORM |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|
#
# class SightingForm(forms.ModelForm):
#     # image = forms.FileField()
#
#     class Meta:
#         model = sighting
#         fields = [
#             "sighLat",
#             "sighLng",
#             "sighPicture",
#             "sighComment",
#         ]

class SightingForm(forms.ModelForm):
        # image = forms.FileField()
    class Meta:
        model = sighting
        fields = [
            "sighLat",
            "sighLng",
            "sighPicture",
            "sighComment",
            ]

    def save(self,picture,bee, commit=True):
        print('entre aquii')
        instance = super(SightingForm, self).save(commit=False)

        instance.sighLat = self.cleaned_data['sighLat']
        instance.sighLng = self.cleaned_data['sighLng']
        instance.sighComment = self.cleaned_data['sighComment']
        instance.sighApproved=False
        instance.sighBee = bee

        print('tambien aquii')


        imgUrl = service.postSighting(picture)
        instance.sighPicture = picture
        if commit:
            print('todo bien aquis')
            instance.save()
            print('tambien todo bien aquis')
    # class Meta:
    #     model = sighting
    #     fields = [
    #         "sighLat",
    #         "sighLng",
    #         "sighPicture",
    #         "sighComment",
    #     ]

# |=========================================|
# |=====|  FORMULARIO DE FIELDFORM    |=====|
# |=========================================|
# |=| Se da formato a cada uno de los     |=|
# |=| campos que se utilizarán.           |=|
# |=========================================|

class FieldForm(forms.ModelForm):
    class Meta:
        model = field
        fields = [
            "fieldsting",
            "fieldnative",
        ]