// // src/components/ResourceList.js

// import React, { useEffect, useState } from 'react';
// import { getResources } from '../services/api';

// const ResourceList = () => {
//   const [resources, setResources] = useState([]);
//   const [error, setError] = useState(null); // New state for error

//   const fetchResources = async () => {
//     try {
//       const data = await getResources();
//       setResources(data.Instances || []);
//       setError(null); // Reset error if successful
//     } catch (error) {
//       setError(error.message);
//     }
//   };

//   useEffect(() => {
//     fetchResources();
//   }, []);

//   return (
//     <div>
//       <h2>AWS EC2 Instances</h2>
//       {error && <p style={{ color: 'red' }}>Error: {error}</p>}
//       {resources.length === 0 && !error ? (
//         <p>No resources found.</p>
//       ) : (
//         resources.map((instance, index) => (
//           <div key={index}>
//             <p>Instance ID: {instance.InstanceId}</p>
//             <p>Instance Type: {instance.InstanceType}</p>
//             {/* Add more instance details as needed */}
//           </div>
//         ))
//       )}
//     </div>
//   );
// };

// export default ResourceList;

// src/components/ResourceList.js

import React, { useState } from 'react';
import { getResources } from '../services/api';

const ResourceList = () => {
  const [resources, setResources] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false); // New state for loading

  const fetchResources = async () => {
    setLoading(true);
    try {
      const data = await getResources();
      setResources(data.Instances || []);
      setError(null);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>AWS EC2 Instances</h2>
      <button onClick={fetchResources}>Refresh</button>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {resources.length === 0 && !loading && !error ? (
        <p>No resources found.</p>
      ) : (
        resources.map((instance, index) => (
          <div key={index}>
            <p>Instance ID: {instance.InstanceId}</p>
            <p>Instance Type: {instance.InstanceType}</p>
            {/* Add more instance details as needed */}
          </div>
        ))
      )}
    </div>
  );
};

export default ResourceList;