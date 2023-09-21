from manejo_de_vectores import *


def test():
    v = [None] * 16
    print("{:<60}".format("Ingrese el tipo de carga que prefiera para los "
                          "participantes"))
    n = int(input("\t0 - Automatica\t 1 - Manual: "))
    print("-" * 79)
    participantes_general(v, n)
    input("\tPresione enter para continuar...")
    print("-" * 79)
    continentes(v)
    input("\tPresione enter para continuar...")
    print("-" * 79)
    print("{:<53}".format("Ingrese el tipo de carga que prefiera para el puntaje"))
    p = int(input("\t0 - Automatica\t 1 - Manual: "))
    print("-" * 79)
    vc = vec_instancias(v, p, "Octavos", "cuartos de final")
    input("\tPresione enter para continuar...")
    print("-" * 79)
    vs = vec_instancias(vc, p, "Cuartos", "semifinal")
    input("\tPresione enter para continuar...")
    vf, vt = vec_instancias(vs, p, "Semifinal", "final", 1)
    input("\tPresione enter para continuar...")
    print("-" * 79)
    podio_add(v, vf, vt, p)
    shell_sort(v)
    input("Presione enter para mostrar todos los participantes con los "
          "rankings \nactualizados...")
    print("-" * 79)
    display_all(v)
    input("\tPresione enter para finalizar...")


if __name__ == "__main__":
    test()
