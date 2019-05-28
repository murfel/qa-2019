import json
import csv


def sber_csv_to_squad_json(csv_file='data/taskB/taskB_train.csv'):
    csv_reader = csv.reader(open(csv_file))
    json_object = {'data': []}

    # "paragraph_id", "question_id", "paragraph", "question", "answer"
    next(csv_reader, None) # skip the header
    lines = [[int(line[0]), int(line[1]), line[2], line[3], line[4]] for line in csv_reader]
    lines.sort(key=lambda x: int(x[0]))

    i = 0
    while i < len(lines):
        line = lines[i]
        paragraph_id = lines[i][0]
        article = {'context': line[2], 'qas': []}
        json_object['data'].append({'title': '', 'paragraphs': [article]})
        while i < len(lines) and lines[i][0] == paragraph_id:
            line = lines[i]
            article['qas'].append({'question': line[3], 'id': line[1], 'answers':
                [{'text': line[4], 'answer_start': article['context'].find(line[4])}]})
            i += 1

    with open('sdsj2017_sberquad.json', 'w', encoding='ascii') as json_file:
        json.dump(json_object, json_file)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv_data_file', action='store', help='csv data file')
    args = parser.parse_args()

    csv_file = None

    sber_csv_to_squad_json()
