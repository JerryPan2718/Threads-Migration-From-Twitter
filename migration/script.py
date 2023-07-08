import os

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    threads.login(os.environ.get('jerry.pan.jp'), os.environ.get('Jx011024'))
    threads.dump_settings('../data/session.json')

