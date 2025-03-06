// SemanticUI-free pre-@plone/components
import React from 'react';
import { FormattedMessage, defineMessages, useIntl } from 'react-intl';
import { useSelector, shallowEqual } from 'react-redux';
import { useLocation } from 'react-router-dom';
import { Container } from '@plone/components';
import SlotRenderer from '@plone/volto/components/theme/SlotRenderer/SlotRenderer';
import FooterLinks from '@kitconcept/volto-light-theme/components/Footer/FooterLinks';
import SocialNetworksLinks from '@plonegovbr/volto-network-block/components/FooterLinks/FooterLinks';

const messages = defineMessages({
  copyright: {
    id: 'Copyright',
    defaultMessage: 'Copyright',
  },
});

const Footer = () => {
  const intl = useIntl();
  const {
    content,
    lang,
    siteActions = [],
  } = useSelector(
    (state) => ({
      lang: state.intl.locale,
      siteActions: state.actions?.actions?.site_actions,
      content: state.content.data,
    }),
    shallowEqual,
  );
  const location = useLocation();
  const navroot = useSelector((state) => state.navroot.data.navroot);
  const footerLinks = navroot?.footer_links;

  return (
    <footer id="footer">
      <SlotRenderer name="preFooter" content={content} location={location} />

      <Container className="footer">
        <div className="footer-message">
          <FormattedMessage
            id="The {plonecms} is {copyright} 2000-{current_year} by the {plonefoundation} and friends."
            defaultMessage="The {plonecms} is {copyright} 2000-{current_year} by the {plonefoundation} and friends."
            values={{
              plonecms: (
                <FormattedMessage
                  id="Plone{reg} Open Source CMS/WCM"
                  defaultMessage="Plone{reg} Open Source CMS/WCM"
                  values={{ reg: <sup>®</sup> }}
                />
              ),
              copyright: (
                <abbr title={intl.formatMessage(messages.copyright)}>©</abbr>
              ),
              current_year: new Date().getFullYear(),
              plonefoundation: (
                <a className="item" href="http://plone.org/foundation">
                  <FormattedMessage
                    id="Plone Foundation"
                    defaultMessage="Plone Foundation"
                  />
                </a>
              ),
            }}
          />{' '}
          <br />
          <FormattedMessage
            id="Distributed under the {license}."
            defaultMessage="Distributed under the {license}."
            values={{
              license: (
                <a
                  className="item"
                  href="http://creativecommons.org/licenses/GPL/2.0/"
                >
                  <FormattedMessage
                    id="GNU GPL license"
                    defaultMessage="GNU GPL license"
                  />
                </a>
              ),
            }}
          />
        </div>
        <FooterLinks
          links={footerLinks}
          siteActions={siteActions}
          lang={lang}
        />
        <SocialNetworksLinks />
      </Container>
      <SlotRenderer name="postFooter" content={content} location={location} />
    </footer>
  );
};

export default Footer;
