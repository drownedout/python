"""
Given a target amount n and a list(array) of distinct coin values,
what's the fewest coins needed to make the change amount.

For example:

	- If n = 10 and coins = [1,5,10]. Then there are four possible ways
	to make change:

		- 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
		- 5 + 1 + 1 + 1 + 1 + 1
		- 5 + 5
		- 10

	With 1 coin being the minimum.

"""

# Not efficient since it produces A LOT of recursive calls


def coin_change(amount, coins):

    # Default value
    minimum_coins = amount

    # Checks to see if the target amount is in coins - Base case
    if amount in coins:
        return 1

    else:

        # For every coin value that is less than or equal to
        # the target amount.

        for i in [coin for coin in coins if coin <= amount]:
            # Add a coin count + recursive call
            number_of_coins = 1 + coin_change(amount - i, coins)

            # Reset minimum if the new number of coins is less
            # than the inital minimum
            if number_of_coins < minimum_coins:
                minimum_coins = number_of_coins

    return minimum_coins

# Dynamic programming solution


def dynamic_coin_change(amount, coins, known_results):

    # Default value
    minimum_coins = amount

    # Base case
    if amount in coins:
        known_results[amount] = 1
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_results[amount] > 0:
        return known_results[amount]

    else:
        # For every coin value that is <= amount
        for i in [coin for coin in coins if coin <= amount]:
            # Recursive call, we also include known results
            number_of_coins = 1 + \
                dynamic_coin_change(amount - i, coins, known_results)

            # Reset minimum if we have a new one
            if number_of_coins < minimum_coins:
                minimum_coins = number_of_coins

                # Reset the known result
                known_results[amount] = minimum_coins

    return minimum_coins


known_results = [0] * (15 + 1)  # Hardcoding for dynamic coin change function

print(coin_change(15, [1, 5, 10]))
print(dynamic_coin_change(15, [1, 5, 10], known_results))
