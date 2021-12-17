from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    is_instructor = models.BooleanField('Es instructor',default=False)
    is_coordinador = models.BooleanField('Es coordinador',default=False)
    is_JGrupo = models.BooleanField('Es jefe de grupo',default=False)

class Ambientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_ambiente = models.CharField(max_length=50, blank=False, null=False)
    ZONA_FORMACION = (
        ('Zona 1', '1'),
        ('Zona 2', '2'),
        ('Zona 3', '3'),
        ('Zona 5', '5'),
    )
    zona = models.CharField(max_length=10, choices=ZONA_FORMACION, default='Zona 1')

    def __str__(self):
        return self.zona

class Fichas(models.Model):
    id = models.BigAutoField(primary_key=True)
    PROGRAMA_DE_FORMACION =(
        ('ADSI', 'Analisis y desarrollo de sistemas de informacion'),
        ('ADSO', 'Analisis y desarrollo de software'),
    )
    programa_de_formacion = models.CharField(max_length=1500, choices=PROGRAMA_DE_FORMACION, default='ADSI')
    numero = models.CharField(max_length=50)
    jefe_ficha = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    #fecha_finalizacion = models.DateField()
    JORNADA = (
        ('M','mañana'),
        ('T','tarde'),
    )
    jornada_de_ficha = models.CharField(max_length=10,choices=JORNADA,default='M')
    #trimestre_actual = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.numero

class Instructor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    PROGRAMA_DE_FORMACION =(
        ('ADSI', 'Analisis y desarrollo de sistemas de informacion'),
    )
    programa_de_formacion = models.CharField(max_length=10, choices=PROGRAMA_DE_FORMACION, default='ADSI')
    TIPO_INSTRUCTOR = (
        ('TE', 'Tecnico'),
        ('TR', 'Transversal'),
        ('BI', 'Bilinguismo'),
    )
    tipo_instructor = models.CharField(max_length=3, choices=TIPO_INSTRUCTOR, default='TE')
    '''ambiente = models.OneToOneField(Ambientes, on_delete=models.CASCADE)'''
    '''fichas = models.ForeignKey(Fichas, on_delete=models.CASCADE)'''

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellidos)


class Trimestres(models.Model):
    TRIMESTRES = (
        ('T1', 'Trimestre 1'),
        ('T2', 'Trimestre 2'),
        ('T3', 'Trimestre 3'),
        ('T4', 'Trimestre 4'),
        ('T5', 'Trimestre 5'),
        ('T6', 'Trimestre 6'),
    )
    trimestres = models.CharField(max_length=3, choices=TRIMESTRES, default='T1')

    def __str__(self):
        return self.trimestres

class Actividad(models.Model):
    id_actividad= models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre_actividad

class Competencia_aprendizaje(models.Model):
    id_competencia = models.AutoField(primary_key=True)
    nombre_competencia = models.CharField(max_length=1500)
    codigo = models.IntegerField()

    def __str__(self):
        return self.nombre_competencia

class Resultado_aprendizaje(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    nombre_resultado = models.CharField(max_length=1500)
    competencia = models.ForeignKey(Competencia_aprendizaje, on_delete=models.CASCADE)
    trimestres = models.ForeignKey(Trimestres, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_resultado

class Filtros(models.Model):
    id_resultado = models.IntegerField()
    nombre_resultado = models.CharField(max_length=1500)
    actividad_id = models.IntegerField()
    competencia_id = models.IntegerField()
    trimestres_id = models.BigIntegerField()
    id_competencia = models.IntegerField()
    nombre_competencia = models.CharField(max_length=1500)
    codigo = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    trimestres = models.CharField(max_length=3)
    id_actividad = models.IntegerField()
    nombre_actividad = models.CharField(max_length=1500)

    class Meta:
        managed = False
        db_table = 'filtros'