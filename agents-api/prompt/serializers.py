# prompt/serializers.py
from rest_framework import serializers
from .models import Template, Prompt, Instruction, Rule

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = '__all__'

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'
