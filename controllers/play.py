from subprocess import Popen
from subprocess import call

def mp3():
    filename = request.vars['filename']
    volume = request.vars['volume']
    Popen(["mpg321", "/home/pi/web2py/applications/leeroy/static/mp3/" + filename])
    return "Yay"
    
def volume():
    v = request.vars['v']
    call(["amixer", "cset", "numid=1", "--", v + "%"])
    Popen(["mpg321", "/home/pi/leeroy.mp3"])
    return "done"
     