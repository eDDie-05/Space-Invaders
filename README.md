# Space Invaders — Python

A simple Space Invaders-inspired arcade game written in Python with Pygame.

## Features
- Player-controlled ship
- Enemy formation and movement
- Projectile firing
- Collision handling
- Score tracking

## Requirements
- Python 3.9 or newer
- Pygame

## Run locally
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install pygame
python space.py
```

## Controls
- Left / Right arrows: move the player
- Space: fire
- Close the game window: exit

## Project files
- `space.py` — game loop, player, enemies, projectiles and scoring

## Current scope
A local learning project. Add tests for collision cases, difficulty progression and restart behavior before a formal release.
