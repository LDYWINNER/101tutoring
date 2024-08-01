
def person_income(data, name):
    people = data.split('#')
    info = []
    for person in people:
        info.append(person.split())
    #print(info)
    sum = 0
    for i in info:
        if i[0] == name:
            temp = i[1].split(',')
            for num in temp:
                sum += float(num)
    if sum == 0:
        return None
    return sum


data1 = 'Jack 123,129.8,23.5#Bob 1234#Chris 1,2,3,4#Susie 34.5,0.8,99.9'
data2 = 'Cate 5.3,9.2,32.1,5,11#Daisy 98.2,152.3,5.22,87.15#Abe 51,88.7774#Frank 66,22,34,56,71.12'

print(person_income(data1, 'Jack')) #276.3
print(person_income(data1, 'Bob')) #1234.0
print(person_income(data1, 'Chris')) #10.0
print(person_income(data1, 'Susie')) #135.2
print(person_income(data2, 'Abe')) #139.7774
print(person_income(data2, 'Billy')) #None
print(person_income(data2, 'Cate')) #62.6
print(person_income(data2, 'Daisy')) #342.87
print(person_income(data2, 'Erin')) #None
print(person_income(data2, 'Frank')) #249.12