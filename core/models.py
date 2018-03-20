from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name = "Название", max_length=64, blank=True, null=True, default=None)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.TextField(verbose_name = "Описание", blank=True, null=False, default=None)
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class Table(models.Model):
    number = models.IntegerField(verbose_name = "Номер",default=None, blank=True)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    number_of_guests = models.IntegerField(verbose_name = "Количество персон",default=None,)

    def __str__(self):
        return "%s" % (self.number)

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

class Doctor(models.Model):
    name =  models.CharField(verbose_name = "Имя",max_length=64, blank=False,)
    patronomic = models.CharField(verbose_name = "Отчество",max_length=64,blank=True,)
    surname = models.CharField(verbose_name = "Фамилия", max_length=64, )
    specialization = models.CharField(verbose_name = "Специализация", max_length=64)
    room = models.IntegerField(verbose_name = "Кабинет",default=None)

    def __str__(self):
        return "%s.%s.%s" %(self.surname, self.name[0:1:1], self.patronomic[0:1:1])

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

class Room(models.Model):
    number = models.IntegerField(verbose_name = "Номер",default=None, blank=True)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    number_of_bed = models.IntegerField(verbose_name = "Количество мест",default=None,choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ), blank=True)
    shower =  models.CharField (verbose_name = "Душ", max_length= 3, choices = (
        ("Yes" , "Да"),
        ("No", "Нет"),
    ), default=None, blank=True,)
    category = models.CharField (verbose_name = "Тип номера", max_length= 10, choices = (
        ("Lux" , "Люкс"),
        ("Half_Lux", "Полулюкс"),
        ("Standart", "Стандарт"),
        ("Econom", "Эконом"),
    ), default=None, blank=True,)

    def __str__(self):
        return "%s" % (self.number)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

class Guest(models.Model):
    name =  models.CharField(verbose_name = "Имя",max_length=64, blank=False,)
    patronomic = models.CharField(verbose_name = "Отчество",max_length=64,blank=True,)
    surname = models.CharField(verbose_name = "Фамилия", max_length=64, )
    age = models.IntegerField(verbose_name = "Возраст",default=0)
    sex = models.CharField (verbose_name = "Пол", max_length= 6, choices = (
        ("Male" , "Мужской"),
        ("Female", "Женский"),
    ), default=None, )
    category = models.ForeignKey(Category,verbose_name = "Категория",  null=True, default=None, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,verbose_name = "Комната",  null=True, default=None, on_delete=models.CASCADE)
    table = models.ForeignKey(Table,verbose_name = "Стол",  null=True, default=None, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor,verbose_name = "Врачи", help_text="Выберите врачей для постояльца.")
    data_arrival = models.DateTimeField(verbose_name="Дата приезда", auto_now=False, auto_now_add=False,blank=True, null=True, default=None)
    data_departure = models.DateTimeField(verbose_name="Дата отъезда", auto_now=False, auto_now_add=False, blank=True,null=True, default=None)
    def __str__(self):
        return "%s.%s.%s" %(self.surname, self.name[0:1:1], self.patronomic[0:1:1])

    class Meta:
        verbose_name = "Постоялеца"
        verbose_name_plural = "Постояльцы"
