def is_winning_ticket(tickett):
    if len(tickett) != 20:
        return "invalid ticket"

    left_part = tickett[:10]
    right_part = tickett[10:]
    winning_symbols = ['@', '#', '$', '^']

    for symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            symbol_repetitions = symbol * repetition

            if symbol_repetitions in left_part and symbol_repetitions in right_part:
                if repetition == 10:
                    return (f'ticket "{tickett}" - {repetition}{symbol} Jackpot!')
                else:
                    return (f'ticket "{tickett}" - {repetition}{symbol}')

    return f'ticket "{tickett}" - no match'


data = input().split(', ')
collection_of_tickets = [ticket.strip() for ticket in data]

for single_ticket in collection_of_tickets:
    print(is_winning_ticket(single_ticket))
