from subprocess import call

python_base = 'env/bin/python'

def run_tornado():
    call([python_base,'blow.py'])

def run_testrun():
    call([python_base,'try.py'])

# end of file