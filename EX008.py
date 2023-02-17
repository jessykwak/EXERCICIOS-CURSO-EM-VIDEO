h = float(input('Qual a sua altura em metros?'))
cm = h*100
mm = h*1000

print('A sua altura em metros é {}m, em cm é {}cm, e em mm é {}mm.'.format(h, cm, mm))
print(f'Em decametros e {h*.1}dam, em hectometros, {h*.01}hm e em kilometros, {h*.001}km.')
