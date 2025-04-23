from plone.dexterity.interfaces import IDexterityFTI
from zope.component import queryUtility


def prepend_behavior(portal_type, behavior):
    fti = queryUtility(IDexterityFTI, name=portal_type)
    new = [
        currentbehavior
        for currentbehavior in fti.behaviors
        if currentbehavior != behavior
    ]
    new.insert(0, behavior)
    fti.behaviors = tuple(new)


def remove_behavior(portal_type, behavior):
    fti = queryUtility(IDexterityFTI, name=portal_type)
    if fti is not None:
        new = [
            currentbehavior
            for currentbehavior in fti.behaviors
            if currentbehavior != behavior
        ]
        fti.behaviors = tuple(new)
