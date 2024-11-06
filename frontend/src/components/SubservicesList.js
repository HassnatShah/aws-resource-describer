// frontend/src/components/SubservicesList.js

import React, { useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { fetchSubservices } from '../store/subservicesActions';
import './SubservicesList.css';

const SubservicesList = () => {
  const { serviceName } = useParams();
  const dispatch = useDispatch();
  const subservicesState = useSelector((state) => state.subservices);
  const { loading, subservices, error } = subservicesState;

  useEffect(() => {
    if (serviceName) {
      dispatch(fetchSubservices(serviceName));
    }
  }, [dispatch, serviceName]);

  return (
    <div className="subservices-list">
      <h1>{capitalize(serviceName)} Sub-services</h1>
      <Link to="/" className="back-link">← Back to Services</Link>
      {loading && <p>Loading sub-services...</p>}
      {error && <p className="error">Error: {error}</p>}
      <ul>
        {subservices.map((subservice) => (
          <li key={subservice}>
            <Link to={`/services/${serviceName}/${subservice}`} className="subservice-link">
              {formatSubserviceName(subservice)}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

const capitalize = (s) => s.charAt(0).toUpperCase() + s.slice(1);

const formatSubserviceName = (s) => {
  // Replace hyphens with spaces and capitalize words
  return s.split('-').map(word => capitalize(word)).join(' ');
};

export default SubservicesList;