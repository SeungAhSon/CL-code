import glob
import pickle
import pandas as pd
from tqdm import tqdm
import random

def load_activations_goemo(vector_path):
    with open(f'{vector_path}/GoEmo_activations_train.pkl', 'rb') as f:
        go_emo_train = pickle.load(f)

    with open(f'{vector_path}/GoEmo_activations_test.pkl', 'rb') as f:
        go_emo_test = pickle.load(f)
        
    return go_emo_train, go_emo_test

def load_activations_yelp(vector_path, dataset, num_activation_files_to_load=4):
    
    vector_files = glob.glob(f'{vector_path}/{dataset}*') + glob.glob(f'{vector_path}/{dataset.title()}*') # we stored activations as Yelp, but it should usually be yelp

    df_yelp = pd.read_pickle('../datasets/pkl/yelp.pkl')

    positive = []
    negative = []
    steering_vectors = []
    idx = 0
    for file in vector_files:
        if idx == num_activation_files_to_load: # only load a certain amount of them due to memory problems
            break
        count = 0
        with open(file, 'rb') as f:
            a = pickle.load(f)
            # print(a)
            random.shuffle(a)
            for entry in tqdm(a):
                # we need this, because our activation vectors still contained duplicates
                try:
                    df_entry = df_yelp.loc[entry[0]]
                except KeyError:
                    continue
                label = df_entry['sentiment']
                target_sentence = entry[1]
                steering_vector = entry[2]
                # activations = value[1]
                # loss = value[2]
                # epoch = value[3]
                # gen_text = value[4]
                # label = value[5]
                if label:
                    positive.append([steering_vector, target_sentence, label])
                    steering_vectors.append([steering_vector, target_sentence, label])
                    # positive.append([steering_vector, activations, loss, epoch, target_sentence])
                else:
                    negative.append([steering_vector, target_sentence, label])
                    steering_vectors.append([steering_vector, target_sentence, label])
                    # negative.append([steering_vector, activations, loss, epoch, target_sentence])
                # if count == 2000: 
                #     print()
                #     break
                count += 1

        idx += 1

    print(f"Number of positive acti vectors: {len(positive)}")
    print(f"Number of negative acti vectors: {len(negative)}")

    return steering_vectors