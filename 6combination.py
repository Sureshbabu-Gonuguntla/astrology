planets = []
for x in range(6):
    k = input("enter planet name : \n",)
    planets.append(k)
b = set(planets)
m = sorted(b)
if m == ['jupiter', 'mars', 'mercury', 'moon', 'sun', 'venus']: # sun,moon,mars,mercury,jupiter,venus
    print("If the Sun, the Moon, Mars, Mercury,Jupiter and Venus be all in one bhava, the person born "
          "under the yoga will be a holy man called (Tir,thankara) dwelling in forests and hills and having wife,"
          "children and wealth.")
elif m == ['jupiter', 'mars', 'mercury', 'moon', 'saturn', 'sun']:
    print("If the six planets combining and producing the yoga be the Sun,the Moon, Mars, Mercury, Iupiter and Saturn, the effect "
          "on the person born is that he will be a robber, addicced to women not his own, leprous, reviled by relatives,"
          "bereft of children, ignorant and in exile.")
elif m == ['mars', 'mercury', 'moon', 'saturn', 'sun', 'venus']:
    print("The person brrn formed of the Sun, the Moon, Mars, mercury,venus and saturn be insignificant,"
          "engaged in works not his own, afflicted with consumption and dryness of the nose and despicable.")
elif m == ['jupiter', 'mars', 'moon', 'saturn', 'sun', 'venus']:
    print(" If the sun, the Moon, Mars, Jupiter, Venus and Saturn be the six planets jointly producing the yoga, "
          "the person whose birth is influenced by it will be a king's councillor,"
          "bereft of the joys which wife, children and wealth give,but calm and contented.")
elif m == ['jupiter', 'mars', 'mercury', 'moon', 'saturn', 'venus']:
    print("lf the Moon, Mars, Mercury, jupiter, Venus and Saturn be together in a bhava, the person whose birth is "
          "influenced by the conjunction of these planets will be a pilgrim to holy shrines and an ascetic.")
elif m == ['jupiter', 'mars', 'mercury', 'saturn', 'sun', 'venus']:
    print(" If the Sun, Mars, Mercury, Jupiter,Venus and Saturn be in conjun:tion, the person born in the yoga will be of "
          "wandering habits and very wise.")
elif m == ['jupiter', 'mercury', 'moon', 'saturn', 'sun', 'venus']:
    print("If the Sun, the Moon, Mercury,Jupiter, Venus and Saturn combine and produce the effect thereof upon "
          "the person born is that he will suffer from headache, have a constitutional disposition to madness, "
          "dwell in solitudes and that in a foreign country")

else:
    print("wrong input, please check")
print("---------------")
print("source:Jataka Parijatha")
