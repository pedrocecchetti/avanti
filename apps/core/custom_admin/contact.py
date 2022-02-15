from django.contrib.auth.admin import UserAdmin

from ..forms.user import UserCreateForm, UserUpdateForm


class ContactAdmin(UserAdmin):
    # The forms to add and change user instances
    empty_value_display = "----"

    readonly_fields = ["subject", "name", "email", "message", "created_at"]

    # The fields to be used in displaying the User model.
    list_display = (
        "name",
        "email",
        "created_at",
        "is_answered"
    )
    list_filter = (
        "is_answered",

    )

    # The fields to be used in updates on User model.
    fieldsets = (
        (
            "Informações básicas",
            {
                "classes": ("grp-collapse grp-open",),
                "fields": (("name", "email", "person_responsible", "is_answered")),
            },
        ),
        ("mensagem", { "fields": ("subject", "message",)}),
    )

    ordering = ("created_at",)
    filter_horizontal = ()