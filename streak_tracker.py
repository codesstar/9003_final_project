import os
from datetime import date, timedelta

class StreakTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.streak, self.last_date = self.load_streak()

    def load_streak(self):
        if not os.path.exists(self.file_path):
            return 0, None
        with open(self.file_path, 'r') as f:
            lines = f.read().split(',')
            return int(lines[0]), date.fromisoformat(lines[1])

    def save_streak(self):
        with open(self.file_path, 'w') as f:
            f.write(f"{self.streak},{self.last_date.isoformat()}")

    def update_streak(self):
        today = date.today()
        if self.last_date is None or today == self.last_date:
            print("Streak unchanged.")
        elif today == self.last_date + timedelta(days=1):
            self.streak += 1
            print(f"🔥 Streak extended! You're on a {self.streak}-day streak!")
        else:
            self.streak = 1
            print("🌱 Streak restarted. Let's build it up again!")
        self.last_date = today
        self.save_streak()

    def view_streak(self):
        print(f"📆 Current streak: {self.streak} day(s)")
