# 2-Player Obstacle Game in Pygame

This is a two-player competitive obstacle course game built using Python and Pygame.

Players race to reach the green **finish** area while avoiding moving and static walls. First player to reach the finish **3 times wins** the game!

---

## 🎮 Gameplay

- **Player 1 controls:**
  - `W` = up
  - `S` = down
  - `A` = left
  - `D` = right

- **Player 2 controls:**
  - `↑` = up
  - `↓` = down
  - `←` = left
  - `→` = right

- Avoid hitting red walls. If you do, you're pushed back!
- Dynamic walls (`w7`, `w10`, `w11`) move up/down or shrink/expand over time.
- When a player touches the green square at the bottom, they score 1 point.
- First to 3 points wins!
- The game tracks and displays the **fastest time to reach the goal**.

---

## 🛠️ How to Run

1. Make sure Python 3 is installed.
2. Install Pygame if needed:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

## 🧠 Features

- Two-player support
- Dynamic and static obstacles
- Collision detection and movement reversal
- Real-time timer and best time tracking
- Game end screen

---

## 📂 Files

- `main.py` – The main game logic
- `README.md` – This file

---

## 📜 License

This project is open source and free to use for educational purposes.
