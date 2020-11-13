def which_encoding(file,num_line=5,zipfile=False):
    import chardet # library pour détecter l'encodage
    import numpy as np
    if zipfile:
        import zipfile
        archive = zipfile.ZipFile(file, 'r')
        list_des_fichiers_dans_zip=archive.namelist()
        encodage=list()
        with archive.open(list_des_fichiers_dans_zip[0], "r") as f:
            for i in range(num_line):
                line_in_file=f.readline()
                if type(line_in_file)==bytes:
                    rawfile=chardet.detect(line_in_file)
                else:
                    rawfile=chardet.detect(line_in_file.encode())   
                encodage.append(rawfile['encoding'])
        if len(set(encodage))==1:
            encodage=encodage[1]
        else:
            encodages_principaux=np.unique(encodage,return_counts=True)
            encodage=encodages_principaux[0][encodages_principaux[1]==max(encodages_principaux[1])]
            encodage=encodage[0]
    else:
        encodage=list()
        with open(file, "r") as f:
            for i in range(num_line):
                line_in_file=f.readline()
                if type(line_in_file)==bytes:
                    rawfile=chardet.detect(line_in_file)
                else:
                    rawfile=chardet.detect(line_in_file.encode())
                encodage.append(rawfile['encoding'])
        if len(set(encodage))==1:
            encodage=encodage[1]
        else:
            encodages_principaux=np.unique(encodage,return_counts=True)
            encodage=encodages_principaux[0][encodages_principaux[1]==max(encodages_principaux[1])]
            encodage=encodage[0]
    return encodage
