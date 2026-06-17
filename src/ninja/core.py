"""
🥷 Ninja Core Module
The heart of the ninja application - fast, stealthy, and deadly accurate.
"""

import hashlib
import json
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
from enum import Enum


class MissionStatus(Enum):
    """Ninja mission status codes"""
    STEALTH = "stealth"      # In progress, undetected
    STRIKE = "strike"        # Active execution
    SUCCESS = "success"      # Mission accomplished
    FAILED = "failed"        # Mission failed


@dataclass
class NinjaMetrics:
    """Performance metrics for ninja operations"""
    execution_time_ms: float
    memory_usage_mb: float
    stealth_score: int  # 0-100
    accuracy: float     # 0.0-1.0
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class NinjaCore:
    """
    🥷 The Ninja Core
    
    Handles missions with stealth and precision.
    Like a true ninja, it's fast, efficient, and leaves no trace.
    """
    
    def __init__(self, clan_name: str = "Shadow CI/CD"):
        self.clan_name = clan_name
        self.missions_completed = 0
        self.missions_failed = 0
        self.stealth_mode = True
        
    def execute_mission(self, mission_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a ninja mission with the given payload.
        
        Args:
            mission_name: The name of the mission
            payload: Mission parameters
            
        Returns:
            Mission result with status and metrics
        """
        start_time = time.time()
        
        # Simulate mission execution
        time.sleep(0.001)  # Ninja speed!
        
        # Calculate stealth score based on payload complexity
        payload_hash = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode()
        ).hexdigest()
        
        stealth_score = min(100, max(50, 100 - len(payload_hash) // 10))
        
        execution_time = (time.time() - start_time) * 1000
        
        result = {
            "mission": mission_name,
            "status": MissionStatus.SUCCESS.value,
            "clan": self.clan_name,
            "payload_hash": payload_hash[:16] + "...",
            "metrics": NinjaMetrics(
                execution_time_ms=execution_time,
                memory_usage_mb=0.5,
                stealth_score=stealth_score,
                accuracy=0.98
            ).to_dict(),
            "timestamp": time.time()
        }
        
        self.missions_completed += 1
        return result
    
    def stealth_check(self, environment: str) -> bool:
        """
        Check if we can operate undetected in the given environment.
        
        Args:
            environment: Target environment name
            
        Returns:
            True if stealth is possible
        """
        # Ninja is always stealthy in production
        return environment in ["production", "staging", "ninja-lair"]
    
    def get_stats(self) -> Dict[str, Any]:
        """Get ninja clan statistics"""
        return {
            "clan": self.clan_name,
            "missions_completed": self.missions_completed,
            "missions_failed": self.missions_failed,
            "stealth_mode": self.stealth_mode,
            "rank": self._calculate_rank()
        }
    
    def _calculate_rank(self) -> str:
        """Calculate ninja rank based on missions completed"""
        if self.missions_completed >= 100:
            return "🥷 Grandmaster"
        elif self.missions_completed >= 50:
            return "⚔️ Master"
        elif self.missions_completed >= 20:
            return "🗡️ Expert"
        elif self.missions_completed >= 10:
            return "⭐ Skilled"
        else:
            return "🌱 Novice"