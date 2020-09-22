import json
import argparse
import pandas as pd
import ast


def convert(line):
    content = json.loads(line)
    content_copy = content.copy()
    for key, value in content_copy.items():
        if isinstance(value, list):
            content[key] = ','.join(value)
        elif isinstance(value, dict):
            for kk, vv in value.items():
                try:
                    vv = ast.literal_eval(vv)
                    if isinstance(vv, dict):
                        for kkk, vvv in vv.items():
                            content['%s.%s.%s' % (key, kk, kkk)] = vvv
                    else:
                        content['%s.%s' % (key, kk)] = vv
                except Exception as e:
                    content['%s.%s' % (key, kk)] = vv
            del content[key]
    del content_copy
    return content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    args.filename = "..\Data\\business.json"
    csv_filename = '%s.csv' % args.filename[:-len('.json')]
    with open(args.filename, encoding='utf-8') as json_file:
        content = []
        i = 0
        for line in json_file:
            content.append(convert(line))
            print(i)
            i += 1
            print(convert(line))
        df = pd.DataFrame(content)
    df.to_csv(csv_filename, encoding='utf-8', index=False)


if __name__ == '__main__':
    main()
