import pickle


with open("level5.dat") as f:
    symbols =pickle.load(f)

    with open("level5_out.dat", "w") as fout:

        def expand(symbols):
            for sym in symbols:
                if isinstance(sym, list):
                    expand(sym)
                elif isinstance(sym, tuple):
                    char = sym[0]
                    num = sym[1]
                    fout.write(char * num)
        for sym in symbols:
            print sym
            expand(sym)
            fout.write("\n")
