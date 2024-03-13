# prompt/admin.py

from django.contrib import admin
from .models import Prompt, Rule, Template, Instruction, Tag

# Define admin classes for each model
class PromptAdmin(admin.ModelAdmin):
    list_display = ['name', 'output_format', 'display_tags', 'created_at']
    search_fields = ['name', 'output_format', 'created_at']
    list_filter = ['created_at', 'active']

    def display_tags(self, obj):
            """Creates a string for the Tags. This is required because list_display cannot directly display ManyToManyFields."""
            return ', '.join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

class RuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_tags', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['created_at']

    def display_tags(self, obj):
            """Creates a string for the Tags. This is required because list_display cannot directly display ManyToManyFields."""
            return ', '.join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['created_at']

class InstructionAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_tags', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['created_at']

    def display_tags(self, obj):
            """Creates a string for the Tags. This is required because list_display cannot directly display ManyToManyFields."""
            return ', '.join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['created_at']

# Register the models with their respective admin classes
admin.site.register(Prompt, PromptAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Instruction, InstructionAdmin)
admin.site.register(Tag, TagAdmin)