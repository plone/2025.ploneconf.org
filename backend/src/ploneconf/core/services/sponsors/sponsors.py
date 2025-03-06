from collections import defaultdict
from plone import api
from plone.restapi.interfaces import ISerializeToJsonSummary
from plone.restapi.services import Service
from ploneconf.core.utils import sponsor_levels
from typing import Any
from zope.component import getMultiAdapter


class Get(Service):
    """list Sponsors by level."""

    def _serialize_brain(self, brain) -> dict[str, Any]:
        obj = brain.getObject()
        return getMultiAdapter((obj, self.request), ISerializeToJsonSummary)()

    def get_sponsors(self) -> dict[str, list[dict[str, str]]]:
        """Return all published sponsors, grouped by level."""
        response = defaultdict(list)
        context = self.context
        results = api.content.find(
            context,
            portal_type="Sponsor",
            review_state="published",
            sort_on="getObjPositionInParent",
        )
        for brain in results:
            response[brain.level].append(self._serialize_brain(brain))
        return response

    def reply(self) -> dict[str, list[dict]]:
        """Published sponsors, grouped by level.

        :returns: Sponsors grouped by level.
        """
        all_sponsors = self.get_sponsors()
        levels = []
        for key, title, url in sponsor_levels(self.context):
            sponsors = all_sponsors.get(key, [])
            if sponsors:
                levels.append({
                    "@id": url,
                    "id": key,
                    "title": title,
                    "items": sponsors,
                })
        return {
            "levels": levels,
        }
