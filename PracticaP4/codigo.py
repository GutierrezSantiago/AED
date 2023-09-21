import os.path
import pickle

def buscar(m, dni, FD):
    tsize = os.path.getsize(FD)
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < tsize:
        fp = m.tell()
        vot = pickle.load(m)
        if vot.dni == dni:
            posicion = fp
            break

    m.seek(fp_incial, io.SEEK_SET)
    return posicion
