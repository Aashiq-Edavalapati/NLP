def editDist(X, m, Y, n):
    """
        Finds Levenshtein distance between string 'X' and 'Y'.

        Args:
            X -> 
            m ->
            Y ->
            n ->
    """
    # Case 1(Base Case): Empty strings
    if m == 0:
        return n
    
    if n == 0:
        return m
    
    # Case 2: If the characters are match, then 
    cost = 0 if (X[m - 1] == Y[n - 1]) else 1

    return min(editDist(X, m - 1, Y, n) + 1,       # deletion (case 3a)
               editDist(X, m, Y, n - 1) + 1,       # insertion (case 3b)
               editDist(X, m - 1, Y, n - 1) + cost # substitution (case 2 + 3c)
              )

if __name__ == '__main__':
    X = 'kitten'
    Y = 'sitting'

    print(f'Levenshtein Distance between {X} and {Y} is {editDist(X, len(X), Y, len(Y))}')