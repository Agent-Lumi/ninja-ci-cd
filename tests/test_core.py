"""
Tests for the 🥷 Ninja Core module.
"""

import pytest
from ninja.core import MissionStatus, NinjaCore, NinjaMetrics


class TestNinjaCore:
    """Test cases for NinjaCore class."""

    def test_ninja_initialization(self):
        """Test that a ninja is properly initialized."""
        ninja = NinjaCore()
        assert ninja.clan_name == "Shadow CI/CD"
        assert ninja.missions_completed == 0
        assert ninja.missions_failed == 0
        assert ninja.stealth_mode is True

    def test_custom_clan(self):
        """Test creating a ninja with a custom clan."""
        ninja = NinjaCore(clan_name="Thunder Strike")
        assert ninja.clan_name == "Thunder Strike"

    def test_execute_mission(self):
        """Test executing a ninja mission."""
        ninja = NinjaCore()
        result = ninja.execute_mission(
            "test_mission",
            {"target": "production", "payload": "test"}
        )
        
        assert result["mission"] == "test_mission"
        assert result["status"] == MissionStatus.SUCCESS.value
        assert result["clan"] == "Shadow CI/CD"
        assert "payload_hash" in result
        assert "metrics" in result
        assert ninja.missions_completed == 1

    def test_mission_metrics(self):
        """Test that mission execution returns proper metrics."""
        ninja = NinjaCore()
        result = ninja.execute_mission("metrics_test", {})
        
        metrics = result["metrics"]
        assert "execution_time_ms" in metrics
        assert "memory_usage_mb" in metrics
        assert "stealth_score" in metrics
        assert "accuracy" in metrics
        assert 0 <= metrics["stealth_score"] <= 100
        assert 0.0 <= metrics["accuracy"] <= 1.0

    def test_stealth_check_production(self):
        """Test stealth check in production environment."""
        ninja = NinjaCore()
        assert ninja.stealth_check("production") is True
        assert ninja.stealth_check("staging") is True
        assert ninja.stealth_check("ninja-lair") is True

    def test_stealth_check_development(self):
        """Test stealth check in development environment."""
        ninja = NinjaCore()
        assert ninja.stealth_check("development") is False

    def test_get_stats_initial(self):
        """Test getting stats for a new ninja."""
        ninja = NinjaCore()
        stats = ninja.get_stats()
        
        assert stats["clan"] == "Shadow CI/CD"
        assert stats["missions_completed"] == 0
        assert stats["missions_failed"] == 0
        assert stats["stealth_mode"] is True
        assert stats["rank"] == "🌱 Novice"

    def test_rank_progression(self):
        """Test rank progression as missions are completed."""
        ninja = NinjaCore()
        
        # Complete 10 missions for Skilled rank
        for _ in range(10):
            ninja.execute_mission("mission", {})
        assert ninja.get_stats()["rank"] == "⭐ Skilled"
        
        # Complete 10 more for Expert rank
        for _ in range(10):
            ninja.execute_mission("mission", {})
        assert ninja.get_stats()["rank"] == "🗡️ Expert"


class TestNinjaMetrics:
    """Test cases for NinjaMetrics dataclass."""

    def test_metrics_creation(self):
        """Test creating metrics."""
        metrics = NinjaMetrics(
            execution_time_ms=100.5,
            memory_usage_mb=2.5,
            stealth_score=85,
            accuracy=0.95
        )
        
        assert metrics.execution_time_ms == 100.5
        assert metrics.memory_usage_mb == 2.5
        assert metrics.stealth_score == 85
        assert metrics.accuracy == 0.95

    def test_metrics_to_dict(self):
        """Test converting metrics to dictionary."""
        metrics = NinjaMetrics(
            execution_time_ms=50.0,
            memory_usage_mb=1.0,
            stealth_score=90,
            accuracy=0.99
        )
        
        d = metrics.to_dict()
        assert d["execution_time_ms"] == 50.0
        assert d["memory_usage_mb"] == 1.0
        assert d["stealth_score"] == 90
        assert d["accuracy"] == 0.99


class TestMissionStatus:
    """Test cases for MissionStatus enum."""

    def test_status_values(self):
        """Test mission status enum values."""
        assert MissionStatus.STEALTH.value == "stealth"
        assert MissionStatus.STRIKE.value == "strike"
        assert MissionStatus.SUCCESS.value == "success"
        assert MissionStatus.FAILED.value == "failed"