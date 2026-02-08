import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
      : 'http://localhost:8000/api/leaderboard/';
    
    console.log('Leaderboard Component - Fetching from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard Component - Raw data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard Component - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard Component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-2">Loading leaderboard...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  const getRankBadge = (index) => {
    if (index === 0) return { class: 'bg-warning text-dark', icon: '🥇' };
    if (index === 1) return { class: 'bg-secondary', icon: '🥈' };
    if (index === 2) return { class: 'bg-danger', icon: '🥉' };
    return { class: 'bg-primary', icon: '#' };
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="mb-0">🏆 Leaderboard</h2>
        <span className="badge bg-primary">{leaderboard.length} Competitors</span>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="col">Rank</th>
              <th scope="col">User</th>
              <th scope="col">Team</th>
              <th scope="col">Points</th>
              <th scope="col">Activities</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => {
                const badge = getRankBadge(index);
                return (
                  <tr key={entry.id || entry._id || index} className={index < 3 ? 'table-active' : ''}>
                    <td>
                      <span className={`badge ${badge.class}`}>
                        {badge.icon} {index + 1}
                      </span>
                    </td>
                    <td><strong>{entry.user_name || entry.username || 'N/A'}</strong></td>
                    <td>
                      {entry.team_name || entry.team ? (
                        <span className="badge bg-info">{entry.team_name || entry.team}</span>
                      ) : (
                        <span className="text-muted">No Team</span>
                      )}
                    </td>
                    <td>
                      <span className="badge bg-success fs-6">{entry.points || entry.total_points || 0} pts</span>
                    </td>
                    <td>{entry.activity_count || entry.activities || 0}</td>
                  </tr>
                );
              })
            ) : (
              <tr>
                <td colSpan="5" className="text-center text-muted">No leaderboard entries found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
