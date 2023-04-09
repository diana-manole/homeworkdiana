from pprint import pprint
import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
exams = pd.DataFrame(exam_data, index=labels)
pprint(exams[(exams.score > 12) & (exams.score < 15)])
pprint(exams.attempts.sum())
exams.sort_values(by=['name', 'score'], ascending=[False,True])
exams['name'] = exams['name'].replace('James', 'Matteo')
exams['name']['a'] = 'BooBoo'
pprint(exams) 
""" 6 найдите где количетсво попыток меньше 1 и оценка больше 15 """
pprint(exams[(exams.attempts < 1) & (exams.score < 15)])
"""7 найдите макс и мин оценки"""
pprint(exams.score.max())
pprint(exams.score.min())
"""8 найдите максимельное количество попыток """
pprint(exams.attempts.max())
"""9 удалить колонку попыток """
pprint(exams.drop(['attempts'],axis=1))
"""10 добавить заново колонку attempts везде поставить 1"""
#pprint(exams.insert(1,'attempts',[1,1,1,1,1,1,1,1,1,1 ],True))
"""11 qualify везде поставить yes"""


