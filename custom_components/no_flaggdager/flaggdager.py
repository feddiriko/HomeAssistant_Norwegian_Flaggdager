from datetime import date, timedelta

def beregn_paskedag(year):
    """Returnerer 1. påskedag som datetime.date"""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    måned = (h + l - 7 * m + 114) // 31
    dag = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, måned, dag)

def get_flaggdag(dato: date) -> str | None:
    """Returnerer navnet på flaggdagen hvis det er en, ellers None"""
    faste_dager = {
        (1, 1): "1. nyttårsdag",
        (1, 21): "H.K.H. Prinsesse Ingrid Alexandras fødselsdag",
        (2, 6): "Samefolkets dag",
        (2, 21): "H.M. Kong Harald Vs fødselsdag",
        (5, 1): "Den internasjonale arbeiderdagen",
        (5, 8): "Frigjøringsdagen 1945",
        (5, 17): "Grunnlovsdagen",
        (6, 7): "Unionsoppløsningen 1905",
        (7, 4): "H.M. Dronning Sonjas fødselsdag",
        (7, 20): "H.K.H. Kronprins Haakon Magnus' fødselsdag",
        (7, 29): "Olsokdagen",
        (8, 19): "H.K.H. Kronprinsesse Mette-Marits fødselsdag",
        (12, 25): "1. juledag"
    }

    if (dato.month, dato.day) in faste_dager:
        return faste_dager[(dato.month, dato.day)]

    påske = beregn_paskedag(dato.year)
    pinse = påske + timedelta(days=49)

    if dato == påske:
        return "1. påskedag"
    if dato == pinse:
        return "1. pinsedag"

    return None
