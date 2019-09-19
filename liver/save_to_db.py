from .models import male_lethal,male_compl,female_lethal,female_compl


def str_to_bool(stri):
    if stri == 'жив' or stri == 'да':
        return True
    else:
        return False


def std():
    # female complications
    with open(r'C:\Users\User\Desktop\DJ_Nurotic\Rex2\liver\Female_compl.txt', 'r') as f:
        t = [line for line in f]
    for line in t:
        line = line.strip().split('\t')
        obj = female_compl()
        # bool fields
        obj.result = not(str_to_bool(line[0]))
        obj.ibs = str_to_bool(line[7])
        obj.csn = str_to_bool(line[8])
        obj.chr_pan = str_to_bool(line[9])
        # int fields
        obj.css = int(line[2])
        obj.fv = int(line[6])
        obj.dad = int(line[10])
        obj.comp_mor = int(line[12])
    # float fields
        obj.actv = float(line[1])
        obj.lp = float(line[3])
        obj.mgp = float(line[4])
        obj.zs = float(line[5])
        obj.emot_coeff = float(line[11])
        obj.score = float(line[13])
    # commit
        obj.save()

# female lethality
    with open(r'C:\Users\User\Desktop\DJ_Nurotic\Rex2\liver\Female_lethal.txt', 'r') as f:
        t = [line for line in f]
    for line in t:
        line = line.strip().split('\t')
        obj = female_lethal()
    # bool fields
        obj.result = str_to_bool(line[0])
        obj.mfa = str_to_bool(line[5])
        obj.takrolimus = str_to_bool(line[6])
        obj.methylprednise = str_to_bool(line[7])
        # int fields
        obj.css = int(line[4])
        obj.dad = int(line[8])
        # float fields
        obj.glucose = float(line[1])
        obj.erythrocyte = float(line[2])
        obj.actv = float(line[3])
        obj.kokraf = float(line[9])
        obj.mdrd = float(line[10])
        obj.score = float(line[11])
    # commit
        obj.save()

# male complications
    with open(r'C:\Users\User\Desktop\DJ_Nurotic\Rex2\liver\Male_compl.txt', 'r') as f:
        t = [line for line in f]
    for line in t:
        line = line.strip().split('\t')
        obj = male_compl()
        # bool fields
        obj.result = not(str_to_bool(line[0]))
        obj.sd = str_to_bool(line[2])
        obj.chr_pan = str_to_bool(line[3])
        # int fields
        obj.psycho = int(line[4])
        obj.activity = int(line[5])
        obj.pg = int(line[6])
        obj.dad = int(line[7])
        # float field
        obj.lpvp = float(line[1])
        # commit
        obj.save()

    # male lethality
    with open(r'C:\Users\User\Desktop\DJ_Nurotic\Rex2\liver\Male_lethal.txt', 'r') as f:
        t = [line for line in f]
    for line in t:
        line = line.strip().split('\t')
        obj = male_lethal()
        # bool fields
        obj.result = str_to_bool(line[0])
        obj.vrvp = str_to_bool(line[4])
        obj.bkk = str_to_bool(line[5])
        obj.mfa = str_to_bool(line[6])
        # float fields
        obj.prot_time = float(line[1])
        obj.mgp = float(line[2])
        obj.meld = float(line[3])
        obj.sad = float(line[7])
        obj.dad = float(line[8])
        obj.score = float(line[9])
    # commit
        obj.save()
