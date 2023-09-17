from rest_framework.viewsets import ModelViewSet

from ..models import Form, Submission
from .serializers import FormSerializer, SubmissionSerializer


class FormViewSet(ModelViewSet):
    serializer_class = FormSerializer
    queryset = Form.objects.all()


class SubmissionViewSet(ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
