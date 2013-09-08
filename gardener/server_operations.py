import re

from subprocess import call, Popen, PIPE

from config import SERVER_PORT

python_base = 'backyard/bin/python'
gunicorn_base = 'backyard/bin/gunicorn'

def run_tornado():
    call([python_base,'blow.py'])

def run_testrun():
    call([python_base,'try.py'])

def run_gunicorn(arguments = None):
    option_list = [gunicorn_base,'-b','0.0.0.0:'+str(SERVER_PORT),'fly:app']
    try:
        stop_gunicorn()
        if arguments:
            for item in arguments:
                option_list.append(item)
            call(option_list)
        else:
            call([gunicorn_base,'-b','0.0.0.0:'+str(SERVER_PORT),'-w','4','-k','tornado','fly:app','--daemon'])
    except:
        if arguments:
            for item in arguments:
                option_list.append(item)
            call(option_list)
        else:
            call([gunicorn_base,'-b','0.0.0.0:'+str(SERVER_PORT),'-w','4','-k','tornado','fly:app','--daemon'])

def stop_gunicorn():
    proc = Popen(['ps','aux'], stdout=PIPE)
    output=proc.communicate()[0].split('\n')
    processes = output[2:]
    ids = []
    for item in processes:
        if re.search('gunicorn',item):
            values=[]
            strings = item.split(" ")
            for x in strings:
                if x != "":
                    values.append(x)
            ids.append(values[1])

    ids.sort()
    call(['kill','-9',ids[0]])

# end of file