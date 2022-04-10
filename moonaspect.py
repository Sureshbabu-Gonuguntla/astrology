import pandas as pd
from tabulate import tabulate

result = [("Aries", "will make the person born a King","a man of learning","equal in status to a king","endowed with every amiable quality","a thief","a beggar"),
("Taurus", "one bereft of proporty","a thief","honorable person","a king","wealthy","one of a servaut class"),
("Gemini", "defective in some limb","a king","intelligent and sagacious","a fearless person","a villain","a poor man"),
("Cancer", "valiant","honoriable","endowed with the highestpoetical talent","a person of royal rank","a person working in iron","sufiering from ophthalmia"),
("Leo", "a king","one speaking learnedlY","wealthy","a King","a wicked person","mighty"),
("Virgo", "wealthy","mightY","lordlY","learned","badly behaved","one in comfotable circumstance"),
("Libra","impotent","a king","a mint master","a merchant","impotent","impotent"),
("Scorpio", "minister of a king","father of twins","favourite of a king","one engaged in a base occupation","a sickly person","a poor man"),
("Segitterius", "arbitrator in a court and "
                "one addicted to courtezans","learned, wealthy and wise","wealthy, famous and learned","wealthy and fanrous","addicted to courrezans","an arbitrator in court and addicted to courtezans"),
("Capricorn", "a lord","a king","a king","a learned man","a rich person","a beggar"),
("Aquarius", "a libertine","Rich and famous","Rich and famous","famous","a libertine","a libertine"),
("Pisces", "foul'mouthed and evil'minded","a learned king, fond of mirth","a king","a learned man","foul-mouthel and evil-minded","foul-mouthed and evil minded.")]

df = pd.DataFrame(result, columns=["Moon position", "mars", "mercury", "jupiter", "venus", "saturn", "sun"], index=['aries','taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra','scorpio', 'sagittarius', 'capricorn','aquarius','pisces'])
print(df)

col_names = ["Moon position", "mars","mercury","jupiter","Venus","Saturn","Sun"]
print(tabulate(result, headers=col_names))
print("------------------------------------------------------------------")
x = input("Enter the moon placement sign  :" )
y = input("Enter the planet name which moon aspect by :" )

cellValue = df.loc[x, y]
print("The person becomes :", cellValue)
