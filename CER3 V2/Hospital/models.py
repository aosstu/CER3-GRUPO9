from django.db import models
from django.contrib.auth.models import User
import time,datetime
class Bebe(models.Model):
    current_date = datetime.date.today()
    t =time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    madre = models.ForeignKey(User, null=True,blank=True,editable=True,to_field="username",on_delete=models.PROTECT,default='SIN MADRE',related_name='%(class)s_madre')
    padre = models.ForeignKey(User, null=True,blank=True,editable=True,to_field="username",on_delete=models.PROTECT,default='SIN PADRE',related_name='%(class)s_padre')
    choices=(('Masculino','Masculino'),('Femenino','Femenino'))
    sexo = models.CharField(max_length=20,choices=choices,blank=True,editable=True)
    nombre = models.CharField(max_length=20, default="SIN NOMBRE",blank=True,editable=True)
    apellido_paterno   = models.CharField(max_length=30, default="SIN APELLIDO",blank=True,editable=True)
    apellido_materno   =models.CharField(max_length=30,default="SIN APELLIDO",blank=True,editable=True)
    fecha_nacimiento   =models.DateField(default=current_date,blank=True,editable=True)
    hora_nacimiento    =models.TimeField(default=current_time,blank=True,editable=True)
    peso               =models.PositiveSmallIntegerField(default=1,blank=True,editable=True)
    talla              =models.FloatField(default=1.0,blank=True,editable=True)
    def __str__(self) :
        texto = "{0} {1} {2}"
        return texto.format(self.nombre,self.apellido_paterno,self.apellido_materno)
    
        
# Create your models here.
class AvanceDiario(models.Model):
    peso=models.PositiveSmallIntegerField(default=1,blank=True,editable=True)
    tolerancia_choices=(('Buena','Buena'),('Mala','Mala'),('Regular','Regular'))
    tolerancia=models.CharField(max_length=7,null=True,blank=True,editable=True,default='Regular',choices=tolerancia_choices)
    unidad_choices=(('UCI','UCI'),('UTI','UTI'))
    unidad =models.CharField(max_length=3,null=True,blank=True,editable=True,default='EN CAMBIO',choices=unidad_choices)
    cama = models.IntegerField(null=True,blank=True,editable=True,default=1)
    sino_choices = (('Si','Si'),('No','No'))
    orina=models.CharField(max_length=2,null=True,blank=True,editable=True,default='Si',choices=sino_choices)
    deposiciones = models.CharField(max_length=2,null=True,blank=True,editable=True,default='Si',choices=sino_choices)
    bebe = models.ForeignKey(Bebe, null=True,blank=True,editable=True,on_delete=models.PROTECT)
    current_date = datetime.date.today()
    fecha   =models.DateField(default=current_date,blank=True,editable=True)
    
    def __str__(self):
        return 'AvanceDiario '+self.bebe
    