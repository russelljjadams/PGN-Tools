# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:18:15 2024

@author: rjadams
"""

import chess.pgn
import os

def save_games_to_pgn(games, output_directory, batch_size=100):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    game_count = 0
    batch_number = 1
    pgn_file = None

    for game in games:
        if game_count % batch_size == 0:
            if pgn_file:
                pgn_file.close()
            pgn_file_path = os.path.join(output_directory, f'batch_{batch_number}.pgn')
            pgn_file = open(pgn_file_path, 'w')
            batch_number += 1

        pgn_file.write(str(game) + "\n\n")
        game_count += 1

    if pgn_file:
        pgn_file.close()

def main():
    input_pgn_file = 'polgar.pgn'
    output_directory = './'

    with open(input_pgn_file) as pgn_file:
        pgn = chess.pgn.read_game(pgn_file)

        # Assuming the PGN file contains multiple games
        if pgn:
            games = [pgn]
            while True:
                pgn = chess.pgn.read_game(pgn_file)
                if not pgn:
                    break
                games.append(pgn)

            save_games_to_pgn(games, output_directory)

if __name__ == "__main__":
    main()
