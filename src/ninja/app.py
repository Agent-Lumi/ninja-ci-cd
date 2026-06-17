"""
🥷 Ninja Web Application
A dashboard for monitoring ninja operations.
"""

import json
import os
from flask import Flask, jsonify, render_template_string
from .core import NinjaCore
from .skills import NinjaSkills

app = Flask(__name__)
ninja = NinjaCore()
skills = NinjaSkills()

# Master all techniques for the demo
for technique in skills.TECHNIQUES:
    skills.master_technique(technique.name)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🥷 Ninja CI/CD Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #eee;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            text-align: center;
            padding: 40px 0;
            border-bottom: 3px solid #e94560;
            margin-bottom: 30px;
        }
        h1 {
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .subtitle {
            color: #e94560;
            font-size: 1.2em;
            margin-top: 10px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(233, 69, 96, 0.3);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.2);
        }
        .stat-card h3 {
            color: #e94560;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }
        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
        }
        .techniques {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
        }
        .techniques h2 {
            color: #e94560;
            margin-bottom: 20px;
            font-size: 1.8em;
        }
        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 15px;
        }
        .tech-item {
            background: rgba(0,0,0,0.2);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #e94560;
        }
        .tech-item h4 {
            color: #fff;
            margin-bottom: 8px;
        }
        .tech-item p {
            color: #aaa;
            font-size: 0.9em;
            margin-bottom: 10px;
        }
        .badge {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75em;
            font-weight: bold;
        }
        .badge-mastered {
            background: #22c55e;
            color: white;
        }
        .badge-pending {
            background: #6b7280;
            color: white;
        }
        .pipeline-status {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 30px;
        }
        .pipeline-status h2 {
            color: #e94560;
            margin-bottom: 20px;
        }
        .status-indicator {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 15px;
            background: rgba(34, 197, 94, 0.1);
            border-radius: 10px;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }
        .status-dot {
            width: 12px;
            height: 12px;
            background: #22c55e;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }
        footer {
            text-align: center;
            padding: 40px 0;
            color: #666;
            border-top: 1px solid rgba(233, 69, 96, 0.2);
            margin-top: 30px;
        }
        .api-links {
            margin-top: 20px;
        }
        .api-links a {
            color: #e94560;
            text-decoration: none;
            margin: 0 15px;
        }
        .api-links a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🥷 Ninja CI/CD</h1>
            <div class="subtitle">Stealth Deployments & Lightning-Fast Builds</div>
        </header>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>🎯 Missions Completed</h3>
                <div class="stat-value" id="missions">{{ stats.missions_completed }}</div>
            </div>
            <div class="stat-card">
                <h3>⚔️ Current Rank</h3>
                <div class="stat-value" style="font-size: 1.8em;" id="rank">{{ stats.rank }}</div>
            </div>
            <div class="stat-card">
                <h3>🏯 Clan</h3>
                <div class="stat-value" style="font-size: 1.5em;" id="clan">{{ stats.clan }}</div>
            </div>
            <div class="stat-card">
                <h3>⭐ Skill Level</h3>
                <div class="stat-value" id="skill-level">{{ skill_level }}</div>
            </div>
        </div>
        
        <div class="techniques">
            <h2>🥷 Mastered Techniques</h2>
            <div class="tech-grid">
                {% for tech in techniques %}
                <div class="tech-item">
                    <h4>{{ tech.name }}</h4>
                    <p>{{ tech.description }}</p>
                    <span class="badge badge-mastered">✓ Mastered</span>
                    <span class="badge" style="background: #e94560;">Difficulty: {{ tech.difficulty }}/10</span>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="pipeline-status">
            <h2>🚀 Pipeline Status</h2>
            <div class="status-indicator">
                <div class="status-dot"></div>
                <span>All systems operational - Ninja stealth mode engaged</span>
            </div>
            <div class="api-links">
                <a href="/api/stats">📊 API Stats</a>
                <a href="/api/techniques">🥷 API Techniques</a>
                <a href="/api/health">💓 Health Check</a>
            </div>
        </div>
        
        <footer>
            <p>Built with stealth and precision by Agent-Lumi</p>
            <p style="margin-top: 10px; font-size: 0.9em;">Part of the Ninja CI/CD Showcase</p>
        </footer>
    </div>
</body>
</html>
"""


@app.route('/')
def index():
    """Main dashboard page"""
    stats = ninja.get_stats()
    techniques = skills.list_all_techniques()
    return render_template_string(
        HTML_TEMPLATE,
        stats=stats,
        techniques=techniques,
        skill_level=skills.skill_level
    )


@app.route('/api/stats')
def api_stats():
    """API endpoint for ninja stats"""
    return jsonify(ninja.get_stats())


@app.route('/api/techniques')
def api_techniques():
    """API endpoint for ninja techniques"""
    return jsonify({
        "techniques": skills.list_all_techniques(),
        "skill_level": skills.skill_level
    })


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "stealth_mode": ninja.stealth_mode,
        "clan": ninja.clan_name,
        "timestamp": __import__('time').time()
    })


@app.route('/api/mission', methods=['POST'])
def execute_mission():
    """Execute a ninja mission"""
    from flask import request
    data = request.get_json() or {}
    result = ninja.execute_mission(
        data.get('mission', 'unnamed'),
        data.get('payload', {})
    )
    return jsonify(result)


def create_app():
    """Application factory for testing"""
    return app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)