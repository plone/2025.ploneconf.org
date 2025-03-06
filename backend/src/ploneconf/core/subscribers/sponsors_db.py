from plone import api
from ploneconf.core import logger
from ploneconf.core.content.sponsors.sponsors_db import SponsorsDB
from zope.lifecycleevent import ObjectAddedEvent


ADD_PERMISSION = "ploneconf.core: Add SponsorsDB"


def sponsors_db_add(content: SponsorsDB, event: ObjectAddedEvent):
    """Restrict permission to add a SponsorsDB."""
    site = api.portal.get()
    site.manage_permission(ADD_PERMISSION, [], acquire=False)
    logger.info(f"Remove permissão {ADD_PERMISSION} em {content.absolute_url()}")
