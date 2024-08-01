from Card import Card

def make_card(n):
    try:
        return Card(n)
    except Exception as e:
        print("invalid card: ", e)
        return None