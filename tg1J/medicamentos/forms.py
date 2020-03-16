from django import forms
from medicamentos.models import Medicamento

class MedicamentoForm(forms.ModelForm):

    class Meta:
        model = Medicamento
        CHOICES = [('Rojo','Rojo'),('Amarillo', 'Amarillo'), ('Verde', 'Verde')]
        fields = [
                'nombre',
                'fecha_vencimiento',
                'fabricado_por',
                'registro_invima',
                'numero_lote',
                'presentacion_comercial',
                'forma_farmaceutica',
                'principio_activo',
                'unidad_medica',
                'porcentaje',
                'temperatura',
                'cantidad',
                'codigo',
        ]
        
        labels = {
                'Nombre': 'nombre',
                'Fecha Vencimiento': 'fecha_vencimiento',
                'Fabricado Por': 'fabricado_por',
                'Registro Invima': 'registro_invima',
                'Numero Lote': 'numero_lote',
                'Presentacion Comercial': 'presentacion_comercial',
                'Forma Farmaceutica': 'forma_farmaceutica',
                'Principio Activo': 'principio_activo',
                'Unidad Medica': 'unidad_medica',
                'Porcentaje': '%',
                'Temperatura': 'C°',
                'Cantidad': '0000...',
                'Codigo': '0000..',
        }

        widgets = {
                'Nombre':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'fecha_vencimiento':forms.DateInput(attrs={'class':'form-control  form-control-user', 'type':'date','id':'myDate','value':'aaaa-mm-dd'}),
                'Fabricado_por':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Registro_invima':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Numero_lote':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Presentacion_comercial':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Forma_farmaceutica':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Principio_activo':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Unidad_medica':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Porcentaje':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Temperatura':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
                'Cantidad':forms.TextInput(attrs={'class':'form-control form-control-medicamentor'}),
                'Codigo':forms.TextInput(attrs={'class':'form-control form-control-medicamento'}),
        }

