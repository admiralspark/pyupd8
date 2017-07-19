import pip

UPDATELIST = pip.main(['list', '--outdated', '--format=columns'])

for line in str(UPDATELIST):
    '''
    line = line.strip() #remove \n if there
    pip.main(['install', line, '--upgrade'])
    '''
    print(line)