from plone import api
from ploneconf.core.upgrades import prepend_behavior
from ploneconf.core.upgrades import remove_behavior


def update_to_vlt_site_customizations_fields(setup_tool):
    update_site_customizations_fields_data(setup_tool)
    replace_custom_behavior_with_vlt_behaviors(setup_tool)


def update_site_customizations_fields_data(setup_tool):
    """Update the site customizations fields data.
    It will only update the `footer_links` and `footer_logos` fields
    in the Plone site.
    It's given as helper function to be used in the upgrade step in case you have it
    in other locations.
    """
    portal = api.portal.get()

    for field in ["footer_links", "footer_logos"]:
        if not hasattr(portal, field):
            continue

        if (
            isinstance(getattr(portal, field, False), dict)
            and "blocks_layout" in getattr(portal, field, False)
            and "items" in getattr(portal, field, False)["blocks_layout"]
        ):
            resultant_items = []
            for item_id in getattr(portal, field, False)["blocks_layout"]["items"]:
                item = getattr(portal, field, False)["blocks"][item_id]
                item["@id"] = item_id
                resultant_items.append(item)
            setattr(portal, field, resultant_items)

        # Set default if the field is empty
        if isinstance(getattr(portal, field, False), dict):
            setattr(portal, field, [])


def replace_custom_behavior_with_vlt_behaviors(setup_tool):
    remove_behavior("Plone Site", "ploneconf.core.sitecustomization")
    prepend_behavior("Plone Site", "voltolighttheme.footer")
    prepend_behavior("Plone Site", "voltolighttheme.theme")
    prepend_behavior("Plone Site", "voltolighttheme.header")
