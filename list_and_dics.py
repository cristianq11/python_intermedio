def run():
    my_list= [1,'hello',4.5]
    my_dict = {'firstname': 'cristian', 'lastname': 'Quiroz'}
    
    super_list = [
        {'firstname': 'cristian', 'lastname': 'Quiroz'},
        {'firstname': 'caren', 'lastname': 'Salas'},
        {'firstname': 'pepe', 'lastname': 'cardona'},
        {'firstname': 'carlos', 'lastname': 'oquendo'}
    ]

    super_dict = {
        'natural_num': [1,2,3,4,5,6,7,8,9,10],
        'integer_nums':[-1,-2,-3,-4,-5,-6,-7,-8,-9,0],
        'floating_nums':[1.5,2.3,3.4,4.5,5.6,6.7,7.8,9.1]
        
    }


    for key,value in super_dict.items():
        print(key, '-', value )

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])



































if __name__=='__main__':
    run()