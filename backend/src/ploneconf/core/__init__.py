"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "20250919.1"

PACKAGE_NAME = "ploneconf.core"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
