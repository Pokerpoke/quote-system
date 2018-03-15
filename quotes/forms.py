from django import forms


class AddQuoteForm(forms.Form):
    """
    添加报价单
    """
    project_num = forms.IntegerField(
        required=True,
        label=u'项目编号',
        error_messages={'required': u'请输入项目编号'},
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'项目编号',
            }
        )
    )
    amount = forms.IntegerField(
        required=True,
        label=u'数量',
        error_messages={'required': u'请输入数量'},
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'数量',
            }
        )
    )
    unit_price = forms.IntegerField(
        required=True,
        label=u'单价',
        error_messages={'required': u'请输入单价'},
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'单价',
            }
        )
    )
