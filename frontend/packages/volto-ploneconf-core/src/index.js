import installBlocks from './config/blocks';
import installSettings from './config/settings';
import installReducers from './config/reducers';
import installViews from './config/views';

const applyConfig = (config) => {
  installSettings(config);
  installBlocks(config);
  installReducers(config);
  installViews(config);

  return config;
};

export default applyConfig;
