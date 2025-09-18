def checkmate(board_str):
    # แยกแถว (เว้นบรรทัดว่าง, ตัดช่องว่างด้านท้าย)
    rows = [list(r.rstrip()) for r in board_str.splitlines() if r.strip()]
    n = len(rows)

    # ตรวจสอบว่าเป็นตารางจัตุรัส
    if n == 0 or any(len(r) != n for r in rows):
        print("Error")
        return

    # ตรวจสอบว่ามี King เพียงตัวเดียว
    king_positions = [(r, c) for r in range(n) for c in range(n) if rows[r][c] == "K"]
    if len(king_positions) != 1:
        print("Error")
        return

    # กำหนดตำแหน่ง King
    kr, kc = king_positions[0]

    # คืนค่า True ถ้าอยู่ในกระดาน, False ถ้าอยู่นอกกระดาน
    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    # Rook เคลื่อนแนวตั้ง/แนวนอน
    rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    # Bishop เคลื่อนแนวทแยง
    bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    # Knight เคลื่อนแบบตัว L
    knight_moves = [
        (2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)
    ]
    # Pawn โจมตีแนวทแยง ทั้งขึ้นและลง
    pawn_moves = [(-1,-1), (-1,1), (1,-1), (1,1)]

    # ตรวจสอบ Rook กับ Queen
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

    # ตรวจสอบ Bishop กับ Queen
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

    # ตรวจสอบ Knight
    for dr, dc in knight_moves:
        r, c = kr+dr, kc+dc
        if in_bounds(r, c) and rows[r][c] == 'N':
            print("Success")
            return

    # ตรวจสอบ Pawn
    for dr, dc in pawn_moves:
        r, c = kr+dr, kc+dc
        if in_bounds(r, c) and rows[r][c] == 'P':
            print("Success")
            return

    print("Fail")
