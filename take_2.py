import time

def gen(file_name):
    with open(file_name) as file:
        for line in file:
            yield line

def make_dictionary(file_name):
    global start 
    start = time.time()
    dictionary_test = {}
    for line in gen(file_name):
            
            city, temp = line.split(';')
            temp = float(temp.strip())
            if city not in dictionary_test:
                    ### max, min, sum, loop
                    dictionary_test[city] = [temp,temp,temp,1]

            elif city in dictionary_test:
                dictionary_test[city][2] = dictionary_test[city][2] + temp
                dictionary_test[city][3] += 1
                ### if the number stored is less than the iteration put it in the max column.
                if dictionary_test[city][0] < temp:
                    dictionary_test[city][0] = temp
                elif dictionary_test[city][1] > temp:
                     dictionary_test[city][1] = temp

    make_avg(dictionary_test)

def make_avg(dictionary):
    for city in dictionary:
        dictionary[city][2] = round(dictionary[city][2]/dictionary[city][3], 1)
        dictionary[city][2]
        dictionary[city].pop(3)
    print_to_file(dictionary)

def print_to_file(data):
     with open("wdict.txt","w") as log_data:
        for city in data:
            output = "{};{};{};{}\n".format(city,data[city][0],data[city][1],data[city][2])
            log_data.write(output)

make_dictionary('300mil.txt')
end = time.time()
print(end-start)

