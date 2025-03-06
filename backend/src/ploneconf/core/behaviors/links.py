from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from ploneconf.core import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ILinkInformation(model.Schema):
    """Plone Conference Link Information."""

    model.fieldset(
        "links",
        label=_("Links"),
        fields=[
            "remoteUrl",
            "twitter",
            "bluesky",
            "github",
            "mastodon",
            "instagram",
            "linkedin",
            "youtube",
            "facebook",
        ],
    )

    remoteUrl = schema.URI(
        title=_("Site"),
        description=_("Link to site"),
        required=False,
    )

    twitter = schema.URI(
        title=_("X"),
        description=_("X profile url"),
        required=False,
    )
    bluesky = schema.URI(
        title=_("Bluesky"),
        description=_("Bluesky profile url"),
        required=False,
    )

    github = schema.URI(
        title=_("GitHub"),
        description=_("GitHub profile url"),
        required=False,
    )

    mastodon = schema.URI(
        title=_("Mastodon"),
        description=_("Mastodon profile url"),
        required=False,
    )

    instagram = schema.URI(
        title=_("Instagram"),
        description=_("Instagram profile url"),
        required=False,
    )

    linkedin = schema.URI(
        title=_("LinkedIn"),
        description=_("LinkedIn profile url"),
        required=False,
    )

    youtube = schema.URI(
        title=_("YouTube"),
        description=_("YouTube channel url"),
        required=False,
    )

    facebook = schema.URI(
        title=_("Facebook"),
        description=_("Facebook page url"),
        required=False,
    )
