import { useState, useEffect } from 'react';
import axios from 'axios';
import { HashLink } from 'react-router-hash-link';

export function VisitorCount() {
  const [message, setMessage] = useState('Not Requested Yet');

  useEffect(() => {
    axios.post('https://431e2ijwgg.execute-api.ap-southeast-1.amazonaws.com/Prod/put_visitor_count')
      .then(response => {
        setMessage(response.data.visitor_count);
      })
      .catch(error => {
        console.error('Error updating visitor count:', error);
      });
  }, []); // Runs once when the component mounts

  return (
    <HashLink smooth to="#home" className="logo">
      <span>{"Visitor "}</span>
      <span>{` Count: ${message}`}</span>
    </HashLink>
  );
}
