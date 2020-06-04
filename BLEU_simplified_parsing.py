# simplified BLEU (machine traslation) metrics
# data type only like D0['grouped']
import re

def ParseMetric(Y, Y_pred, eps=10e-5):
    
    def BagOfWords(line):
        pat = re.compile('[-a-zA-Zа-яА-Я0-9]+')
        words = [i.lower() for i in pat.findall(line)]
        return words
    
    def BLEUmy(list_origin, list_my):
        s1 = set(list_origin)
        s2 = set(list_my)
        return round((len(s1&s2) + eps)/(len(s1|s2) + eps), 3)
    
    # basic info - hard variabt with importance of positioning (may do without positioning)
    base_info_mark = []
    not_so_important_fields = ['all_text', 'salary']
    for key1 in Y['basic_info']:
        if key1 in not_so_important_fields: 
            continue
        val = BLEUmy(BagOfWords(Y['basic_info'][key1]), BagOfWords(Y_pred['basic_info'][key1]))
        #print(key1, '-->', val)
        base_info_mark = base_info_mark + [val]
    base_info_mark = round(sum(base_info_mark)/len(base_info_mark), 3)
    
    # exp info
    def ExpBlockInfoBagOfWords(Y, k1='work_experience', k2='work_places'):
        items = []
        for item in Y[k1][k2]:
            prom = []
            for key2 in item:
                if key2=='all_text': 
                    continue
                prom = prom + BagOfWords(item[key2])
            items = items + prom # or [prom]
        return items
    exp_origin = ExpBlockInfoBagOfWords(Y)
    exp_predict = ExpBlockInfoBagOfWords(Y_pred)
    exp_mark = BLEUmy(exp_origin, exp_predict)

    # edu info
    edu_origin = ExpBlockInfoBagOfWords(Y, k1='education', k2='info')
    edu_predict = ExpBlockInfoBagOfWords(Y_pred, k1='education', k2='info')
    edu_mark = BLEUmy(edu_origin, edu_predict)
    
    return (base_info_mark, exp_mark, edu_mark)
    

    
#import json

#ff0 = open(r'origin.json', 'r')
#origign = json.load(ff0)
#ff0.close()

#ff1 = open(r'bad_var.json', 'r')
#origign_bad = json.load(ff1)
#ff1.close()

#ParseMetric(origign, origign_bad)
        