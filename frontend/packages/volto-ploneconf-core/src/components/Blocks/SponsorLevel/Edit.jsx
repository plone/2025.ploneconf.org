import React from 'react';
import { withBlockExtensions } from '@plone/volto/helpers/Extensions';
import SidebarPortal from '@plone/volto/components/manage/Sidebar/SidebarPortal';

import SponsorLevelBlockData from './Data';
import SponsorLevelBlockView from './View';

const SponsorLevelBlockEdit = (props) => {
  const { data, onChangeBlock, block, selected } = props;
  return (
    <>
      <SponsorLevelBlockView {...props} isEditMode />
      <SidebarPortal selected={selected}>
        <SponsorLevelBlockData
          data={data}
          block={block}
          onChangeBlock={onChangeBlock}
        />
      </SidebarPortal>
    </>
  );
};

export default withBlockExtensions(SponsorLevelBlockEdit);
