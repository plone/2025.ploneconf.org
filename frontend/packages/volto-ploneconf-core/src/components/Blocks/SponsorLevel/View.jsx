import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers/Extensions';
import SponsorLevelView from './DefaultView';

const SponsorLevelBlockView = (props) => {
  return <SponsorLevelView {...props} />;
};

export default withBlockExtensions(SponsorLevelBlockView);
