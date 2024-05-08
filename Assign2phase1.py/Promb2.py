"""Task-1: Winner Winner Chocolate Dinner ! "
Starting with n chocolates in a bowl, Two players take turns in order to remove them from the
bowl. They can either take one or two chocolates in each turn, and the player who removes the
last chocolates wins entire bowl of chocolate.
Imagine that the first player decides to remove a single Chocolate in each turn, while the second
player withdraws one Chocolate if the number of chocolates left in the bowl are odd return-1, and
-2 if it is even.
Make Two Functions for Player_1 and Player_2 and call them recursively in such a way that both
handle each others strategy."""

def player_1(choco):
    if choco <= 0:
        return -1
    elif choco % 2 == 0:
        return -2
    else:
        return player_2(choco - 1)


def player_2(choco):
    if choco <= 0:
        return 1
    elif choco % 2 != 0:
        return -1
    else:
        return player_1(choco - 2)


def play(n):
    winner = player_1(n)
    if winner == 1:
        print("Player 1 : Winner Winner Chocolate Dinner ! ")
    else:
        print("Player 2 : Winner Winner Chocolate Dinner ! ")


play(15)