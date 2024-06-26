from django import forms

from properties.models import Property
from crispy_forms.helper import FormHelper
from django.forms.widgets import HiddenInput
from .models import MaintenanceRequest, Worker
from django.forms import CheckboxSelectMultiple
from crispy_forms.layout import Layout, Field, Submit, Div, Row, HTML


class MaintenanceForm(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apt, staircase, etc.'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please describe the issue in detail so the contractor can come prepared.'}))
    class Meta:
        model = MaintenanceRequest
        fields = ['description', 'property', 'location', 'urgent']

    def __init__(self, *args, user=None, properties=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            if user.role == 3:
                self.fields['property'].queryset = Property.objects.filter(tenants=user)
            else:
                self.fields['property'].queryset = properties

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'maintenance-form'
        self.helper.form_show_errors = True
        self.helper.layout = Layout(
            Row(
                Div(
                    Field('property', css_class='form-control'),
                    css_class='col',
                ),
                Div(
                    Field('location', css_class='form-control'),
                    css_class='col',
                ),
            ),
            Field('description', css_class='form-control', rows=5),
            Field('urgent', css_class='form-control'),
            Submit('form', 'Save', css_class='btn btn-primary col-12 mt-1'),
            HTML('<small class="text-muted">* Contractor will contact you if needed for more information or scheduling visit.</small>')
        )


class EditMaintenanceForm(forms.ModelForm):
    STATUS = ((0, 'Submitted'), (3, 'Cancel'))
    STATUS_ALL= ((0, 'Submitted'), (1, 'In-progress'), (2, 'Completed'), (3, 'Cancel'))
    status = forms.ChoiceField(choices=STATUS_ALL, widget=forms.Select(attrs={'class': 'form-control'}),)
    contractor_note = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter any notes for the tenant.'}), required=False)
    scheduled_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    contractor = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = MaintenanceRequest
        fields = ['description', 'location', 'urgent', 'status', 'contractor_note', 'scheduled_date', 'contractor']
        css = {"all": ["form-control form-control-user"]}

    def __init__(self, *args, user=None, contractors=None, **kwargs):
        super().__init__(*args, **kwargs)
        if contractors is not None:
            self.fields['contractor'].queryset = contractors
        self.current_status = self.STATUS_ALL
        if user and (user.role == 3 ):
            self.current_status = self.STATUS
        self.fields['status'].widget.choices = self.current_status

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'maintenance-form'
        self.helper.form_show_errors = True

        if user and (user.role == 1 or user in contractors):
            self.helper.layout = self.contractor_fields()
        else:
            self.helper.layout = self.user_layout()


    def user_layout(self):
        self.fields['contractor'].widget = HiddenInput()
        return Layout(
            Field('contractor', css_class='hidden-description'),
            Field('description', css_class='form-control', rows=5),
            Field('location', css_class='form-control'),
            Row(
                Div(
                    Field('urgent', css_class='form-control'),
                    css_class='col',
                ),
                Div(
                    Field('status', css_class='form-control'),
                    css_class='col',
                ),
            ),
            Submit('form', 'Save', css_class='btn btn-primary col-12 mt-1'),
        )

    def contractor_fields(self):
        contractor_choices = [(contractor.pk, f"{contractor.first_name} {contractor.last_name}") for contractor in self.fields['contractor'].queryset]
        self.fields['contractor'].widget.choices = contractor_choices
        self.fields['description'].widget = HiddenInput()

        return Layout(
            HTML('<style>.hidden-description { display: none; }</style>'),
            Field('description', css_class='hidden-description'),
            Field('location', css_class='form-control'),
            Row(
                Div(
                    Field('urgent', css_class='form-control'),
                    css_class='col',
                ),
                Div(
                    Field('status', css_class='form-control'),
                    css_class='col',
                ),
            ),
            HTML('<hr>'),
            Field('contractor_note', css_class='form-control', rows=5),
            Row(
                Div(
                    Field('scheduled_date', css_class='form-control'),
                    css_class='col',
                ),
                Div(
                    Field('contractor', css_class='form-control'),
                    css_class='col',
                ),
            ),
            Row(
            Div(
                HTML('<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>')
            ),
            Div(
                Submit('form', 'Save', css_class='btn btn-primary col-12'),
        
            ),
            css_class='modal-footer'
            ),
            )


class WorkerCodeForm(forms.ModelForm):
    assigned_properties = forms.ModelMultipleChoiceField(
        queryset=Property.objects.all(), 
        widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    class Meta:
        model = Worker
        fields = ['code_name', 'assigned_properties']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['assigned_properties'].queryset = Property.objects.filter(landlord=user)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'worker-form'
        self.helper.form_show_errors = True
        self.helper.layout = Layout(
            Field('code_name', css_class='form-control'),
            Field('assigned_properties', css_class='form-control'),
            Submit('form', 'Create', css_class='btn btn-primary col-12 mt-1'),
        )
