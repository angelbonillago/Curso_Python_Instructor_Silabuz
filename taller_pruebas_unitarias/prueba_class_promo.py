from datetime import timedelta, datetime
from clases_promo import Promo


now=datetime.now()

#validamos si la fecha ya expiro!
def test_promo_expires():
    tiempo_pasado = now-timedelta(days=700)
    promo = Promo("2015-2",tiempo_pasado)
    assert promo.expired #->F 


