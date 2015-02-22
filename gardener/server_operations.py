from subprocess import call

python_base = 'env/bin/python'
gunicorn_base = 'env/bin/gunicorn'

def run_tornado():
    call([python_base,'blow.py'])

def run_testrun():
    call([python_base,'try.py'])

# end of file