from django.db import models
from django.forms import Textarea

from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fieldset_tuple)

from .model_admin_mixin import ModelAdminMixin
from ..admin_site import contract_admin
from ..forms import CommunicationSkillsForm
from ..models import CommunicationSkills


@admin.register(CommunicationSkills, site=contract_admin)
class CommunicationSkillsAdmin(
        ModelAdminMixin, admin.ModelAdmin):

    form = CommunicationSkillsForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 5,
                   'cols': 50,
                   'style': 'height: 3em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'emp_identifier',
                'contract',
            )}),
        ('Communication Skills', {
            'fields': (
                'communication_skills_desc',
                'communication_skills',
                'communication_skills_comm',
            )
        }),
        audit_fieldset_tuple)

    def get_readonly_fields(self, request, obj=None):
        return ['communication_skills_desc', ]
