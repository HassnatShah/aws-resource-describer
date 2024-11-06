import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const fetchInstances = async () => {
  try {
    const response = await axios.get(`${API_URL}/describe-resources`);
    return response.data.Instances; // Return the array of instances directly
  } catch (error) {
    if (error.response) {
      console.error('Server Error:', error.response.data);
      throw new Error(error.response.data.error || 'Server Error');
    } else if (error.request) {
      console.error('Network Error:', error.request);
      throw new Error('Network Error');
    } else {
      console.error('Error:', error.message);
      throw new Error(error.message);
    }
  }
};