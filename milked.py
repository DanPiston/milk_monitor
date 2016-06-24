from milklogentry import MilkLogEntry

def main():
    starting_ounces = input('Starting Ounces: ')
    entry = MilkLogEntry(starting_ounces)

    ending_ounces = input('Ending Ounces: ')
    entry.set_ending_ounces(ending_ounces)

    total = entry.amount_consumed

    print ('The baby drank {} ounces!'.format(entry.amount_consumed))

    entry.log_db(starting_ounces, ending_ounces, total)
    
if __name__ == '__main__':
    main()
