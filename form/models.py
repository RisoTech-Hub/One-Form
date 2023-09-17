from django.db.models import CASCADE, CharField, ForeignKey, JSONField, TextField
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Form(TimeStampedModel):
    name = CharField(_("Name"), max_length=128, blank=False, null=False)
    code = CharField(_("Code"), max_length=128, blank=False, null=False, unique=True)
    description = TextField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = "Form"
        verbose_name_plural = "Forms"
        db_table = "form_form"

    def __str__(self):
        return f"{self.name}"


class Submission(TimeStampedModel):
    form = ForeignKey(Form, related_name="submissions", on_delete=CASCADE)
    data = JSONField(_("Data"), default=dict, blank=True, null=True)

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"
        db_table = "form_submission"

    def __str__(self):
        return "{}: {} #{} {} {}".format(self.form.name, _("Submission with ID"), self.id, _("at"), self.created)
