import torch
import torch.nn as nn
import os

torch.set_default_device("cpu")

class BattleshipAI(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 4, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(4, 8, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(8, 1, kernel_size=1)
        )

    def forward(self, x):
        logits = self.conv(x)
        return logits.view(x.size(0), -1)


def call_ai(grid):
    best_model_path = os.path.join(os.path.dirname(__file__), "best_ai.pth")
    if not os.path.exists(best_model_path):
        print("No best_ai.pth found. Please train the model first.")
        return

    # convert to format ai can read
    board = []
    for row in grid:
        new_row = []
        for x in row:
            if x == 1:
                new_row.append(-1)
            elif x<0:
                new_row.append(1)
            else:
                new_row.append(0)
        board.append(new_row)

    # load ai
    ai_state_dict = torch.load(best_model_path, map_location="cpu")
    ai = BattleshipAI().to("cpu")
    ai.load_state_dict(ai_state_dict)
    ai.eval()

    board_size = len(board)
    state = torch.tensor(board, dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # (1,1,H,W)

    # mask played points so it doesnt get stuck in a loop
    flat_board = state.flatten()
    mask = (flat_board == 0)

    # onwards
    logits = ai(state).flatten()
    logits = logits.masked_fill(~mask, float('-inf'))
    probs = torch.softmax(logits, dim=-1)
    dist = torch.distributions.Categorical(probs)
    action = dist.sample()

    row, col = divmod(action.item(), board_size)
    return [row, col]


