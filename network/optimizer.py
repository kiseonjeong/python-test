import numpy as np

class SGD:
    """
    (class) SGD
    -----------
    - The SGD optimizer

    Parameter
    ---------
    - lr : learning rate (default = 0.01)\n
    """
    # Object initializer
    def __init__(self, lr=0.01):
        self.lr = lr

    # Update network parameters by SGD
    def update(self, params, grads):
        for key, val in params.items():
            params[key] -= self.lr * grads[key]

class Momentum:
    """
    (class) Momentum
    ----------------
    - The Momentum optimizer

    Parameter
    ---------
    - lr : learning rate (default = 0.01)\n
    - momentum : momentum value (default = 0.9)\n
    """
    # Object initializer
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None

    # Update network parameters by Momentum
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]

class Nesterov:
    """
    (class) Nesterov
    ----------------
    - The Nesterov optimizer

    Parameter
    ---------
    - lr : learning rate (default = 0.01)\n
    - momentum : momentum parameter (default = 0.9)\n
    """
    # Object initializer
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
    
    # Update network parameters by Nesterov
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)
            
        for key in params.keys():
            self.v[key] *= self.momentum
            self.v[key] -= self.lr * grads[key]
            params[key] += self.momentum * self.momentum * self.v[key]
            params[key] -= (1 + self.momentum) * self.lr * grads[key]

class AdaGrad:
    """
    (class) AdaGrad
    ---------------
    - The AdaGrad optimizer

    Parameter
    ---------
    - lr : learning rate (default = 0.01)\n
    """
    # Object initializer
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    # Update network parameters by AdaGrad
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)

class RMSprop:
    """
    (class) RMSprop
    ---------------
    - The RMSprop optimizer

    Parameter
    ---------
    - lr : learning rate (default = 0.01)\n
    - decay_rate : decay parameter (default = 0.99)\n
    """
    # Object initializer
    def __init__(self, lr=0.01, decay_rate = 0.99):
        self.lr = lr
        self.decay_rate = decay_rate
        self.h = None
    
    # Update network parameters by RMSprop
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
            
        for key in params.keys():
            self.h[key] *= self.decay_rate
            self.h[key] += (1 - self.decay_rate) * grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)

class Adam:
    """
    (class) Adam
    ------------
    - The Adam optimizer

    Parameter
    ---------
    - lr : learning rate (default = 0.001)\n
    - beta1 : beta1 parameter (default = 0.9)\n
    - beta2 : beta2 parameter (default = 0.999)\n
    """
    # Object initializer
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None
    
    # Update network parameters by Adam
    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)
        
        self.iter += 1
        lr_t  = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)         
        
        for key in params.keys():
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])            
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
