# prompt/serializers.py
from rest_framework import serializers
from .models import Template, Prompt, Instruction, Rule, Tag

class PromptSerializer(serializers.ModelSerializer):
    rules_content = serializers.SerializerMethodField()
    instructions_content = serializers.SerializerMethodField()
    template_content = serializers.SerializerMethodField()
    tags_content = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = ['uuid', 'name', 'slug', 'description', 'content', 'output_format', 'created_at', 'change_log', 'active', 'template_content', 'rules_content', 'instructions_content', 'tags_content']

    def get_rules_content(self, obj):
        return [rule.content for rule in obj.rules.all()]

    def get_instructions_content(self, obj):
        return [instruction.content for instruction in obj.instructions.all()]
    
    def get_template_content(self, obj):
        return [obj.template.content]
    
    def get_tags_content(self, obj):
        return [tag.slug for tag in obj.tags.all()]

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
