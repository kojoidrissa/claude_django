from django.db import models
from django.utils import timezone


class LightningTalk(models.Model):
    """Model to represent a Lightning Talk proposal."""
    
    # Speaker information
    speaker_name = models.CharField(
        max_length=200,
        help_text="Full name of the speaker"
    )
    
    email = models.EmailField(
        help_text="Contact email for the speaker"
    )
    
    # Talk information
    title = models.CharField(
        max_length=300,
        help_text="Title of the lightning talk"
    )
    
    # Optional: Add a description field for more details
    description = models.TextField(
        blank=True,
        help_text="Brief description of the talk (optional)"
    )
    
    # Acceptance status
    is_accepted = models.BooleanField(
        default=False,
        help_text="Whether the talk has been accepted"
    )
    
    # Timestamps (useful for tracking when proposals come in)
    submitted_at = models.DateTimeField(
        default=timezone.now,
        help_text="When the talk was proposed"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last time the proposal was updated"
    )
    
    # Optional: Track who reviewed/accepted the talk
    reviewed_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the talk was reviewed"
    )
    
    notes = models.TextField(
        blank=True,
        help_text="Internal notes about the proposal (not shown to speaker)"
    )
    
    class Meta:
        ordering = ['-submitted_at']  # Most recent proposals first
        verbose_name = "Lightning Talk"
        verbose_name_plural = "Lightning Talks"
    
    def __str__(self):
        """String representation for admin and debugging."""
        status = "✓ Accepted" if self.is_accepted else "⏳ Pending"
        return f"{self.title} by {self.speaker_name} [{status}]"
    
    def accept(self):
        """Helper method to accept a talk."""
        self.is_accepted = True
        self.reviewed_at = timezone.now()
        self.save()
    
    def reject(self):
        """Helper method to reject a talk."""
        self.is_accepted = False
        self.reviewed_at = timezone.now()
        self.save()