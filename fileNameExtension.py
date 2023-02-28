fl=input('Enter file name with extension(Valid file name): ')
try: 
    fl=fl.split('.')
except: 
    print('Invalid file name')
print('You entered a ',fl[1],'File Name')