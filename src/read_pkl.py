import argparse
import pickle
parser = argparse.ArgumentParser()
parser.add_argument('--pkl_file', )
args = parser.parse_args()
if __name__ == '__main__':
    file = open(args.pkl_file, 'rb')
    data = pickle.load(file)
    for k,v in data.items():
        print(k,v)

