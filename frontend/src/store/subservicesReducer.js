// frontend/src/store/subservicesReducer.js

import {
    FETCH_SUBSERVICES_REQUEST,
    FETCH_SUBSERVICES_SUCCESS,
    FETCH_SUBSERVICES_FAILURE,
  } from './subservicesActions';
  
  const initialState = {
    loading: false,
    subservices: [],
    error: '',
  };
  
  const subservicesReducer = (state = initialState, action) => {
    switch (action.type) {
      case FETCH_SUBSERVICES_REQUEST:
        return {
          ...state,
          loading: true,
        };
      case FETCH_SUBSERVICES_SUCCESS:
        return {
          loading: false,
          subservices: action.payload,
          error: '',
        };
      case FETCH_SUBSERVICES_FAILURE:
        return {
          loading: false,
          subservices: [],
          error: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default subservicesReducer;  