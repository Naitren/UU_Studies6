immutable_var=(1, True, 'string')
print (immutable_var)
#immutable_var[0]=200 - нельзя изменить, потому что элементы кортежа не меняются.'
mutable_list = [1, True, 'string']
print(mutable_list)
mutable_list[1]=False
print(mutable_list)


