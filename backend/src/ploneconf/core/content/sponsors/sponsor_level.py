from plone.dexterity.content import Container
from zope.interface import Interface
from zope.interface import implementer


class ISponsorLevel(Interface):
    """Sponsorship Level."""


@implementer(ISponsorLevel)
class SponsorLevel(Container):
    """Convenience subclass for ``SponsorLevel`` portal type."""
