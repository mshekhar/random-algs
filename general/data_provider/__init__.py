import csv
import json
import os
import sys

csv.field_size_limit(sys.maxsize)


def get_test_case(file_name):
    # fieldnames = ['input', 'result']
    with open(os.path.join('data_provider', file_name), 'rU') as test_data_file:
        test_data_rows = csv.DictReader(test_data_file, dialect="excel-tab")
        feed_columns = test_data_rows.fieldnames
        print 'generating rows', feed_columns
        for row_num, row in enumerate(test_data_rows):
            print row_num
            d = {}
            for col in feed_columns:
                d[col] = json.loads(row[col])
            yield d
