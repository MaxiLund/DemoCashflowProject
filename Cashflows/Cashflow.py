from generic_app.models import *

class Cashflow(Model):
    
    amount = FloatField(default=float(0))
    Currency = TextField(default="EUR")
    