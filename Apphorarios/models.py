from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    is_instructor = models.BooleanField('Es instructor',default=False)
    is_coordinador = models.BooleanField('Es coordinador',default=False)
    is_JGrupo = models.BooleanField('Es jefe de grupo',default=False)

class Ambientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    zona = models.CharField(max_length=50, blank=False, null=False)
    nombre_ambiente = models.CharField(max_length=50, blank=False, null=False)
    ZONA_FORMACION = (
        ('1', 'Zona 1'),
        ('2', 'Zona 2'),
        ('3', 'Zona 3'),
        ('5', 'Zona 5'),
    )
    zona = models.CharField(max_length=3, choices=ZONA_FORMACION, default='1')

    def __str__(self):
        return self.zona

class Fichas(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero = models.IntegerField(blank=False, null=False)
    jefe_ficha = models.CharField(max_length=50, blank=False, null=False)
    #fecha_inicio = models.DateField()
    #fecha_finalizacion = models.DateField()
    JORNADA = (
        ('M','mañana'),
        ('T','tarde'),
    )
    jornada_de_ficha = models.CharField(max_length=10,choices=JORNADA,default='M')
    trimestre_actual = models.IntegerField(blank=False, null=False)


class Trimestre1(models.Model):
    #id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    actividad = models.CharField(max_length=1500)
    nombre_competencia = models.CharField(max_length=1500)
    resultado_competencia = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre_competencia


class Trimestre2(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    actividad = models.CharField(max_length=1500)
    nombre_competencia = models.CharField(max_length=1500)
    resultado_competencia = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre_competencia

class Trimestre3(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    actividad = models.CharField(max_length=1500)
    nombre_competencia = models.CharField(max_length=1500)
    resultado_competencia = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre_competencia

class Trimestre4(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    actividad = models.CharField(max_length=1500)
    nombre_competencia = models.CharField(max_length=1500)
    resultado_competencia = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre_competencia

class Trimestre5(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    actividad = models.CharField(max_length=1500)
    nombre_competencia = models.CharField(max_length=1500)
    resultado_competencia = models.CharField(max_length=1500)
    
    def __str__(self):
        return self.nombre_competencia

class Trimestre6(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    actividad = models.CharField(max_length=1500)
    nombre_competencia = models.CharField(max_length=1500)
    resultado_competencia = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre_competencia

class Instructor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    TIPO_INSTRUCTOR = (
        ('TE', 'Tecnico'),
        ('TR', 'Transversal'),
        ('BI', 'Bilinguismo'),
    )
    tipo_instructor = models.CharField(max_length=3, choices=TIPO_INSTRUCTOR, default='TE')
    ambiente = models.OneToOneField(Ambientes, on_delete=models.CASCADE)
    fichas = models.ForeignKey(Fichas, on_delete=models.CASCADE)


    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellidos)