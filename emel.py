from sklearn import tree

#jeruk = 0
#apel = 1
#halus = 0
#kasar = 1

ciri = [[120, 1],[150, 1],[200, 0],[250, 0],[200,1]]
label = [0, 0, 1, 1, 0]
mesin = tree.DecisionTreeClassifier()
mesin = mesin.fit(ciri, label)

a = input('Berapa gram beratnya ?')
b = input('Teksturnya Halus atau kasar ?')

data = int(a)
if b.lower() == 'halus':
    tekstur = 0
elif b.lower() == 'kasar':
    tekstur = 1
else:
    print('Unknown')

c = mesin.predict([[data, tekstur]])
if c == 0:
    d = 'Jeruk'
else:
    d = 'Apel'

print('Nama buahnya diprediksi {}'.format(d))