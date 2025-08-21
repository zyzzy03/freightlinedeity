# box drawing copy-and-paste ref
# ┍  ┓ ┕ ┛ ┡  ┩ ┅   ━

class asciiSeperators:
    def LineOpen():
        # prints a simple starting line
        print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")

        # prints a mid line
    def LineMid():
        print("┣ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ┫")

        # prints a mid line
    def LineEnd():
        print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")



class asciiRicing:
    # memory leaks galore!
    def title(RicingLocation):
        ricing = open(RicingLocation)
        print(ricing.read())

    def lister(Array):
        for i in range(len(Array)):
            print("| ", Array[i])