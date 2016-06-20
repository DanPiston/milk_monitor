milk_entry = {'Time of Day': '',
              'Starting Oz': '',
              'Ending Oz': '',
              'Total Oz': ''}


def get_milk():
    
    time_of_day =input = raw_input("What Time?: ")
    start_oz = input = raw_input('Starting Oz?: ')
    end_oz =  input = raw_input('Finishing Oz?: ')
    total_oz = int(start_oz) - int(end_oz)
    print('\nAt ' + time_of_day + '\nWe started with ' + str(start_oz) + '\nThen we finished with ' + str(end_oz) + '\nHe Drank ' + str(total_oz))

def main():
    get_milk()

main()
