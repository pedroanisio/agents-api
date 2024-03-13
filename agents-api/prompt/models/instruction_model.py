from django.db import models
import uuid
from django.utils.text import slugify

class Instruction(models.Model):
    """
    Represents an instruction entity in the application.

    Each instruction includes a name, slug, description, content, and a timestamp 
    for when it was created. Slugs are automatically generated from the first 50 
    characters of the description if not explicitly provided.

    Attributes:
        uuid (UUIDField): The unique identifier for the instruction, not editable.
        name (CharField): The name of the instruction.
        slug (SlugField): A slug for the instruction, auto-generated from the description if blank.
        description (TextField): A detailed description of the instruction.
        content (CharField): The content or body of the instruction.
        created_at (DateTimeField): The timestamp when the instruction instance was created.
    """
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)    
    description = models.TextField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Overwrites the default save method to automatically generate a slug
        from the first 50 characters of the description if a slug is not provided.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.slug:
            self.slug = slugify(self.description[:50])  # Generate slug from the first 50 characters of description
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the Instruction, showcasing the
        first 50 characters of its description.

        Returns:
            str: A substring of the instruction's description limited to 50 characters.
        """
        return self.description[:50]  # Return the first 50 characters of description
