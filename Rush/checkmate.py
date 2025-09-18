def checkmate(board_str):
    # Parse rows safely (ignore empty lines, strip trailing spaces)
    rows = [list(r.rstrip()) for r in board_str.splitlines() if r.strip()]
    n = len(rows)

    # Validate: must be square
    if n == 0 or any(len(r) != n for r in rows):
        print("Error")
        return

    # Validate: exactly one King
    king_positions = [(r, c) for r in range(n) for c in range(n) if rows[r][c] == "K"]
    if len(king_positions) != 1:
        print("Error")
        return

    kr, kc = king_positions[0]

    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    knight_moves = [
        (2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)
    ]
    # ✅ Pawns can attack both upward and downward
    pawn_moves = [(-1,-1), (-1,1), (1,-1), (1,1)]

    # Rooks & Queens
    for dr, dc in rook_dirs:
        r, c = kr+dr, kc+dc
        while in_bounds(r, c):
            piece = rows[r][c]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # Bishops & Queens
    for dr, dc in bishop_dirs:
        r, c = kr+dr, kc+dc
        while in_bounds(r, c):
            piece = rows[r][c]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # Knights
    for dr, dc in knight_moves:
        r, c = kr+dr, kc+dc
        if in_bounds(r, c) and rows[r][c] == 'N':
            print("Success")
            return

    # Pawns
    for dr, dc in pawn_moves:
        r, c = kr+dr, kc+dc
        if in_bounds(r, c) and rows[r][c] == 'P':
            print("Success")
            return

    print("Fail")
