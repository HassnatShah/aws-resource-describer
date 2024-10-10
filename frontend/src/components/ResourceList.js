import React, { useEffect, useState } from 'react';
import { getResources } from '../services/api';

const ResourceList = () => {
  const [resources, setResources] = useState([]);

  useEffect(() => {
    const fetchResources = async () => {
      try {
        const data = await getResources();
        setResources(data.Reservations || []); // Adjust according to API response
      } catch (error) {
        console.error('Failed to fetch resources:', error);
      }
    };

    fetchResources();
  }, []);

  return (
    <div>
      <h2>AWS EC2 Instances</h2>
      {resources.length === 0 ? (
        <p>No resources found.</p>
      ) : (
        resources.map((reservation, index) => (
          <div key={index}>
            {reservation.Instances.map((instance) => (
              <div key={instance.InstanceId}>
                <p>Instance ID: {instance.InstanceId}</p>
                <p>Instance Type: {instance.InstanceType}</p>
                {/* Add more instance details as needed */}
              </div>
            ))}
          </div>
        ))
      )}
    </div>
  );
};

export default ResourceList;