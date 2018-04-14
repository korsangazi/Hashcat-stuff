import operator

input_hcmask = "input.hcmask"       # input file
output_hcmask = "output.hcmask"     # output file
min_guess = 0                       # min amount of ? (= 0 to parse all masks)

def masktosize(s):
    i = 1
    i = i * 26**(s.count("?l"))
    i = i * 26**(s.count("?u"))
    i = i * 10**(s.count("?d"))
    i = i * 33**(s.count("?s"))
    i = i * 94**(s.count("?a"))
    return i

masks = [i.replace("\n", "") for i in open(input_hcmask, "r").readlines()]

d = {}

for mask in masks:
    d[mask] = masktosize(mask)


sorted_d = sorted(d.items(), key=operator.itemgetter(1))

f = open(output_hcmask, "w")
for mask in sorted_d:
    if mask[0].count("?") > min_guess:
        f.write("{0}\n".format(mask[0]))

f.close()

    

