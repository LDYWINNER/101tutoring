
def packGoldBars(gold):
    bars = 0

    temp = gold * 100
    temp2 = temp % 10
    if temp2 != 0:
        return -1

    if gold >= 1:
        bars += (gold // 1)
        gold -= (gold // 1)
    if gold >= 0.5:
        bars += (gold // 0.5)
        gold -= 0.5
    if gold >= 0.1:
        bars += (gold // 0.1)
        gold -= 0.1 * (gold // 0.1)

    return int(bars)

print(packGoldBars(4.7))
print(packGoldBars(4.25))
print(packGoldBars(10.90))