/**
 * Sponsors block.
 * @module components/Blocks/Sponsors/View
 */

import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getNavroot } from '@plone/volto/actions/navroot/navroot';
import { hasApiExpander } from '@plone/volto/helpers/Utils/Utils';
import { getBaseUrl, flattenToAppURL } from '@plone/volto/helpers/Url/Url';
import { withBlockExtensions } from '@plone/volto/helpers/Extensions';
import Sponsors from '../../Sponsors/Sponsors';
/**
 * View document block class.
 * @class View
 * @extends Component
 */
const View = (props) => {
  const { properties } = props;
  const dispatch = useDispatch();
  const pathname = properties.pathname;
  const navroot = useSelector((state) => state.navroot?.data?.navroot?.['@id']);
  useEffect(() => {
    if (!hasApiExpander('navroot', getBaseUrl(pathname))) {
      dispatch(getNavroot(getBaseUrl(pathname)));
    }
  }, [dispatch, pathname]);
  return (
    <div className="block sponsorsBlock">
      {navroot && <Sponsors navRoot={flattenToAppURL(navroot)} />}
    </div>
  );
};

export default withBlockExtensions(View);
