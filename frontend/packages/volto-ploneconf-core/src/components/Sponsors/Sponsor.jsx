/**
 * Sponsor container.
 * @module components/Sponsors/Sponsor
 */
import React from 'react';
import { UniversalLink } from '@plone/volto/components/manage/UniversalLink/UniversalLink';
import { flattenToAppURL } from '@plone/volto/helpers/Url/Url';

const SponsorLogo = ({ content }) => {
  const hasImage = content?.image ? true : false;
  const imageSrc = hasImage
    ? content.image.download
    : `${content['@id']}/${content.image_scales.image[0].download}`;
  return (
    <img
      title={content.title}
      alt={content.title}
      src={flattenToAppURL(imageSrc)}
    />
  );
};

/**
 * Sponsor function.
 * @function Sponsor
 * @returns {JSX.Element} Markup of the a Sponsor option.
 */
const Sponsor = ({ content }) => {
  const sponsorId = content.id;
  const level = content.level;
  return (
    <div id={sponsorId} className={`sponsor ${level}`}>
      <UniversalLink href={flattenToAppURL(content['@id'])}>
        <SponsorLogo content={content} />
      </UniversalLink>
    </div>
  );
};

export default Sponsor;
