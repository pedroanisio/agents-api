# prompt/views.py
from rest_framework import viewsets
from .models import Template, Prompt, Instruction, Rule
from .serializers import TemplateSerializer, PromptSerializer, InstructionSerializer, RuleSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
