import SponsorView from '../components/View/Sponsor';

export default function installViews(config) {
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    Sponsor: SponsorView,
  };
  return config;
}
