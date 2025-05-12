import chess

def mostrar_tabuleiro(tabuleiro):
    print(tabuleiro)

def jogar():
    tabuleiro = chess.Board()
    mostrar_tabuleiro(tabuleiro)
    
    while not tabuleiro.is_game_over():
        movimento = input("\nDigite seu movimento (ex: e2e4): ")
        
        if chess.Move.from_uci(movimento) in tabuleiro.legal_moves:
            tabuleiro.push(chess.Move.from_uci(movimento))
            mostrar_tabuleiro(tabuleiro)
        else:
            print("Movimento inválido. Tente novamente.")
    
    print("\nJogo finalizado!")
    
jogar()
