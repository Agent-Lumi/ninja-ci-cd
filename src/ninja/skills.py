"""
🥷 Ninja Skills Module
Special abilities and techniques for the CI/CD ninja.
"""

import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class Technique:
    """A ninja technique/skill"""
    name: str
    description: str
    difficulty: int  # 1-10
    damage: int      # Impact score


class NinjaSkills:
    """
    🥷 Ninja Skills
    
    Specialized techniques for CI/CD mastery.
    """
    
    TECHNIQUES = [
        Technique("Shadow Clone", "Parallel test execution", 5, 80),
        Technique("Silent Step", "Zero-downtime deployment", 8, 95),
        Technique("Smoke Bomb", "Rollback on failure", 4, 70),
        Technique("Dragon Fire", "High-performance builds", 7, 90),
        Technique("Water Walking", "Cross-platform compatibility", 6, 75),
        Technique("Mind Transfer", "Configuration as code", 9, 100),
        Technique("Rasengan", "Dependency caching", 5, 85),
        Technique("Chidori", "Lightning-fast tests", 7, 88),
    ]
    
    def __init__(self):
        self.mastered_techniques: List[str] = []
        self.skill_level = 1
        
    def list_all_techniques(self) -> List[Dict[str, Any]]:
        """List all available ninja techniques"""
        return [
            {
                "name": t.name,
                "description": t.description,
                "difficulty": t.difficulty,
                "damage": t.damage,
                "mastered": t.name in self.mastered_techniques
            }
            for t in self.TECHNIQUES
        ]
    
    def master_technique(self, technique_name: str) -> bool:
        """Master a specific technique"""
        technique = self._find_technique(technique_name)
        if technique and technique_name not in self.mastered_techniques:
            self.mastered_techniques.append(technique_name)
            self._update_skill_level()
            return True
        return False
    
    def get_technique(self, technique_name: str) -> Optional[Dict[str, Any]]:
        """Get details of a specific technique"""
        technique = self._find_technique(technique_name)
        if technique:
            return {
                "name": technique.name,
                "description": technique.description,
                "difficulty": technique.difficulty,
                "damage": technique.damage,
                "mastered": technique.name in self.mastered_techniques
            }
        return None
    
    def validate_code_quality(self, code: str) -> Dict[str, Any]:
        """
        🥷 Code Quality Validation
        
        Ninja-level code inspection for stealth and efficiency.
        """
        issues = []
        score = 100
        
        # Check for obvious secrets
        secret_patterns = [
            (r'password\s*=\s*["\'][^"\']+["\']', "Hardcoded password detected!"),
            (r'api[_-]?key\s*=\s*["\'][^"\']+["\']', "API key exposed!"),
            (r'secret\s*=\s*["\'][^"\']+["\']', "Secret in code!"),
        ]
        
        for pattern, message in secret_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                issues.append({"severity": "critical", "message": message})
                score -= 25
        
        # Check for debug statements
        if re.search(r'(print|console\.log|debugger)', code):
            issues.append({"severity": "warning", "message": "Debug statements found"})
            score -= 10
        
        # Check line length (ninja code is compact)
        lines = code.split('\n')
        long_lines = [i for i, line in enumerate(lines, 1) if len(line) > 88]
        if long_lines:
            issues.append({
                "severity": "info", 
                "message": f"Long lines detected on: {long_lines}"
            })
            score -= len(long_lines) * 2
        
        return {
            "score": max(0, score),
            "grade": self._calculate_grade(score),
            "issues": issues,
            "lines_analyzed": len(lines)
        }
    
    def _find_technique(self, name: str) -> Optional[Technique]:
        """Find a technique by name"""
        for t in self.TECHNIQUES:
            if t.name.lower() == name.lower():
                return t
        return None
    
    def _update_skill_level(self):
        """Update overall skill level based on mastered techniques"""
        total_difficulty = sum(
            t.difficulty for t in self.TECHNIQUES
            if t.name in self.mastered_techniques
        )
        self.skill_level = 1 + (total_difficulty // 10)
    
    def _calculate_grade(self, score: int) -> str:
        """Calculate letter grade from score"""
        if score >= 95:
            return "🥷 S-Rank Ninja"
        elif score >= 90:
            return "A - Elite"
        elif score >= 80:
            return "B - Skilled"
        elif score >= 70:
            return "C - Competent"
        elif score >= 60:
            return "D - Needs Training"
        else:
            return "F - Academy Student"