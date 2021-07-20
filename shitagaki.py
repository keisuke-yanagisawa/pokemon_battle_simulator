from subprocess import Popen, PIPE

class PokemonShowdown(object):
    def __init__(self, path):
        #path = path to pokemon_showdown
        self.path = path

        self.proc = Popen([path, "simulate-battle"], stdin=PIPE, stdout=PIPE)

    def _input(self, string):
        self.proc.stdin.write(string.encode())
        self.proc.stdin.write("\n".encode())
        self.proc.stdin.flush()
        

    def start(self, formatid):
        self._input(f'>start {"formatid":"{formatid}"}')
        ret = [proc.stdout.readline for _ in range(3)] # read 3 lines
        return ret
        
    def act(self, player_id, action, *args, **kwargs):
        # 参加している人数分だけ動かす必要あり。まあとりあえず2人前提でいいか。

        # >p1 move Hidden Power
        # >p2 move Close Combat

        ret = []
        while(True):
            ret.append(proc.stdout.readline())
            if(ret[-1].startswith("|turn|")):
                break

        return ret
