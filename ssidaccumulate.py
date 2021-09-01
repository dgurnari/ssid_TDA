import sys, collections, csv

def accumulate():
    min_strength = 0#this is a minimal strength of the connection to be taken into account.
    fname = "output"

    readings = collections.defaultdict(dict)
    basis = set()
    matrix = []

    with open(fname) as f:
        content = f.readlines()

    for l in content:
        ls = l.split()
        if len(ls) == 3:
            [t,b,v] = ls
            readings[t][b] = v
            min_strength = min(min_strength, int(v))
            basis.add(b)

    basis = sorted(list(basis))

    timestamps = readings.keys()
    timestamps.sort(key=lambda x: float(x))
    i=1

    for t in timestamps:
        row = []
        i = i+1
        for b in basis:
            if b not in readings[t]:
                row.append(min_strength-1) # too silent
            else:
                row.append(readings[t][b])
        matrix.append(row)

    out_file  = open("file_with_points.csv", "w")
    csvw = csv.writer(out_file,lineterminator='\n')
    csvw.writerows(matrix)



if __name__ == '__main__':
    accumulate()
