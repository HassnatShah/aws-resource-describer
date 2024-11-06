// // frontend/src/store/subservicesActions.js

// import axios from 'axios';

// // Action Types
// export const FETCH_SUBSERVICES_REQUEST = 'FETCH_SUBSERVICES_REQUEST';
// export const FETCH_SUBSERVICES_SUCCESS = 'FETCH_SUBSERVICES_SUCCESS';
// export const FETCH_SUBSERVICES_FAILURE = 'FETCH_SUBSERVICES_FAILURE';

// // Action Creators
// export const fetchSubservicesRequest = () => ({
//   type: FETCH_SUBSERVICES_REQUEST,
// });

// export const fetchSubservicesSuccess = (subservices) => ({
//   type: FETCH_SUBSERVICES_SUCCESS,
//   payload: subservices,
// });

// export const fetchSubservicesFailure = (error) => ({
//   type: FETCH_SUBSERVICES_FAILURE,
//   payload: error,
// });

// // Thunk Action
// export const fetchSubservices = (serviceName) => {
//   return async (dispatch) => {
//     dispatch(fetchSubservicesRequest());
//     try {
//       const response = await axios.get(`/api/services/${serviceName}`);
//       dispatch(fetchSubservicesSuccess(response.data.subservices));
//     } catch (error) {
//       dispatch(fetchSubservicesFailure(error.message));
//     }
//   };
// };

// frontend/src/store/subservicesActions.js

import axios from 'axios';

// Action Types
export const FETCH_SUBSERVICES_REQUEST = 'FETCH_SUBSERVICES_REQUEST';
export const FETCH_SUBSERVICES_SUCCESS = 'FETCH_SUBSERVICES_SUCCESS';
export const FETCH_SUBSERVICES_FAILURE = 'FETCH_SUBSERVICES_FAILURE';

// Action Creators
export const fetchSubservicesRequest = () => ({
  type: FETCH_SUBSERVICES_REQUEST,
});

export const fetchSubservicesSuccess = (subservices) => ({
  type: FETCH_SUBSERVICES_SUCCESS,
  payload: subservices,
});

export const fetchSubservicesFailure = (error) => ({
  type: FETCH_SUBSERVICES_FAILURE,
  payload: error,
});

// Thunk Action
export const fetchSubservices = (serviceName) => {
  return async (dispatch) => {
    dispatch(fetchSubservicesRequest());
    try {
      const response = await axios.get(`/api/services/${serviceName}`);
      dispatch(fetchSubservicesSuccess(response.data.subservices));
    } catch (error) {
      dispatch(fetchSubservicesFailure(error.message));
    }
  };
};
