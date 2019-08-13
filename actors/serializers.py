
from rest_framework.serializers import ModelSerializer
from .models import *

class PersonasSerializer(ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'

class TiposAutenticacionesSerializer(ModelSerializer):
    class Meta:
        model = TiposAutenticaciones
        fields = '__all__'

class AuditoriaUsuariosSerializer(ModelSerializer):
    class Meta:
        model = AuditoriaUsuarios
        fields = '__all__'   

class RecetasSerializer(ModelSerializer):
    class Meta:
        model = Recetas
        fields = '__all__'

class EstadosSerializer(ModelSerializer):
    class Meta:
        model = Estados
        fields = '__all__'

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'        
class DetallePromocionSerializer(ModelSerializer):
    class Meta:
        model = DetallePromocion
        fields = '__all__'

class FarmaciasSerializer(ModelSerializer):
    class Meta:
        model = Farmacias
        fields = '__all__'

class BancosSerializer(ModelSerializer):
    class Meta:
        model = Bancos
        fields = '__all__'

class TipoNCSerializer(ModelSerializer):
    class Meta:
        model = TipoNC
        fields = '__all__'

class NotasdeCreditoSerializer(ModelSerializer):
    class Meta:
        model = NotasdeCredito
        fields = '__all__'

class CuponesSerializer(ModelSerializer):
    class Meta:
        model = Cupones
        fields = '__all__'

class DetalleCuponSerializer(ModelSerializer):
    class Meta:
        model = DetalleCupon
        fields = '__all__'

class AuditoriaCuponSerializer(ModelSerializer):
    class Meta:
        model = AuditoriaCupon
        fields = '__all__'

class InventarioSerializer(ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'