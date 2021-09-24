import os

def open_ann(ann):
    with open(ann) as f:
        entities = []
        for line in f:
            if line[0] == 'T':
                sline = line.split()
                ranges = []
                n = 3
                i = sline[2]
                j = sline[3]
                while ';' in j:
                    j, i2 = sline[n].split(';')
                    ranges.append((int(i), int(j)))
                    i = i2
                    j = sline[n+1]
                    n += 1
                ranges.append((int(i), int(j)))

                # sort ranges
                sorted_ranges = sorted(ranges, key=lambda r: r[0])
                e = (sline[1], sorted_ranges)
                entities.append(e)

        sorted_entities = sorted(entities, key=lambda e: e[1][0][0])
        return sorted_entities

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
etypes = [
                'Abbreviation',
                'Anatomical_Entity',
                'ConditionalTemporal',
                'Degree',
                'Finding',
                'Location',
                'Measure',
                'Negation',
                'Type_of_measure',
                'Uncertainty',
            ]
anntypes = ['B','O','I']

train = open('1.train_find.txt',"a+")
folders = ['/data/sameSampleTrainWithStarting/','/data/sameSampleDev/']
#folders = ['/data/heldOutDev/']
to_write=['Finding']
for folder in folders:
    for filename in os.listdir(ROOT_DIR+folder):
        if filename != ".DS_Store" and filename.split(".")[-1] == 'txt':
            print(filename)
            f = open(ROOT_DIR+folder+filename,'r')
            res = open_ann(ROOT_DIR+folder+filename.split(".")[0]+'.ann')
            #print(res)
            typeList = []
            references = []

            i = 0
            for line in f:
                words = line.split(' ')
                for w in words:
                    hasPoint = False
                    hasComma = False
                    hasSemi = False
                    w = w.replace("\n",'')
                    if w != "":
                        if w[-1] == '.':
                            w = w[0:-1]
                            hasPoint = True
                        elif w[-1] == ',':
                            w = w[0:-1]
                            hasComma = True
                        elif w[-1] == ':':
                            w = w[0:-1]
                            hasSemi = True
                        e = i+len(w)
                        found = False

                        for ent in res:
                            rang = ent[1][0]
                            if i == rang[0] and ent[0] in to_write and found ==False:
                                #print('')
                                train.write(w+"\t"+"B-"+ent[0]+"\n")
                                train.flush()
                                found = True
                                #if hasPoint:
                                #    train.write('.' + "\t" + "O"+ "\n")
                                #    train.flush()
                                #if hasComma:
                                #    train.write(',' + "\t" + "O"+ "\n")
                                #   train.flush()
                                #if hasSemi:
                                #    train.write(':' + "\t" + "O"+ "\n")
                                #    train.flush()
                            elif i > rang[0] and i <= int(rang[1]) and ent[0] in to_write and found ==False:
                                train.write(w + "\t" + "I-" + ent[0]+"\n")
                                train.flush()
                                found = True
                                #if hasPoint:
                                #    train.write('.' + "\t" + "O"+ "\n")
                                #    train.flush()
                                #if hasComma:
                                #    train.write(',' + "\t" + "O"+ "\n")
                                #    train.flush()
                                #if hasSemi:
                                #    train.write(':' + "\t" + "O"+ "\n")
                                #    train.flush()
                        if not found and w != '' and w != ' ' and w != '\n':
                         train.write(w + "\t" + "O"+"\n")
                         train.flush()
                         #if hasPoint:
                         #   train.write('.' + "\t" + "O" + "\n")
                         #   train.flush()
                         #if hasComma:
                         #   train.write(',' + "\t" + "O" + "\n")
                         #   train.flush()
                         #if hasSemi:
                         #   train.write(':' + "\t" + "O" + "\n")
                          #  train.flush()

                        if hasPoint or hasComma or hasSemi:
                            i = e+1+1
                        else:
                            i = e+1

        train.write("\n")
        train.flush()

train.close()

