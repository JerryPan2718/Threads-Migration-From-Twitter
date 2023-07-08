import os
import sys 

from threads import Threads

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py INSTAGRAM_USERNAME INSTAGRAM_PASSWORD")
        sys.exit(1)
    
    instagram_username = sys.argv[1]
    instagram_password = sys.argv[2]

    # Set the environment variables
    os.environ['INSTAGRAM_USERNAME'] = instagram_username
    os.environ['INSTAGRAM_PASSWORD'] = instagram_password


    print(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))
    threads = Threads()
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))
    threads.dump_settings('./data/session.json')

    user = threads.get_user_by_username(username='zuck')
    print(user)

