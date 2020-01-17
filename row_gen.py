import pandas as pd

data = pd.read_csv('a.csv')

data = data.values.tolist()

with open('./templates/table.html', 'w') as file:
    for x in range(len(data)):
        print(data[0][0])
        all_string = '''
        <tr class="row100">
            <td class="column100 column1" data-column="column1">{}</td>
            <td class="column100 column2" data-column="column2">{}</td>
            <td class="column100 column3" data-column="column3">{}</td>
            <td class="column100 column4" data-column="column4">{}</td>
            <td class="column100 column5" data-column="column5">{}</td>
            <td class="column100 column6" data-column="column6">
                <p>{}</p>
            </td>
        </tr>
        '''.format(data[x][0], data[x][1], data[x][2], data[x][3], data[x][4], data[x][5])
        file.write(all_string)
        file.write('\n')

