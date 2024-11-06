// src/services/api.js

import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const getResources = async () => {
  try {
    const response = await axios.get(`${API_URL}/describe-resources`);
    return response.data;
  } catch (error) {
    // Check if response exists
    if (error.response) {
      // Server responded with a status other than 2xx
      console.error('Server Error:', error.response.data);
      throw new Error(error.response.data.error || 'Server Error');
    } else if (error.request) {
      // Request was made but no response received
      console.error('Network Error:', error.request);
      throw new Error('Network Error');
    } else {
      // Something else happened
      console.error('Error:', error.message);
      throw new Error(error.message);
    }
  }
};