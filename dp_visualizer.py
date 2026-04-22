# dp_visualizer.py

# -------------------------------
# 1. RECURSION
# -------------------------------
rec_calls = 0

def fib_rec(n):
    global rec_calls
    rec_calls += 1

    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


# -------------------------------
# 2. MEMOIZATION (Top-Down DP)
# -------------------------------
memo_calls = 0

def fib_memo(n, dp):
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp)
    return dp[n]


# -------------------------------
# 3. TABULATION (Bottom-Up DP)
# -------------------------------
def fib_tab(n):
    if n <= 1:
        return n, [n]

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n], dp


# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":
    n = int(input("Enter n: "))

    # Recursion
    global rec_calls
    rec_calls = 0
    rec_result = fib_rec(n)

    # Memoization
    global memo_calls
    memo_calls = 0
    dp = [-1] * (n + 1)
    memo_result = fib_memo(n, dp)

    # Tabulation
    tab_result, table = fib_tab(n)

    print("\n--- Results ---")
    print(f"Recursion Result: {rec_result}, Calls: {rec_calls}")
    print(f"Memoization Result: {memo_result}, Calls: {memo_calls}")
    print(f"Tabulation Result: {tab_result}")

    print("\nDP Table (Tabulation):")
    print(table)