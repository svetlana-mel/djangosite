from django.db import models

class Age(models.Model):
    value = models.CharField(max_length=50)
    comment = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Возрастные категории'
        verbose_name = 'Возрастная категория'
        ordering = ['value']

class Groups(models.Model):
    value = models.CharField(max_length=50)
    comment = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = ['value']

class Types(models.Model):
    value = models.CharField(max_length=50)
    comment = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = 'Типы'
        verbose_name = 'Тип'
        ordering = ['value']

class Organizers(models.Model):
    value = models.CharField(max_length=256)
    comment = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name_plural = 'Организаторы'
        verbose_name = 'Организатор'
        ordering = ['value']
    


class Events(models.Model):
    name = models.CharField(max_length=254)
    date = models.DateField(db_index=True)
    town = models.CharField(max_length=50)
    # ============= many-to-many relations ==============
    groups = models.ManyToManyField(Groups)
    age = models.ManyToManyField(Age)
    types = models.ManyToManyField(Types)
    organizers = models.ManyToManyField(Organizers)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Соревнования'
        verbose_name = 'Соревнование'
        ordering = ['date']


class Participants(models.Model):
    fname = models.CharField(max_length=254)
    lname = models.CharField(max_length=254)
    registered = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')
    email = models.EmailField()
    event = models.ForeignKey('Events', null=False, on_delete=models.PROTECT, db_index=True, verbose_name='Мероприятие')
    groups = models.ManyToManyField(Groups)
    age = models.ManyToManyField(Age)
    types = models.ManyToManyField(Types)

    class Meta:
        verbose_name_plural = 'Участники'
        verbose_name = 'Участник'
        ordering = ['registered']  

