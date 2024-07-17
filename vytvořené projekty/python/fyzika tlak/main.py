import random

typ_hmotnosti=random.randrange(1,4)
if typ_hmotnosti == 1:
    typ_hmotnosti="g"

elif typ_hmotnosti == 2:
    typ_hmotnosti="dg"

elif typ_hmotnosti == 3:
    typ_hmotnosti="kg"

elif typ_hmotnosti == 4:
    typ_hmotnosti="t"

hmotnost=float(random.randint(0.1,9999))
plocha=float(random.randint(0.1,9999))

typ_plochy=random.randrange(1,4)

if typ_plochy == 1:
    ttyp_plochy="mm"

elif typ_plochy == 2:
    typ_plochy="cm"

elif typ_plochy == 3:
    typ_plochy="dm"

elif typ_plochy == 4:
    typ_plochy="m"

typ_příkladu=random.randrange(1,3)
if typ_příkladu == 1:
    print(f"jaký tlak vyvolá těleso o hmotnosti {hmotnost} {typ_hmotnosti} na plochu {plocha}{typ_plochy}?")
