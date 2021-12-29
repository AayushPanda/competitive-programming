# Gaussian lens equation: 1/do + 1/di = 1/f
# Lens ratios: di/do = hi/ho, = f/so = si/f
from random import randint
from fractions import Fraction
import pandas

data = pandas.DataFrame(columns='Do,f,Di,Ho,Hi,So,Si,Constant ratio'.split(','))

for x in range(3):
    do = randint(1, 20)
    di = randint(do, 30)
    ho = randint(1, 10)

    f = Fraction(1, Fraction(1, do) + Fraction(1, di))
    hi = Fraction(di, do) * ho
    so = do - f
    si = f/so * f

    data.loc[x] = [str(do), str(f), str(di), str(ho), str(hi), str(so), str(si), str(Fraction(di, do))]

print(data.head())
data.to_csv('scienceLensData.csv')
