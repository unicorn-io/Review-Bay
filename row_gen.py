import pandas as pd
import os

data = pd.read_csv('a.csv')

data = data.values.tolist()

def get_list():
    return data

def yes_no(a):
    if (a == '1'): return 'yes'
    else: return 'no'

def generate_table(listo):
    with open('./SIH/table.txt', 'w') as file:
       
        for x in range(len(listo)):
            all_string = '''
            <tr class="row100">
                <td class="column100 column1" data-column="column1">{}</td>
                <td class="column100 column2" data-column="column2">{}</td>
                <td class="column100 column3" data-column="column3">{}</td>
                <td class="column100 column4" data-column="column4">{}</td>
                <td class="column100 column5" data-column="column5">{}</td>
                <td class="column100 column6" data-column="column6">
                    {}
                </td>
            </tr>
            '''.format(listo[x][0], listo[x][1], listo[x][2], yes_no(listo[x][3]), yes_no(listo[x][4]), yes_no(listo[x][5]))
            file.write(all_string)
            file.write('\n')
        

