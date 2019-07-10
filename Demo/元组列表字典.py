# dariy_section=['milk','water','tp','ep'];
# milk_exp=('1988','12','28');
# milk_car={};
# milk_car['exp_data']=milk_exp;
# milk_car['fl_oz']=5;
# milk_car['cost']=10;
# milk_car['b_name']='ppppp';
# cheeses=['asdfghjjkl','B','C'];
# dariy_section.append(cheeses);
# print('This milk carton will exp on %s\\%s\\%s' % (milk_exp[0],milk_exp[1],milk_exp[2]));
# 'print(dariy_section[0]+dariy_section[len(dariy_section)-1])';
# print('the 6 milk cost %d' %(6*milk_car['cost']));    '取得字典内cost的键值'
# print(dariy_section);
# dariy_section.pop();
# print(dariy_section);
# print(cheeses[0][0:5]);
def t(*k):
    for i in k:
        yield from i

if __name__=='__main__':
    s = ['a','b','c']
    b = [1,2,3]
    a = [4,5,6]
    print(list(t(b,s,a)))
