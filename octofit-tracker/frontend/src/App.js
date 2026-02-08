import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, NavLink } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Workouts from './components/Workouts';
import Leaderboard from './components/Leaderboard';

function Home() {
  return (
    <div className="container mt-4">
      <div className="text-center mb-5">
        <h1 className="display-4 fw-bold">Welcome to OctoFit Tracker</h1>
        <p className="lead text-muted">Track your fitness activities and compete with your team!</p>
      </div>
      
      <div className="row g-4">
        <div className="col-md-6 col-lg-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="display-3 mb-3">👥</div>
              <h5 className="card-title">Users</h5>
              <p className="card-text">View all registered users and their fitness stats</p>
              <Link to="/users" className="btn btn-primary">View Users</Link>
            </div>
          </div>
        </div>
        
        <div className="col-md-6 col-lg-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="display-3 mb-3">🏢</div>
              <h5 className="card-title">Teams</h5>
              <p className="card-text">Explore teams and join the competition</p>
              <Link to="/teams" className="btn btn-primary">View Teams</Link>
            </div>
          </div>
        </div>
        
        <div className="col-md-6 col-lg-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="display-3 mb-3">🏃</div>
              <h5 className="card-title">Activities</h5>
              <p className="card-text">Track all fitness activities and progress</p>
              <Link to="/activities" className="btn btn-primary">View Activities</Link>
            </div>
          </div>
        </div>
        
        <div className="col-md-6 col-lg-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="display-3 mb-3">💪</div>
              <h5 className="card-title">Workouts</h5>
              <p className="card-text">Browse available workout types and programs</p>
              <Link to="/workouts" className="btn btn-primary">View Workouts</Link>
            </div>
          </div>
        </div>
        
        <div className="col-md-6 col-lg-4">
          <div className="card h-100">
            <div className="card-body text-center">
              <div className="display-3 mb-3">🏆</div>
              <h5 className="card-title">Leaderboard</h5>
              <p className="card-text">Check the competition rankings and top performers</p>
              <Link to="/leaderboard" className="btn btn-primary">View Leaderboard</Link>
            </div>
          </div>
        </div>
        
        <div className="col-md-6 col-lg-4">
          <div className="card h-100 bg-light">
            <div className="card-body text-center d-flex flex-column justify-content-center">
              <h5 className="card-title">Get Started</h5>
              <p className="card-text">Join a team and start tracking your fitness journey today!</p>
              <div className="d-flex flex-wrap gap-2 justify-content-center">
                <Link to="/users" className="btn btn-sm btn-outline-primary">Sign Up</Link>
                <Link to="/teams" className="btn btn-sm btn-outline-secondary">Join Team</Link>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div className="alert alert-info mt-5" role="alert">
        <h4 className="alert-heading">🎯 Quick Stats</h4>
        <p className="mb-0">
          Navigate through the menu to explore users, teams, activities, and compete on the leaderboard!
        </p>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand d-flex align-items-center" to="/">
              <img 
                src="/octofitapp-logo.png" 
                alt="OctoFit Logo" 
                className="navbar-logo me-2"
              />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/"
                  >
                    Home
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/users"
                  >
                    Users
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/teams"
                  >
                    Teams
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/activities"
                  >
                    Activities
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/workouts"
                  >
                    Workouts
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink 
                    className={({ isActive }) => isActive ? "nav-link active" : "nav-link"} 
                    to="/leaderboard"
                  >
                    Leaderboard
                  </NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
