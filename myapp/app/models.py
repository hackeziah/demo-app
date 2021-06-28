from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class TypeAnimal(BaseModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):    
        return f'{self.name}-{self.description}'
    


class Dog(BaseModel):
    name = models.CharField(max_length=100)
    type_animal = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):    
        return f'{self.name}-{self.type_animal}'


class Cat(BaseModel):
    name = models.CharField(max_length=100)
    type_animal = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):    
        return f'{self.name}-{self.type_animal}'


class Person(BaseModel):
    person = models.CharField(max_length=64)
    dog = models.ManyToManyField(Dog, blank=True)
    cat = models.ManyToManyField(Cat,  blank=True)

    def __str__(self):    
        return f'{self.person}'



