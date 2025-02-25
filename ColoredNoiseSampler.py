import numpy as np
import colorednoise


class ColoredNoiseSampler:
    def __init__(self,
            n_variables: int, # independent variables in each simulation (or dim)
            timesteps  : int, # number of timesteps for each variable
        ):
        self.n_variables = n_variables
        self.timesteps   = timesteps

    def sample(self, n_repeats: int, beta: float):
        samples: np.ndarray = colorednoise.powerlaw_psd_gaussian(
            exponent = beta,
            size     = (n_repeats, self.n_variables, self.timesteps)
        )
        samples = samples.transpose([0, 2, 1]) # (n_repeats, timestep, n_variables)
        import ipdb; ipdb.set_trace()
        return samples
