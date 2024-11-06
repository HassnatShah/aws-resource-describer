// frontend/src/components/ServicesList.js

import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchServices } from '../store/servicesActions';
import { Link } from 'react-router-dom';
import './ServicesList.css';

const ServicesList = () => {
  const dispatch = useDispatch();
  const servicesState = useSelector((state) => state.services);
  const { loading, services, error } = servicesState;

  useEffect(() => {
    dispatch(fetchServices());
  }, [dispatch]);

  return (
    <div className="services-list">
      <h1>AWS Services</h1>
      {loading && <p>Loading services...</p>}
      {error && <p className="error">Error: {error}</p>}
      <ul>
        {services.map((service) => (
          <li key={service}>
            <Link to={`/services/${service}`} className="service-link">
              {capitalize(service)}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

const capitalize = (s) => s.charAt(0).toUpperCase() + s.slice(1);

export default ServicesList;