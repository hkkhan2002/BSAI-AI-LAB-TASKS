def minimax(depth, i, is_max, vals, last, count):
    if depth == last:
        count[0] = count[0] + 1
        return vals[i]
    if is_max:
        left = minimax(depth + 1, i * 2, False, vals, last, count)
        right = minimax(depth + 1, i * 2 + 1, False, vals, last, count)
        if left > right:
            return left
        return right
    left = minimax(depth + 1, i * 2, True, vals, last, count)
    right = minimax(depth + 1, i * 2 + 1, True, vals, last, count)
    if left < right:
        return left
    return right


def alphabeta(depth, i, is_max, vals, last, alpha, beta, count):
    if depth == last:
        count[0] = count[0] + 1
        return vals[i]
    if is_max:
        value = -9999
        for k in range(2):
            result = alphabeta(depth + 1, i * 2 + k, False, vals, last, alpha, beta, count)
            if result > value:
                value = result
            if value > alpha:
                alpha = value
            if alpha >= beta:
                break
        return value
    value = 9999
    for k in range(2):
        result = alphabeta(depth + 1, i * 2 + k, True, vals, last, alpha, beta, count)
        if result < value:
            value = result
        if value < beta:
            beta = value
        if alpha >= beta:
            break
    return value


def main():
    scores = [3, 5, 2, 9, 0, 7, 0, 0]
    depth = 3

    count1 = [0]
    print('Minimax value:', minimax(0, 0, True, scores, depth, count1))
    print('Minimax leaves checked:', count1[0])

    count2 = [0]
    print('Alpha-beta value:', alphabeta(0, 0, True, scores, depth, -9999, 9999, count2))
    print('Alpha-beta leaves checked:', count2[0])

    reordered = [3, 5, 2, 9, 0, 0, 0, 7]
    count3 = [0]
    print('Reordered minimax value:', minimax(0, 0, True, reordered, depth, count3))
    print('Reordered minimax leaves checked:', count3[0])

    count4 = [0]
    print('Reordered alpha-beta value:', alphabeta(0, 0, True, reordered, depth, -9999, 9999, count4))
    print('Reordered alpha-beta leaves checked:', count4[0])


if __name__ == '__main__':
    main()
