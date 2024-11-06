import React, { useState } from 'react';
import { fetchInstances } from '../services/api';
import './ResourceList.css';

const ResourceList = () => {
  const [instances, setInstances] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const loadInstances = async () => {
    setLoading(true);
    try {
      const data = await fetchInstances();
      setInstances(data || []);
      setError(null);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  const toggleDetails = (id) => {
    setInstances((prevInstances) =>
      prevInstances.map((instance) =>
        instance.InstanceId === id
          ? { ...instance, showDetails: !instance.showDetails }
          : instance
      )
    );
  };

  return (
    <div className="resource-list">
      <h2>EC2 Instances</h2>
      <button onClick={loadInstances}>Refresh</button>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {instances.length === 0 && !loading && !error ? (
        <p>No instances found.</p>
      ) : (
        instances.map((instance) => (
          <div key={instance.InstanceId} className="instance-card">
            <div
              className="instance-header"
              onClick={() => toggleDetails(instance.InstanceId)}
            >
              <h3>
                {instance.InstanceId} - {instance.InstanceType}
              </h3>
              <p>
                <strong>State:</strong> {instance.State.Name}
              </p>
            </div>
            {instance.showDetails && (
              <div className="instance-details">
                {/* Basic Info */}
                <div className="section">
                  <h4>Basic Info</h4>
                  <p>
                    <strong>Public DNS:</strong> {instance.PublicDnsName}
                  </p>
                  <p>
                    <strong>Private DNS:</strong> {instance.PrivateDnsName}
                  </p>
                  <p>
                    <strong>Key Pair:</strong> {instance.KeyName}
                  </p>
                  <p>
                    <strong>Launch Time:</strong> {instance.LaunchTime}
                  </p>
                  <p>
                    <strong>AMI ID:</strong> {instance.ImageId}
                  </p>
                </div>

                {/* Networking */}
                <div className="section">
                  <h4>Networking</h4>
                  <p>
                    <strong>Public IP:</strong> {instance.PublicIpAddress}
                  </p>
                  <p>
                    <strong>Private IP:</strong> {instance.PrivateIpAddress}
                  </p>
                  <p>
                    <strong>Availability Zone:</strong>{' '}
                    {instance.Placement.AvailabilityZone}
                  </p>
                </div>

                {/* Security Groups */}
                <div className="section">
                  <h4>Security Groups</h4>
                  {instance.SecurityGroups.map((sg, index) => (
                    <p key={index}>
                      <strong>{sg.GroupName}</strong> (ID: {sg.GroupId})
                    </p>
                  ))}
                </div>

                {/* Storage */}
                <div className="section">
                  <h4>Storage</h4>
                  {instance.BlockDeviceMappings.map((bdm, index) => (
                    <p key={index}>
                      <strong>Device:</strong> {bdm.DeviceName} -{' '}
                      <strong>Volume ID:</strong> {bdm.Ebs.VolumeId}
                    </p>
                  ))}
                </div>

                {/* IAM Role */}
                <div className="section">
                  <h4>IAM Role</h4>
                  <p>
                    <strong>ARN:</strong> {instance.IamInstanceProfile.Arn}
                  </p>
                  <p>
                    <strong>ID:</strong> {instance.IamInstanceProfile.Id}
                  </p>
                </div>

                {/* Additional Details */}
                <div className="section">
                  <h4>Additional Details</h4>
                  <p>
                    <strong>Hypervisor:</strong> {instance.Hypervisor}
                  </p>
                  <p>
                    <strong>Monitoring:</strong> {instance.Monitoring}
                  </p>
                  <p>
                    <strong>EBS Optimized:</strong>{' '}
                    {instance.EbsOptimized ? 'Yes' : 'No'}
                  </p>
                  <p>
                    <strong>Source/Dest Check:</strong>{' '}
                    {instance.SourceDestCheck ? 'Enabled' : 'Disabled'}
                  </p>
                </div>
              </div>
            )}
          </div>
        ))
      )}
    </div>
  );
};

export default ResourceList;