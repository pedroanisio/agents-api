from django.db import models
import uuid
from .tag_model import Tag
from .rule_model import Rule
from .template_model import Template
from .instruction_model import Instruction
from django.utils.text import slugify


class Prompt(models.Model):
    """
    Represents a prompt entity in the application, capable of handling various output types 
    and governed by a set of rules and instructions.
    
    Attributes:
        uuid (UUIDField): A unique identifier for each prompt instance.
        name (CharField): A human-readable name for the prompt.
        rules (ManyToManyField): A collection of rules associated with the prompt.
        output_format (CharField): The format of output expected from the prompt, such as code, image, or free text.
        template (ForeignKey): A reference to a template that defines the structure or format of the prompt's output.
        instructions (ManyToManyField): A collection of instructions related to the prompt.
        created_at (DateTimeField): The date and time when the prompt instance was created.
        change_log (TextField): A log of changes made to the prompt instance.
        active (BooleanField): Indicates whether the prompt is currently active or inactive.
    """
    
    class OutputType(models.TextChoices):
        """Defines possible output types for a prompt."""
        ANIMATION = 'animation', 'Animation'
        AUDIO = 'audio', 'Audio'
        BOOLEAN = 'boolean', 'Boolean'
        CODE = 'code', 'Code'
        DOCUMENT = 'document', 'Document'
        FREE_TEXT = 'free_text', 'Free Text'
        GRAPH = 'graph', 'Graph'
        HTML = 'html', 'HTML'
        IMAGE = 'image', 'Image'
        IMAGE_SEQUENCE = 'image_sequence', 'Image Sequence'
        INTERACTIVE = 'interactive', 'Interactive'
        JSON = 'JSON', 'JSON'
        LINK = 'link', 'Link'
        LIST = 'list', 'List'
        MAP = 'map', 'Map'
        MARKDOWN = 'markdown', 'Markdown'
        MERMAID = 'mermaid', 'Mermeid'        
        QR_CODE = 'qr_code', 'QR Code'
        SCORE = 'score', 'Score'
        TABLE = 'table', 'Table'
        VIDEO = 'video', 'Video'
        XML = 'XML', 'XML'
        YAML = 'YAML', 'YAML'
    # You can continue to add more types as needed


    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='prompts', blank=True)
    content = models.CharField(max_length=255)               
    rules = models.ManyToManyField(Rule, related_name='prompts')
    output_format = models.CharField(max_length=50, choices=OutputType.choices)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, blank=True, null=True)
    instructions = models.ManyToManyField(Instruction, related_name='prompts')
    created_at = models.DateTimeField(auto_now_add=True)
    change_log = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """Returns the human-readable name of the prompt."""
        return self.name


    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically generate a slug from the rule's name
        if a slug is not explicitly provided. This ensures uniqueness and URL-friendliness
        of the slug field.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.slug:
            self.slug = slugify(self.name)  # Automatically generate slug from name
        super().save(*args, **kwargs)