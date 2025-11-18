import json
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime

DATA_FILE = Path.home() / 'hangman_biblico_status.json'

@dataclass
class UserStatus:
    games_played: int = 0
    games_won: int = 0
    total_time_seconds: float = 0.0  # in seconds
    
    def to_json(self):
        return asdict(self)
    
    @classmethod
    def from_json(cls, d):
        return cls(**d)

def load_status() -> UserStatus:
    if not DATA_FILE.exists():
        return UserStatus()
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return UserStatus.from_json(data)
    except Exception:
        return UserStatus()

def save_status(status: UserStatus):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(status.to_json(), f, ensure_ascii=False, indent=2)
    except Exception:
        pass