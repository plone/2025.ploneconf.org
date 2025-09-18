from Acquisition import aq_base
from plone import api
from Products.CMFCore.utils import getToolByName


def install_dependencies(context):
    """Upgrade step to install upgrade step dependencies."""
    setup_tool = api.portal.get_tool("portal_setup")
    setup_tool.runAllImportStepsFromProfile(
        "profile-collective.techevent.users:default", purge_old=False
    )
    setup_tool.runAllImportStepsFromProfile(
        "profile-plone.app.iterate:default", purge_old=False
    )


def move_workflow_history(context):
    """Move worklflow history from old to new workflow."""
    pc = api.portal.get_tool("portal_catalog")
    from_id = "simple_publication_workflow"
    to_id = "iterated_publication_workflow"
    portal_type = ["Keynote", "Presenter", "Talk"]
    brains = pc.unrestrictedSearchResults(portal_type=portal_type)
    for brain in brains:
        obj = brain._unrestrictedGetObject()
        history = getattr(aq_base(obj), "workflow_history", {}) or {}
        if from_id in history:
            history[to_id] = history.pop(from_id)


def update_role_mappings(context):
    """Update permissions after workflow changes."""
    portal = api.portal.get()
    wf_tool = api.portal.get_tool("portal_workflow")
    wf_tool._recursiveUpdateRoleMappings(
        portal,
        {
            "iterated_publication_workflow": wf_tool.getWorkflowById(
                "iterated_publication_workflow"
            )
        },
    )


def update_attendees_permissions(context):
    """Update attendees container permission to allow working copies."""
    pc = api.portal.get_tool("portal_catalog")
    brains = pc.unrestrictedSearchResults(portal_type="Attendees")
    for brain in brains:
        obj = brain._unrestrictedGetObject()
        default_roles = ["Manager", "Site Administrator", "Owner", "Contributor"]
        permissions = [
            "collective.techevent: Add Talk",
            "collective.techevent: Add Keynote",
        ]
        for permission in permissions:
            obj.manage_permission(
                permission,
                roles=default_roles,
                acquire=False,
            )
