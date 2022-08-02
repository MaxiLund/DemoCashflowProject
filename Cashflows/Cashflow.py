from generic_app.models import *

class Cashflow(Model):
    
    id = AutoField(primary_key=True)
    amount = FloatField(default=float(0))
    Currency = TextField(default="EUR")
    