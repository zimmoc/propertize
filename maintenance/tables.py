import django_tables2 as tables
from .models import MaintenanceRequest
from properties.models import Property

class MaintenanceRequestTable(tables.Table):
    property_name = tables.Column(verbose_name='Property', accessor='property.name')
    full_name = tables.Column(verbose_name='Full Name', accessor='submitted_by', order_by=('submitted_by__first_name', 'submitted_by__last_name'))
    contractor = tables.Column(verbose_name='Contractor', accessor='contractor.first_name')
    location = tables.Column(verbose_name='Location')
    open = tables.TemplateColumn("<a class='text-dark profile-btn' href='{% url 'maintenance_request' request_id=record.request_id %}'><i class='fa fa-cog'></i></a>", verbose_name='')

    class Meta:
        model = MaintenanceRequest
        orderable = True
        attrs = {
            "class": "table table-hover",
            'thead': {"class": ""}
            }
        fields = ("open", "status", "property_name", "full_name", "contractor", "request_date", "location")
    
    def render_full_name(self, record):
        return f"{record.submitted_by.first_name} {record.submitted_by.last_name}"