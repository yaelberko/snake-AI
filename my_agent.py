import random
import numpy as np
from game import SnakeGameAI, Direction, Point

class HeuristicAgent:
    def __init__(self):
        self.n_games = 0

    def get_state(self, game):
        head = game.snake[0]
        food = game.food
        direction = game.direction

        # מיקום של אוכל ביחס לראש
        food_dir = [
            food.x < head.x,  # אוכל משמאל
            food.x > head.x,  # אוכל מימין
            food.y < head.y,  # אוכל למעלה
            food.y > head.y   # אוכל למטה
        ]
        return food_dir, direction

    def get_action(self, food_dir, direction, game):
        action = [1, 0, 0]  # ברירת מחדל: ישר

        directions = [Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN]
        safe_moves = []

        for move in [[1,0,0], [0,1,0], [0,0,1]]:
            temp_dir = self._get_new_direction(direction, move)
            temp_head = self._get_new_head(game.head, temp_dir)
            if not game.is_collision(temp_head):
                safe_moves.append((move, temp_dir))

        for move, dir in safe_moves:
            if (dir == Direction.RIGHT and food_dir[1]) or \
               (dir == Direction.LEFT and food_dir[0]) or \
               (dir == Direction.UP and food_dir[2]) or \
               (dir == Direction.DOWN and food_dir[3]):
                return move

        if safe_moves:
            return random.choice(safe_moves)[0]

        return action

    def _get_new_direction(self, current_direction, move):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(current_direction)

        if np.array_equal(move, [1, 0, 0]):
            return clock_wise[idx]
        elif np.array_equal(move, [0, 1, 0]):
            return clock_wise[(idx + 1) % 4]
        else:
            return clock_wise[(idx - 1) % 4]

    def _get_new_head(self, head, direction):
        x, y = head.x, head.y
        if direction == Direction.RIGHT:
            x += 20
        elif direction == Direction.LEFT:
            x -= 20
        elif direction == Direction.DOWN:
            y += 20
        elif direction == Direction.UP:
            y -= 20
        return Point(x, y)

def run_heuristic_ai():
    agent = HeuristicAgent()
    game = SnakeGameAI()
    while True:
        food_dir, direction = agent.get_state(game)
        action = agent.get_action(food_dir, direction, game)
        reward, done, score = game.play_step(action)

        if done:
            print('Game Over. Score:', score)
            break

if __name__ == '__main__':
    run_heuristic_ai()
