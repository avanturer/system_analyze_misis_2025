import os
from graph_utils import main

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'test.csv')

    with open(csv_path, 'r') as file:
        csv_content = file.read()

    result = main(csv_content)
    print(result)