#Writes and/or creates the file
def create_file(x):
    f_name = input = raw_input('What is the day?: ')
    f_write = open(f_name + '.txt', 'a')
    f_write.write('\n' + x)
    f_write.close()

#Gathers the days info
def get_milk():
    time_of_day =input = raw_input("What Time?: ")
    start_oz = input = raw_input('Starting Oz?: ')
    end_oz =  input = raw_input('Any ounces left?: ')
    total_oz = int(start_oz) - int(end_oz)
    statement=  '\nAt ' + time_of_day + '\nWe started with ' + str(start_oz) + 'Ounces' + '\nThen we finished with ' + str(end_oz) + 'Ounces'+ '\nHe Drank ' + str(total_oz) + ' Ounces' 
    return(statement)

def main():
    create_file(get_milk())

main()
