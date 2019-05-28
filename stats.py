import json
import tqdm
import matplotlib.pyplot as plt

def replace_all(text: str, symbols: str) -> str:
    for s in symbols:
        text = text.replace(s, " ")
    return text


def normalize(text: str) -> str:
    text = replace_all(text.lower(), '.,!?')
    text = text.replace(" - ", " ")
    return text


def average(nums: [int]) -> int:
    return sum(nums) / len(nums)


def main():
    # with open('sdsj2017_sberquad.json') as f:
    with open('train-v1.1.json') as f:
        data = json.loads(f.read())

        # context = data['data'][0]['paragraphs'][0]['context']
        # question_objects = data['data'][0]['paragraphs'][0]['qas']

        # print(len(data['data'][0]))

        # exit(1)

        nums = []

        cnt_questions = 0
        q_lens = []
        cnt_questions_arr = []

        for par in tqdm.tqdm(data['data']):
            kek = par['paragraphs']
            for par in kek:
                # par = par['paragraphs'][0]
                context = par['context']
                question_objects = par['qas']

                cnt_questions += len(question_objects)
                cnt_questions_arr.append(len(question_objects))

                context_set = set(normalize(context).split())
                if '' in context_set:
                    context_set.remove("")

                for question_object in question_objects:
                    q = question_object['question']
                    words = normalize(q).split()
                    num = 0
                    for w in words:
                        if w in context_set:
                            num += 1
                    nums.append(num / len(words))

                    q_lens.append(len(words))

    print(average(nums))
    print(cnt_questions)
    print(average(q_lens))
    print(len(data['data']))
    print(average(cnt_questions_arr))
    print(min(cnt_questions_arr), max(cnt_questions_arr))

    plt.hist(q_lens, range(30))
    plt.show()


if __name__ == '__main__':
    main()
