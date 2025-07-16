def editDist(X, m, Y, n):
    """
    Calculates the Levenshtein distance between two strings X and Y.
    The Levenshtein distance is the minimum number of single-character
    edits (insertions, deletions, or substitutions) required to change one
    word into the other.

    Args:
        X (str): First string
        m (int): Length of the first string (can be len(X))
        Y (str): Second string
        n (int): Length of the second string (can be len(Y))

    Returns:
        int: The Levenshtein distance between X and Y
    """

    # Base Case 1: If first string is empty, the only option is to insert all characters of second string
    if m == 0:
        return n

    # Base Case 2: If second string is empty, the only option is to remove all characters of first string
    if n == 0:
        return m

    # Check if the last characters of both substrings match
    # If they do, cost = 0 (no edit needed), else cost = 1 (substitution needed)
    cost = 0 if X[m - 1] == Y[n - 1] else 1

    # Recursively compute the minimum of three operations:
    # 1. Deletion from X
    # 2. Insertion into X (or deletion from Y)
    # 3. Substitution of the last character if they are different
    return min(
        editDist(X, m - 1, Y, n) + 1,       # Deletion
        editDist(X, m, Y, n - 1) + 1,       # Insertion
        editDist(X, m - 1, Y, n - 1) + cost # Substitution
    )

def editDistDP(X, Y):
    """
    Calculates the Levenshtein distance between two strings X and Y using Dynamic Programming.

    Args:
        X (str): First string
        Y (str): Second string

    Returns:
        int: The Levenshtein distance between X and Y
    """
    m = len(X)
    n = len(Y)

    # Create a 2D DP table where dp[i][j] represents the edit distance
    # between the first i characters of X and first j characters of Y
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from X
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters of Y

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                cost = 0  # No operation needed if characters match
            else:
                cost = 1  # Substitution needed

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    return dp[m][n]

if __name__ == '__main__':
    X = 'kitten'
    Y = 'sitting'

    print(f'Levenshtein Distance between "{X}" and "{Y}" is {editDistDP(X, Y)}')
    print(f'Levenshtein Distance between "{X}" and "{Y}" is {editDist(X, len(X), Y, len(Y))}')