// frontend/src/components/ServiceDetails.js

import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import './ServiceDetails.css';

const ServiceDetails = () => {
  const { serviceName, subserviceName } = useParams();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [perPage] = useState(10);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError('');
      try {
        const response = await axios.get(`/api/services/${serviceName}/${subserviceName}`, {
          params: {
            page: currentPage,
            per_page: perPage,
          },
        });
        setData(response.data.data);
        // Assuming backend returns total and total_pages
        if (response.data.total && response.data.total_pages) {
          setTotalPages(response.data.total_pages);
        }
      } catch (err) {
        setError(err.response?.data?.description || err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [serviceName, subserviceName, currentPage, perPage]);

  const handleRefresh = () => {
    setCurrentPage(1);
    // Re-fetch data by triggering useEffect
    // Alternatively, you can abstract fetchData and call it here
  };

  const handlePageChange = (newPage) => {
    if (newPage >= 1 && newPage <= totalPages) {
      setCurrentPage(newPage);
    }
  };

  const renderData = () => {
    if (!Array.isArray(data) || data.length === 0) {
      return <p>No data available.</p>;
    }

    // Dynamically render table based on keys
    const headers = Object.keys(data[0]);

    return (
      <table className="details-table">
        <thead>
          <tr>
            {headers.map((header) => (
              <th key={header}>{formatHeader(header)}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              {headers.map((header) => (
                <td key={header}>
                  {typeof item[header] === 'object' ? JSON.stringify(item[header]) : item[header]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  const formatHeader = (header) => {
    // Replace underscores with spaces and capitalize words
    return header.split('_').map(word => capitalize(word)).join(' ');
  };

  const capitalize = (s) => s.charAt(0).toUpperCase() + s.slice(1);

  return (
    <div className="service-details">
      <h1>{capitalize(subserviceName)} Details</h1>
      <Link to={`/services/${serviceName}`} className="back-link">← Back to Sub-services</Link>
      <button className="refresh-button" onClick={handleRefresh}>
        Refresh
      </button>
      {loading && <p>Loading...</p>}
      {error && <p className="error">Error: {error}</p>}
      {!loading && !error && renderData()}
      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="pagination">
          <button
            onClick={() => handlePageChange(currentPage - 1)}
            disabled={currentPage === 1}
            className="pagination-button"
          >
            Previous
          </button>
          {Array.from({ length: totalPages }, (_, i) => (
            <button
              key={i + 1}
              onClick={() => handlePageChange(i + 1)}
              className={`pagination-button ${currentPage === i + 1 ? 'active' : ''}`}
            >
              {i + 1}
            </button>
          ))}
          <button
            onClick={() => handlePageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="pagination-button"
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
};

export default ServiceDetails;