cbt = {}
cbt['urethral play'] = 10
cbt['ball busting'] = 20
print(cbt.values())
for name in cbt.keys():
    print(f'name {name} score {cbt[name]}')

for name, score in cbt.items():
    print(f'name {name} score {score}')

scoreBallBusting = cbt['ball busting']
print(f'score of ball busting is {cbt}')

scoreUrethralPlay = cbt.get('urethral play')
print(f'score of urethral play is {scoreUrethralPlay}')

scoreNone = cbt.get('wrongname')
print(f'score of wrongname is {scoreNone}')
if scoreNone is None:
    print('cant find score oops')
if scoreNone not in cbt:
    print('cant find score oops')
