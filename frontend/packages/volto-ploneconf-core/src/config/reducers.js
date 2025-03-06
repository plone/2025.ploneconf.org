// Reducers
import reducers from '../reducers';

export default function installReducers(config) {
  config.addonReducers = { ...config.addonReducers, ...reducers };
  return config;
}
