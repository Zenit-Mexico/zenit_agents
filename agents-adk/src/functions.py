def vitales_simulados():
    import random
    glucosa = random.randint(60, 200)  # mg/dL
    ritmo_cardiaco = random.randint(60, 100)  # bpm
    o2 = random.randint(60, 100)  # %
    presion_arterial = f"{random.randint(100, 150)}/{random.randint(60, 90)}"  # mmHg
    return {
        'glucosa': glucosa,
        'ritmo_cardiaco': ritmo_cardiaco,
        'o2': o2,
        'presion_arterial': presion_arterial
    }