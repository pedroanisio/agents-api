from django.db import models
import uuid
from .rule_model import Rule
from .template_model import Template
from .instruction_model import Instruction

class Prompt(models.Model):
    """
    Represents a prompt entity in the application, capable of handling various output types 
    and governed by a set of rules and instructions.
    
    Attributes:
        uuid (UUIDField): A unique identifier for each prompt instance.
        name (CharField): A human-readable name for the prompt.
        rules (ManyToManyField): A collection of rules associated with the prompt.
        output_type (CharField): The type of output expected from the prompt, such as code, image, or free text.
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
        JSON = 'json', 'JSON'
        LINK = 'link', 'Link'
        LIST = 'list', 'List'
        MAP = 'map', 'Map'
        MARKDOWN = 'markdown', 'Markdown'
        MERMAID = 'mermaid', 'Mermeid'        
        QR_CODE = 'qr_code', 'QR Code'
        SCORE = 'score', 'Score'
        TABLE = 'table', 'Table'
        VIDEO = 'video', 'Video'
        XML = 'xml', 'XML'
        YAML = 'yaml', 'YAML'
    # You can continue to add more types as needed


    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()    
    content = models.CharField(max_length=255)               
    rules = models.ManyToManyField(Rule, related_name='prompts')
    output_type = models.CharField(max_length=50, choices=OutputType.choices)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    instructions = models.ManyToManyField(Instruction, related_name='prompts')
    created_at = models.DateTimeField(auto_now_add=True)
    change_log = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        """Returns the human-readable name of the prompt."""
        return self.name
