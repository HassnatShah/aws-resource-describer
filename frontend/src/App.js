// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ServicesList from './components/ServicesList';
import SubservicesList from './components/SubservicesList';
import ServiceDetails from './components/ServiceDetails';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<ServicesList />} />
          <Route path="/services/:serviceName" element={<SubservicesList />} />
          <Route path="/services/:serviceName/:subserviceName" element={<ServiceDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;