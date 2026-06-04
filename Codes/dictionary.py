# Your goal is to implement two functions, save_dict() and load_dict(). 
# The save_dict() function takes two inputs arguments for the dictionary to save and an output file path. 
# The load_dict() function takes an input argument of the file path to the saved dictionary and returns its stored dictionary object.

# The 'pickle' module allows you to serialize (save) and deserialize (load) Python objects to and from files or byte streams.
import pickle

def save_dict(dict, filename):
  with open(filename, 'wb') as f:
    pickle.dump(dict, f)

def load_dict(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

test_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

save_dict(test_dict, 'test_dict.pkl')
loaded_dict = load_dict('test_dict.pkl')
print(loaded_dict)

