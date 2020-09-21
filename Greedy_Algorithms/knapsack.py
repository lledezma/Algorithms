def change(cents):
	coins = [25,10,5,1]
	num_of_coins = 0
	for coin in coins:
		num_of_coins+= math.floor(cents/coin)
		cents = cents%coin
		if cents == 0:
			break
	print(num_of_coins)

# change(33)