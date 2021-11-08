import torch
import torch.nn as nn

class Discriminator(nn.Module):
    def __init__(self, img_dim):
        super().__init__()
        self.disc = nn.Sequential(
            nn.Linear(img_dim, 100),
            nn.LeakyReLU(0.2),
            nn.Linear(100, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.disc(x)

class Generator(nn.Module):
    def __init__(self, z_dim, img_dim):
        super().__init__()
        self.gen = nn.Sequential(
            nn.Linear(z_dim, 100),
            nn.LeakyReLU(0.2), 
            nn.Linear(100, img_dim),
            nn.Tanh(),
        )

    def forward(self, x):
        return self.gen(x)