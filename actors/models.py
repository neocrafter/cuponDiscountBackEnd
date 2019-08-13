
from django.db import models

# Create your models here.
class Personas(models.Model):
    ID = models.IntegerField(default = 1,primary_key = True)
    PRIMERNOMBRE = models.CharField(max_length = 20)
    SEGUNDONOMBRE = models.CharField(max_length = 20)
    APELLIDOS = models.CharField(max_length = 40)
    CEDULA = models.CharField(max_length = 15)
    TELEFONO = models.CharField(max_length = 25)
    DIRECCION = models.CharField(max_length = 25)
    GENERO = models.CharField(max_length = 25)
    FECHANACIMIENTO = models.DateField()
    CORREO = models.EmailField(max_length = 100, unique = True)
    VERIFICACIONCORREO = models.BooleanField(default = False)
    FOTOPERFIL = models.CharField(max_length = 25)

class TiposAutenticaciones(models.Model):
    TIPO = models.CharField(max_length = 20)

class Usuarios(models.Model):
    PERSONA = models.ForeignKey(Personas, on_delete = models.CASCADE)
    AUTENTICACION = models.ForeignKey(TiposAutenticaciones, on_delete = models.CASCADE)
    USERNAME = models.CharField(max_length = 25)
    PASSWORD = models.CharField(max_length = 25)
    FECHACREACION = models.DateField()
    ESTADO = models.BooleanField(default = False)


class AuditoriaUsuarios(models.Model):
    USUARIO = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    ULTIMASESION = models.DateField()
    FECHAAUDITORIA = models.DateField()
    ESTATUS = models.CharField(max_length = 25)
    ACCION = models.CharField(max_length = 25)

class Promocion(models.Model):
    FECHACREACION = models.DateField()
    DESCRIPCION = models.CharField(max_length = 250)
    ESTATUS = models.BooleanField(default = False)
    FECHAVIGENCIA = models.DateField()

class Recetas(models.Model):
    SEGUNDONOMBRE = models.ForeignKey(Promocion, on_delete = models.CASCADE)
    FOTORECETA = models.CharField(max_length = 100)
    FECHAFOTO = models.DateField()
    
class Estados(models.Model):
    NOMBRE = models.CharField(max_length = 50)
    TIPO = models.CharField(max_length = 50)
    DESCRIPCION = models.CharField(max_length = 50)

class Productos(models.Model):
    DESCRIPCION = models.CharField(max_length = 75)

class DetallePromocion(models.Model):
    PROMOCION = models.ForeignKey(Promocion, on_delete = models.CASCADE)
    PRODUCTO = models.ForeignKey(Productos, on_delete = models.CASCADE)

class Farmacias(models.Model):
    NOMBRE = models.CharField(max_length = 100)
    DIRECCION = models.CharField(max_length = 100)

class Bancos(models.Model):
    NOMBRE = models.CharField(max_length = 50)
    DIRECCION = models.CharField(max_length = 50)
    TELEFONO = models.CharField(max_length = 50)

class TipoNC(models.Model):
    TIPO = models.CharField(max_length = 50)
    DESCRIPCION = models.CharField(max_length = 50)

class NotasdeCredito(models.Model):
    PROMOCION = models.OneToOneField(Promocion, on_delete = models.CASCADE)
    BANCO = models.OneToOneField(Bancos, on_delete = models.CASCADE)
    FARMACIA = models.OneToOneField(Farmacias, on_delete = models.CASCADE)
    TIPONC = models.OneToOneField(TipoNC, on_delete = models.CASCADE)
    FECHANC = models.DateField()
    MONTO = models.IntegerField()

class Cupones(models.Model):
    PERSONA = models.OneToOneField(Personas, on_delete = models.CASCADE)
    ESTADO = models.OneToOneField(Estados, on_delete = models.CASCADE)
    RECETA = models.OneToOneField(Recetas, on_delete = models.CASCADE)
    FARMACIA = models.OneToOneField(Farmacias, on_delete = models.CASCADE)
    NOTACREDITO = models.ForeignKey(NotasdeCredito, on_delete = models.CASCADE)
    FECHACUPON = models.DateField()
    DESCRIPCION = models.CharField(max_length = 100)

class DetalleCupon(models.Model):
    PRODUCTO = models.ForeignKey(Productos, on_delete = models.CASCADE)
    DESCUENTO = models.IntegerField()

class AuditoriaCupon(models.Model):
    CUPON = models.ForeignKey(Cupones, on_delete = models.CASCADE)
    ESTADO = models.OneToOneField(Estados, on_delete = models.CASCADE)
    USUARIO = models.OneToOneField(Usuarios, on_delete = models.CASCADE)
    FECHAESTADO = models.DateField()
    DESCRIPCION = models.CharField(max_length = 50)

class Inventario(models.Model):
    PROMOCION = models.OneToOneField(Promocion, on_delete = models.CASCADE)
    PRODUCTO = models.OneToOneField(Productos, on_delete = models.CASCADE)
    CANTIDAD = models.IntegerField()