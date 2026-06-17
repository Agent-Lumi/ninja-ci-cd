"""
Tests for the 🥷 Ninja Skills module.
"""

import pytest
from ninja.skills import NinjaSkills, Technique


class TestNinjaSkills:
    """Test cases for NinjaSkills class."""

    def test_initialization(self):
        """Test ninja skills initialization."""
        skills = NinjaSkills()
        assert skills.mastered_techniques == []
        assert skills.skill_level == 1

    def test_list_techniques(self):
        """Test listing all available techniques."""
        skills = NinjaSkills()
        techniques = skills.list_all_techniques()
        
        assert len(techniques) == 8
        for tech in techniques:
            assert "name" in tech
            assert "description" in tech
            assert "difficulty" in tech
            assert "damage" in tech
            assert "mastered" in tech
            assert isinstance(tech["mastered"], bool)

    def test_master_technique(self):
        """Test mastering a technique."""
        skills = NinjaSkills()
        
        result = skills.master_technique("Shadow Clone")
        assert result is True
        assert "Shadow Clone" in skills.mastered_techniques
        
        # Can't master twice
        result = skills.master_technique("Shadow Clone")
        assert result is False

    def test_master_invalid_technique(self):
        """Test mastering an invalid technique."""
        skills = NinjaSkills()
        result = skills.master_technique("Invalid Jutsu")
        assert result is False

    def test_skill_level_increase(self):
        """Test that skill level increases with mastered techniques."""
        skills = NinjaSkills()
        initial_level = skills.skill_level
        
        # Master Shadow Clone (difficulty 5)
        skills.master_technique("Shadow Clone")
        # Master Dragon Fire (difficulty 7)
        skills.master_technique("Dragon Fire")
        
        assert skills.skill_level > initial_level

    def test_get_technique(self):
        """Test getting a specific technique."""
        skills = NinjaSkills()
        tech = skills.get_technique("Shadow Clone")
        
        assert tech is not None
        assert tech["name"] == "Shadow Clone"
        assert tech["description"] == "Parallel test execution"
        assert tech["difficulty"] == 5
        assert tech["damage"] == 80

    def test_get_invalid_technique(self):
        """Test getting a non-existent technique."""
        skills = NinjaSkills()
        tech = skills.get_technique("Non-existent")
        assert tech is None


class TestCodeQualityValidation:
    """Test code quality validation feature."""

    def test_clean_code(self):
        """Test validating clean code."""
        skills = NinjaSkills()
        code = """
def clean_function():
    return "Hello, World!"
"""
        result = skills.validate_code_quality(code)
        
        assert result["score"] == 100
        assert result["grade"] == "🥷 S-Rank Ninja"
        assert len(result["issues"]) == 0

    def test_code_with_secrets(self):
        """Test detecting hardcoded secrets."""
        skills = NinjaSkills()
        code = """
password = "secret123"
api_key = "sk-abc123"
"""
        result = skills.validate_code_quality(code)
        
        assert result["score"] < 100
        assert len(result["issues"]) > 0
        # Should detect both password and api_key
        assert any("password" in issue["message"] for issue in result["issues"])

    def test_code_with_debug_statements(self):
        """Test detecting debug statements."""
        skills = NinjaSkills()
        code = """
def function():
    print("Debug message")
    return True
"""
        result = skills.validate_code_quality(code)
        
        # Should detect print statement
        assert any("Debug" in issue["message"] or "print" in issue["message"] 
                   for issue in result["issues"])

    def test_code_with_long_lines(self):
        """Test detecting long lines."""
        skills = NinjaSkills()
        # Line over 88 characters
        code = "x = \"This is a very long line that exceeds the recommended maximum line length of 88 characters for Python code\""
        
        result = skills.validate_code_quality(code)
        
        # Should have issues for long line
        assert any("Long lines" in issue["message"] for issue in result["issues"])

    def test_grade_calculation(self):
        """Test grade calculation for different scores."""
        skills = NinjaSkills()
        
        # Test various scores
        assert skills._calculate_grade(98) == "🥷 S-Rank Ninja"
        assert skills._calculate_grade(92) == "A - Elite"
        assert skills._calculate_grade(85) == "B - Skilled"
        assert skills._calculate_grade(75) == "C - Competent"
        assert skills._calculate_grade(65) == "D - Needs Training"
        assert skills._calculate_grade(50) == "F - Academy Student"


class TestTechnique:
    """Test cases for Technique dataclass."""

    def test_technique_creation(self):
        """Test creating a technique."""
        tech = Technique(
            name="Test Jutsu",
            description="A test technique",
            difficulty=5,
            damage=80
        )
        
        assert tech.name == "Test Jutsu"
        assert tech.description == "A test technique"
        assert tech.difficulty == 5
        assert tech.damage == 80