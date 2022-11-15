import pickle as p

marks = open('marks2.data','rb')
m1 = p.load(marks)
marks.close()

m = m1

class Car():
    color = ' '
    price = 0

class Car():
    def __init__(self, name=0, type_c=0, creator=0, color=0):
        self.name = name
        self.type_c = type_c
        self.creator = creator
        self.color = color
        
    def delete(self):
        self.spisok()
        marks = open('marks2.data','rb')
        m1 = p.load(marks)
        marks.close()
        m = m1
        print('Enter a car number')
        i1 = int(input())
        u = -3
        t = 0 
        while t != i1 :
            u += 3 
            t += 1
        del m[u:u+3]
        f = open('marks2.data','wb+')
        p.dump(m,f)
        f.close()

    def inf(self):
        print('add number')
        print('1) Add car')
        print('2) Show all')
        print('3) Edit car')
        print('4) Delete car')

    def spisok(self):
        marks = open('marks2.data','rb')
        m1 = p.load(marks)
        marks.close()
        m = m1
        print('Car list:')
        i = 1
        o = 0
        while o < len(m):
            if m[o+1] != ' ' and m[o+2] != ' ':
                print(str(i) + ')'+ m[o]+'/'+ m[o+1] + '/'+  m[o+2])
            elif m[o+1] != ' ':
                print(str(i)+ ')'+m[o]+'/'+m[o+1])
            elif m[o+2] != ' ':
                print(str(i) +') '+ m[o]+'/'+m[o+2])
            else:
                print(str(i) +') '+ m[o])
            o+=3
            i +=1
            
    def add(self):
        marks = open('marks2.data','rb')
        m1 = p.load(marks)
        marks.close()
        m = m1

        print('Enter mark')
        r = input()
    
        f = open('marks2.data','wb+')
        p.dump(m+[r]+[' ']+[' '],f)
        f.close()
    

    def edit(self):
        marks = open('marks2.data','rb')
        m1 = p.load(marks)
        marks.close()
        m = m1
        print('What do you want to edit?')
        print('1) Color')
        print('2) Price')
        y = int(input())
        print('Enter a car number')
        self.spisok()
        i1 = int(input())
        u = -3
        t = 0 
        while t != i1 :
            u += 3 
            t += 1
        
        if y == 1 :
            print('Enter a color')
            cl = input()
            m[u+1] = cl
            f = open('marks2.data','wb+')
            p.dump(m,f)
            f.close()
        if y == 2 :
            print('Enter a price')
            pr = str(int(input()))+ '$'
            m[u+2] = pr
            f = open('marks2.data','wb+')
            p.dump(m,f)
            f.close()
 
while True:
    car = Car()
    car.inf()
    i = int(input())
    if i == 1 :
        car = Car()
        car.add()
    if i == 2 :
        car = Car()
        car.spisok()
    if i == 3 :
        car = Car()
        car.edit()
    if i == 4 :
        car = Car()
        car.delete()
