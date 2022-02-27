import deep_q_network
import py_2048
from play_game import show_board
from IPython.display import clear_output

import torch.nn as nn
from torch import optim
import torch

def average_score(ai,n):
    sum =0
    for i in range(n):
        ai.game.reset()
        while(not py_2048.is_end(ai.game.board)):
            ai.action()
        sum += ai.game.score
    print(sum/n)

n_mid1 = 2048
n_mid2 = 1024
net = deep_q_network.Net(n_mid1,n_mid2)

# 読み込み
load_path = './model/model_2000_Adam.pth'
load_weights = torch.load(load_path)
net.load_state_dict(load_weights)

loss_fnc = nn.MSELoss()
optimizer = optim.RMSprop(net.parameters(), lr=0.01)  # 最適化アルゴリズム

brain = deep_q_network.Brain(net,loss_fnc,optimizer)
game = py_2048.Game()
ai = deep_q_network.Ai(brain,game)

for i in range(10):
    ai.game.reset()
    while(not py_2048.is_end(ai.game.board)):
        ai.action()
    clear_output(wait=False)
    show_board(ai.game)

# average_score(ai,1000)