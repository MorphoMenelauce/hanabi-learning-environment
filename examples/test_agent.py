#!/usr/bin/env python3
from __future__ import print_function

from hanabi_learning_environment import rl_env
from hanabi_learning_environment.agents.simple_agent import SimpleAgent
from hanabi_learning_environment.agents.beta_agent import BetaAgent

# config du jeu
config = {"players": 2, "random_start_player": True}

#
game = rl_env.HanabiEnv(config)

#
agents = [BetaAgent(config), BetaAgent(config)]

print(""""starting the game""")

# reset game
obs = game.reset()
done = False

while not done:
    current_player = obs['current_player']

    actions = [agents[ind].act(obs_p1) for ind, obs_p1 in enumerate(obs['player_observations'])]

    # displaye current game action

    player = obs['current_player']

    print(obs['player_observations'][player]['pyhanabi'])
    print("\n#> Player", player, "joue", actions[current_player], "\n\n")

    obs, rew, done, info = game.step(actions[current_player])

    if done:
        result = sum(obs['player_observations'][current_player]['fireworks'].values())
        if obs['player_observations'][0]['life_tokens'] == 0:
            result = 0
        print("#> Resultat final : ", result, "/25")
