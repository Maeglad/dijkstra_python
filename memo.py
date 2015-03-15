"""
  musim skusit ako to funguje
  podle online helpu by to malo ulozit vysledok do mema dictu a potom ho vratit
"""
def memo(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper
