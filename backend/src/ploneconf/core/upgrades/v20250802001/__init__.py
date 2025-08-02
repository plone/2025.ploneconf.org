from pathlib import Path
from plone import api
from ploneconf.core import logger
from ploneconf.core.setuphandlers.initial import create_example_content
from Products.GenericSetup.tool import SetupTool


BASE_PATH = Path(__file__).parent


def remove_sponsors_db(setup_tool: SetupTool):
    """Remove the old sponsors db."""
    logger.info("Remove /sponsors")
    pasta = api.content.get(path="/sponsors")
    api.content.delete(pasta, check_linkintegrity=False)
    logger.info("SponsorsDB at /sponsors removed")


def remove_schedule(setup_tool: SetupTool):
    """Remove /schedule."""
    logger.info("Remove /scheduke")
    pasta = api.content.get(path="/schedule")
    api.content.delete(pasta, check_linkintegrity=False)
    logger.info("Page /schedume removed")


def configure_techevent(setup_tool: SetupTool):
    """Configure techevent."""
    create_example_content(setup_tool)
    logger.info("Update example content")
