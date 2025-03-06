// Blocks
import SponsorsEdit from '../components/Blocks/Sponsors/Edit';
import SponsorsView from '../components/Blocks/Sponsors/View';
import SponsorLevelEdit from '../components/Blocks/SponsorLevel/Edit';
import SponsorLevelView from '../components/Blocks/SponsorLevel/View';
import { sponsorLevelRestrict } from '../components/Blocks/SponsorLevel/utils';

// Icons
import listBulletSVG from '@plone/volto/icons/list-bullet.svg';

export default function installBlocks(config) {
  config.blocks.blocksConfig.sponsorsList = {
    id: 'sponsorsList',
    title: 'Sponsors',
    icon: listBulletSVG,
    group: 'common',
    view: SponsorsEdit,
    edit: SponsorsView,
    restricted: false,
    mostUsed: false,
    sidebarTab: 0,
    security: {
      addPermission: [],
      view: [],
    },
  };
  config.blocks.blocksConfig.sponsorLevel = {
    id: 'sponsorLevel',
    title: 'Sponsor Level',
    icon: listBulletSVG,
    group: 'common',
    view: SponsorLevelView,
    edit: SponsorLevelEdit,
    restricted: sponsorLevelRestrict,
    mostUsed: false,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: [],
    },
  };

  return config;
}
