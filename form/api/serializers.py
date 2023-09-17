from rest_framework.serializers import ModelSerializer

from ..models import Form, Submission


class FormSerializer(ModelSerializer[Form]):
    class Meta:
        model = Form
        fields = ["id", "name", "code", "description"]


class SubmissionSerializer(ModelSerializer[Submission]):
    class Meta:
        model = Submission
        fields = ["id", "form", "data"]
