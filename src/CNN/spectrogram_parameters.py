import torch
from collections import Mapping

# ----------------------- Defaults ----------
class Defaults():

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    # Probability threshold beyond which 
    # a prediction is considered a '1':
    THRESHOLD = 0.5
    VERBOSE = False
    
    # Validate after every epoch:
    EVAL_PERIOD=1
    
    ADVERSARIAL_LOOPS = 1
    TRAIN_STOP_ITERATIONS = 30
    # Determines number of adversarial samples to discover.
    # This is a number (0, 1] that calculates how
    # many adversarial samples to find based on the size of the
    # current dataset. 
    # Note: -1 means find all adversarial samples!
    ADVERSARIAL_SAMPLES = -1
    # How many incorrect slices for a chunk to be considered
    # an adversarial false positive
    ADVERSARIAL_THRESHOLD = 0
    
    DATASET = 'Call'
    #DATASET = 'Activate'
    #DATASET = 'MFCC_Call'
    
    #LOSS = "Focal_Chunk"
    LOSS = "BCELoss"
    CHUNK_WEIGHTING = "count"
    FOCAL_WEIGHT_INIT = 0.5 
    FOCAL_GAMMA = 15
    FOCAL_ALPHA = 0.25
    
    NEG_SAMPLES = 1
    NORM = "norm"
    SCALE = True

    RANDOM_SEED = 8
    DATA_LOADER_SEED = 33
    
    BATCH_SIZE = 32
    NUM_EPOCHS = 50
    
    #Local
    SAVE_PATH = '../models/'
    #SAVE_PATH = '/home/data/elephants/models/'
    
    INPUT_SIZE = 77
    OUTPUT_SIZE = 1
    
    # Criterion for deciding whether to save
    # a model snapshot. Either 'acc' or 'fscore',
    # (acc for 'accuracy'):
    TRAIN_MODEL_SAVE_CRITERIA = 'acc'

# ----------------------- HyperParameters ------------

class HyperParameterClass(Mapping):

    internal_dict = {
    0 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    1 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    2 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    3 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    4 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    5 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    6 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    7 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    8 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    9 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    10 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    
    11 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    12 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    13 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    14 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    15 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    16 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            },
    17 : {
            'lr': 1e-3,
            'lr_decay_step': 4,
            'lr_decay': 0.95,
            'l2_reg': 1e-5,
            'momentum': 0,     # Make 0.9?
            'weight_decay' : 0
            }
    }
    
    name_to_num_map = {
        'resnet18' : 17
        }
    
    def __getitem__(self, key):
        if type(key) == int:
            return self.internal_dict[key]
        # It's a string:
        model_num = self.name_to_num_map[key]
        return self.internal_dict[model_num]
    
    def __len__(self):
        return len(self.internal_dict)
    
    def __iter__(self):
        return __iter__(self.internal_dict)

HyperParameters = HyperParameterClass()