import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const getResources = async () => {
  try {
    const response = await axios.get(`${API_URL}/describe-resources`);
    return response.data;
  } catch (error) {
    console.error('Error fetching resources:', error);
    throw error;
  }
};