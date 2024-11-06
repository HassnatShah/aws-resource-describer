// frontend/src/store/index.js

import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import servicesReducer from './servicesReducer';
import subservicesReducer from './subservicesReducer';

const rootReducer = combineReducers({
  services: servicesReducer,
  subservices: subservicesReducer,
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;