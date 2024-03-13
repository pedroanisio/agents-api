from django.db import models
import uuid
from django.utils.text import slugify

class Rule(models.Model):
    """
    Represents a rule entity within the application.

    This model stores information related to specific rules, including a unique
    identifier, name, slug, description, content, and creation timestamp. If a slug
    is not explicitly provided, it is automatically generated from the rule's name.

    Attributes:
        uuid (UUIDField): A unique identifier for the rule. It is not editable post-creation.
        name (CharField): The name of the rule.
        slug (SlugField): A URL-friendly slug derived from the rule's name. It is generated automatically if not provided.
        description (TextField): A detailed description of the rule.
        content (CharField): The core content or specifications of the rule.
        created_at (DateTimeField): The date and time when the rule was created.
    """
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField('prompt.Tag', related_name='rules', blank=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        """
        Returns the string representation of the Rule model, which is the name of the rule.

        Returns:
            str: The name of the rule.
        """
        return self.name
