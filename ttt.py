import streamlit as st
import numpy as np

# Initialize game state
def initialize_game():
    return np.zeros((3, 3), dtype=int), 1, "Player X's turn"

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if len(set(board[i, :])) == 1 and board[i, 0] != 0:
            return board[i, 0]
        if len(set(board[:, i])) == 1 and board[0, i] != 0:
            return board[0, i]

    if len(set([board[i, i] for i in range(3)])) == 1 and board[0, 0] != 0:
        return board[0, 0]
    if len(set([board[i, 2 - i] for i in range(3)])) == 1 and board[0, 2] != 0:
        return board[0, 2]

    return 0

def main():
    st.title("Tic Tac Toe")

    # Initialize game state
    if 'board' not in st.session_state:
        st.session_state.board, st.session_state.turn, st.session_state.message = initialize_game()

    # Display game board
    board = st.session_state.board
    st.write(st.session_state.message)

    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            button_label = ""
            if board[i, j] == 1:
                button_label = "X"
            elif board[i, j] == 2:
                button_label = "O"
                
            if cols[j].button(button_label, key=f"{i}-{j}"):
                if board[i, j] == 0:
                    st.session_state.board[i, j] = st.session_state.turn
                    st.session_state.turn = 3 - st.session_state.turn  # Switch turn
                    winner = check_winner(st.session_state.board)
                    if winner != 0:
                        st.session_state.message = "Player X wins!" if winner == 1 else "Player O wins!"
                    elif np.all(st.session_state.board != 0):
                        st.session_state.message = "It's a tie!"
                    else:
                        st.session_state.message = "Player X's turn" if st.session_state.turn == 1 else "Player O's turn"
                st.rerun()  # Refresh the page to update the board

    # Display game message
    if st.session_state.message in ["Player X wins!", "Player O wins!", "It's a tie!"]:
        st.write(st.session_state.message)
        if st.button("Restart Game"):
            st.session_state.board, st.session_state.turn, st.session_state.message = initialize_game()

if __name__ == "__main__":
    main()
