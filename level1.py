import string
table = string.maketrans(string.ascii_lowercase,
                 string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print code.translate(table)
print "map".translate(table)
