from plone.app.iterate.interfaces import IWCContainerLocator
from ploneconf.core import _
from Products.CMFCore.interfaces import IDynamicType
from Products.CMFCore.utils import getToolByName
from zope.component import adapter
from zope.interface import implementer

import plone.restapi.services.workingcopy.create


plone.restapi.services.workingcopy.create.WC_LOCATION_MODE = "membrane"


@implementer(IWCContainerLocator)
@adapter(IDynamicType)
class MembraneUserObjectLocator:
    def __init__(self, context):
        self.context = context

    title = _("Membrane user locator")

    @property
    def available(self):
        return self() is not None

    def __call__(self):
        membership = getToolByName(self.context, "portal_membership")
        user = membership.getAuthenticatedMember()
        membrane_tool = getToolByName(self.context, "membrane_tool")
        return membrane_tool.getUserObject(user_id=user.getId())
