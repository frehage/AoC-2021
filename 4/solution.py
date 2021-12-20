with open('4/data.txt', 'r') as f:
    # read all the numbers
    numbers = list(map(lambda x: int(x), f.readline().split(',')))
    
    # read all lines and convert rows into lists of numbers
    lines = list(map(lambda x: list(map(lambda y: int(y), x.split())), f.read().splitlines()))
    
    # structure the lines into boards
    boards = [lines[i:i+5] for i in range(1,len(lines),6)]

    # convert each number to its index among the numbers drawn
    boards_indexed = [[list(map(lambda n: numbers.index(n), line)) for line in board] for board in boards]
    # create a transposed matrix to work with collumns
    boards_indexed_transpose = [[[row[i] for row in board] for i in range(5)] for board in boards_indexed]

    # when will each board get bingo if we only consider rows?
    rows_bingo = [ min(list(map(lambda l: max(l), board))) for board in boards_indexed]

    # when will each board get bingo if we only consider collumns?
    cols_bingo = [ min(list(map(lambda l: max(l), board))) for board in boards_indexed_transpose]

    # when will each board get bingo?
    board_bingo = [min(rows_bingo[i], cols_bingo[i]) for i in range(len(boards))]

    # which board will winn and when?
    best_board = board_bingo.index(min(board_bingo))
    worst_board = board_bingo.index(max(board_bingo))
    # best_board = i if best_row[1] < best_col[1] else best_col
    best_board = worst_board

    #final index
    final_index = board_bingo[best_board]

    # final number
    final_number = numbers[final_index]

    # sum of all unmarked numbers
    unmarked_sum = 0
    for row in boards_indexed[best_board]:
        for i in row:
            if i > final_index:
                unmarked_sum += numbers[i]

    # final score
    final_score = final_number * unmarked_sum
    print("final_score: ", final_score)