import chess.pgn

def parse_pgn(input_file, output_white, output_black):
    with open(input_file, 'r') as pgn_file:
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break
            
            # Extract FEN and determine whose move it is
            fen = game.board().fen()
            turn = 'w' if game.board().turn == chess.WHITE else 'b'

            # Create a new PGN file based on the turn
            output_file = output_white if turn == 'w' else output_black

            with open(output_file, 'a') as output_pgn:
                # Write the entire PGN to the output file
                output_pgn.write(str(game) + "\n\n")

if __name__ == "__main__":
    # Replace 'input.pgn', 'output_white.pgn', and 'output_black.pgn' with your file paths
    input_pgn_file = 'middlegames.pgn'
    output_white_pgn_file = 'middlegames_white.pgn'
    output_black_pgn_file = 'middlegames_black.pgn'

    # Parse the PGN file and create separate PGNs for White's and Black's move
    parse_pgn(input_pgn_file, output_white_pgn_file, output_black_pgn_file)
