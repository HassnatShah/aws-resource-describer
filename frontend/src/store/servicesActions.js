// frontend/src/store/servicesActions.js

import axios from 'axios';

// Action Types
export const FETCH_SERVICES_REQUEST = 'FETCH_SERVICES_REQUEST';
export const FETCH_SERVICES_SUCCESS = 'FETCH_SERVICES_SUCCESS';
export const FETCH_SERVICES_FAILURE = 'FETCH_SERVICES_FAILURE';

// Action Creators
export const fetchServicesRequest = () => ({
  type: FETCH_SERVICES_REQUEST,
});

export const fetchServicesSuccess = (services) => ({
  type: FETCH_SERVICES_SUCCESS,
  payload: services,
});

export const fetchServicesFailure = (error) => ({
  type: FETCH_SERVICES_FAILURE,
  payload: error,
});

// Thunk Action
export const fetchServices = () => {
  return async (dispatch) => {
    dispatch(fetchServicesRequest());
    try {
      const response = await axios.get('/api/services');
      dispatch(fetchServicesSuccess(response.data.services));
    } catch (error) {
      dispatch(fetchServicesFailure(error.message));
    }
  };
};