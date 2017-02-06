from django import forms
from .models import Teleconsultor,Solicitante,Solicitacao


#classes below

class TeleconsultorForm(forms.ModelForm):

    class Meta:
        model = Teleconsultor
        fields = ('Nome','Email','CRM','DataFormatura')


class SolicitanteForm(forms.ModelForm):

    class Meta:
        model = Solicitante
        fields = ('Nome','CPF','Email','Telefone')


class SolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = ('Texto','solicitante')
