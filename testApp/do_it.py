
import sys

def do_it1(who):
    print ("I am doing it to %s"% who)
    return who
    
def run(args):
    for a in args:
        do_it1(a)

if __name__ == "__main__":
    run(sys.argv)
    
    