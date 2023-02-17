import torch.nn as nn

class BasicGNN(nn.Module):
    '''
        Vanilla Graph Neural Network
    '''
    
    def __init__(self) -> None:
        super().__init__()