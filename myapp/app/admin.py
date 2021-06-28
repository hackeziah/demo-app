from django.contrib import admin
from app.models import TypeAnimal, Cat, Dog, Person


@admin.register(TypeAnimal)
class TypeAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Type Animanal', {
            'fields' : ('name', 'description'),
        }),
    ]

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Dog Information', {
            'fields' : ('name', 'age', 'type_animal'),
        }),
    ]

    formfield_querysets = {
        'type_animal': lambda: TypeAnimal.objects.all(),
    }

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('get_name_with_age', 'type_animal')
    list_per_page = 10
    ordering = ('-created_at', )
    readonly_fields = ('get_name_with_age', ) 
    fieldsets = [
        ('Cat Information', {
            'fields' : ('name', 'age', 'type_animal'),
        }),
    ]

    formfield_querysets = {
        'type_animal': lambda: TypeAnimal.objects.all(),
    }
    
    def get_name_with_age(self, obj):
        return f'{obj.name} - {obj.age}'
    get_name_with_age.short_description = "Name and Age"
    

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('person', 'created_at', 'updated_at',)
    list_per_page = 10
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fieldsets = [
        ('Information', {
            'fields' : ('person', 'dog', 'cat'),
        }),
    ]

    formfield_querysets = {
        'dog': lambda: Dog.objects.all(),
        'cat': lambda: Cat.objects.all(),
    }

