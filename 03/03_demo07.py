score = {'guanyu':95,'zhangfei':96}
score['zhaoyun'] = 98
print (score)

score.pop('zhangfei')
print ('guanyu' in score)
print (score.get('guanyu'))
print (score.get('yase',99))