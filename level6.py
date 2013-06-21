import re


def lookup():
    num = "90052"

    filenames = []
    try:
        while 1:
            with open("channel/"+num+".txt") as fin:
                filenames.append(num+".txt")
                text = fin.read()
                m = re.search("Next nothing is (?P<num>\d+)", text)
                num = m.group('num')
    except:
        pass
    return filenames
 
def collect_comments(filenames):
    import zipfile
    myzip = zipfile.ZipFile("channel.zip", "r")
    fname_comment_map = {}
    with open("level6_out.dat", "w") as fout:
        for info in myzip.infolist():
            fname_comment_map[info.filename] = info.comment

        for fname in filenames:
            fout.write(fname_comment_map[fname])

filenames = lookup()
collect_comments(filenames)
