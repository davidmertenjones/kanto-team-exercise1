
#from question_file import determine_board_state

#test 1: player 1 wins with top row
def test_player1_wins_top_row():
    print("\nTest 1: Player 1 wins with top row")
    board = [[1, 1, 1],
             [0, 2, 0],
             [2, 0, 0]]
    result = determine_board_state(board)
    assert result == True, "Should return True for Player 1 win"
    print("Test passed.\n")

#test 2: player 2 wins with central column
def test_player2_wins_central_column():
    print("Test 2: Player 2 wins with central column")
    board = [[0, 2, 1],
             [0, 2, 0],
             [1, 2, 1]]
    result = determine_board_state(board)
    assert result == True, "Should return True for Player 2 win"
    print("Test passed.\n")

#test 3: no winner
def test_no_winner():
    print("Test 3: No winner scenario")
    board = [[1, 2, 1],
             [2, 1, 2],
             [2, 1, 2]]
    result = determine_board_state(board)
    assert result == False, "Should return False for no winner"
    print("Test passed.\n")

#test 4: both players win (player 1 should be declared winner)
def test_both_players_win():
    print("Test 4: Both players win scenario")
    board = [[1, 1, 1],
             [2, 2, 2],
             [0, 0, 0]]
    result = determine_board_state(board)
    assert result == True, "Should return True for Player 1 win when both win"
    print("Test passed.\n")

# Run tests
test_player1_wins_top_row()
test_player2_wins_central_column()
test_no_winner()
test_both_players_win()


