import django_filters
from django.db.models import Q

from peering_manager.filtersets import (
    ChangeLoggedModelFilterSet,
    OrganisationalModelFilterSet,
    PeeringManagerModelFilterSet,
)
from utils.filters import ContentTypeFilter

from .models import Contact, ContactAssignment, ContactRole, Email

__all__ = (
    "ContactFilterSet",
    "ContactRoleFilterSet",
    "ContactAssignmentFilterSet",
    "EmailFilterSet",
)


class ContactRoleFilterSet(OrganisationalModelFilterSet):
    class Meta:
        model = ContactRole
        fields = ["id", "name", "slug"]


class ContactFilterSet(PeeringManagerModelFilterSet):
    class Meta:
        model = Contact
        fields = ["id", "name", "title", "phone", "email", "address"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)
            | Q(title__icontains=value)
            | Q(phone__icontains=value)
            | Q(email__icontains=value)
            | Q(address__icontains=value)
            | Q(comments__icontains=value)
        )


class ContactAssignmentFilterSet(ChangeLoggedModelFilterSet):
    content_type = ContentTypeFilter()
    contact_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Contact.objects.all(), label="Contact (ID)"
    )
    role_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ContactRole.objects.all(), label="Contact role (ID)"
    )
    role = django_filters.ModelMultipleChoiceFilter(
        field_name="role__slug",
        queryset=ContactRole.objects.all(),
        to_field_name="slug",
        label="Contact role (slug)",
    )

    class Meta:
        model = ContactAssignment
        fields = ["id", "content_type_id", "object_id"]


class EmailFilterSet(PeeringManagerModelFilterSet):
    class Meta:
        model = Email
        fields = ["id", "jinja2_trim", "jinja2_lstrip"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)
            | Q(subject__icontains=value)
            | Q(template__icontains=value)
        )
