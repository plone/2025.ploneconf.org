from plone.dexterity.content import Container
from zope.interface import Interface
from zope.interface import implementer


class ISponsorsDB(Interface):
    """Plone Conference Sponsors Database."""


@implementer(ISponsorsDB)
class SponsorsDB(Container):
    """Convenience subclass for ``SponsorsDB`` portal type."""
