"""
Tests for the 🥷 Ninja Web Application.
"""

import pytest
from ninja.app import app, ninja, skills


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Test the health check endpoint."""

    def test_health_status(self, client):
        """Test health endpoint returns healthy status."""
        response = client.get('/api/health')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['stealth_mode'] is True
        assert data['clan'] == 'Shadow CI/CD'
        assert 'timestamp' in data


class TestStatsEndpoint:
    """Test the stats endpoint."""

    def test_stats_structure(self, client):
        """Test stats endpoint returns correct structure."""
        response = client.get('/api/stats')
        assert response.status_code == 200
        
        data = response.get_json()
        assert 'clan' in data
        assert 'missions_completed' in data
        assert 'missions_failed' in data
        assert 'stealth_mode' in data
        assert 'rank' in data


class TestTechniquesEndpoint:
    """Test the techniques endpoint."""

    def test_techniques_list(self, client):
        """Test techniques endpoint returns list."""
        response = client.get('/api/techniques')
        assert response.status_code == 200
        
        data = response.get_json()
        assert 'techniques' in data
        assert 'skill_level' in data
        assert len(data['techniques']) == 8

    def test_techniques_have_required_fields(self, client):
        """Test that each technique has required fields."""
        response = client.get('/api/techniques')
        data = response.get_json()
        
        for tech in data['techniques']:
            assert 'name' in tech
            assert 'description' in tech
            assert 'difficulty' in tech
            assert 'damage' in tech
            assert 'mastered' in tech


class TestDashboard:
    """Test the main dashboard."""

    def test_dashboard_loads(self, client):
        """Test that the dashboard loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        
        # Check for key elements in the HTML
        html = response.data.decode('utf-8')
        assert '🥷 Ninja CI/CD' in html
        assert 'Shadow CI/CD' in html


class TestMissionExecution:
    """Test mission execution endpoint."""

    def test_execute_mission_success(self, client):
        """Test executing a mission via API."""
        response = client.post('/api/mission', 
                              json={'mission': 'test', 'payload': {'key': 'value'}},
                              content_type='application/json')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['mission'] == 'test'
        assert data['status'] == 'success'
        assert 'metrics' in data

    def test_execute_mission_empty_payload(self, client):
        """Test executing a mission with empty payload."""
        response = client.post('/api/mission',
                              json={'mission': 'empty_test'},
                              content_type='application/json')
        assert response.status_code == 200
        
        data = response.get_json()
        assert data['mission'] == 'empty_test'
        assert 'metrics' in data


class TestErrorHandling:
    """Test error handling."""

    def test_404_error(self, client):
        """Test 404 for unknown endpoint."""
        response = client.get('/api/unknown')
        assert response.status_code == 404

    def test_invalid_method(self, client):
        """Test invalid HTTP method."""
        response = client.post('/api/health')
        assert response.status_code == 405