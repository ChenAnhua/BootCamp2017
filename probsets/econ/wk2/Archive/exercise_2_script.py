'''
This is for problem set 2 in dynamic programming
'''
import numpy as np
import scipy as sp
from scipy.optimize import fminbound
from scipy.stats import lognorm
import matplotlib.pyplot as plt

# we define a modified Bellman operator first
def bellman_operator(w, grid, beta, u, f, s, exo, shocks, Tw=None, compute_policy=0):
    """
    The approximate Bellman operator, which computes and returns the
    updated value function Tw on the grid points.  An array to store
    the new set of values Tw is optionally supplied (to avoid having to
    allocate new arrays at each iteration).  If supplied, any existing data in
    Tw will be overwritten.

    Parameters
    ----------
    w : array_like(float, ndim=1)
        The value of the input function on different grid points
    grid : array_like(float, ndim=1)
        The set of grid points
    beta : scalar
        The discount factor
    u : function
        The utility function
    s:  function
        The poloicy function
    exo:scalar
        equals to 0 if policy function are calculated endogenously and 1 if given exogenously
    f : function
        The production function
    shocks : numpy array
        An array of draws from the shock, for Monte Carlo integration (to
        compute expectations).
    Tw : array_like(float, ndim=1) optional (default=None)
        Array to write output values to
    compute_policy : Boolean, optional (default=False)
        Whether or not to compute policy function

    """
    # === Apply linear interpolation to w === #
    w_func = lambda x: np.interp(x, grid, w)

    # == Initialize Tw if necessary == #
    if Tw is None:
        Tw = np.empty_like(w)

    if compute_policy:
        sigma = np.empty_like(w)

    # == set Tw[i] = max_c { u(c) + beta E w(f(y  - c) z)} == #
    for i, y in enumerate(grid):
        def objective(c):
            return - u(c) - beta * np.mean(w_func(f(y - c) * shocks))
        if exo == 0:
            c_star = fminbound(objective, 1e-10, y)
        else:
            c_star = s(y)
        if compute_policy:
            sigma[i] = c_star
        Tw[i] = - objective(c_star)

    if compute_policy:
        return Tw, sigma
    else:
        return Tw

#define the class
class LogLinearOG:
    """
    Log linear optimal growth model, with log utility, CD production and
    multiplicative lognormal shock, so that

        y = f(k, z) = z k^alpha

    with z ~ LN(mu, s).

    The class holds parameters and true value and policy functions.
    """

    def __init__(self, alpha=0.4, beta=0.96, mu=0, s=0.1):

        self.alpha, self.beta, self.mu, self.s = alpha, beta, mu, s

        # == Some useful constants == #
        self.ab = alpha * beta
        self.c1 = np.log(1 - self.ab) / (1 - beta)
        self.c2 = (mu + alpha * np.log(self.ab)) / (1 - alpha)
        self.c3 = 1 / (1 - beta)
        self.c4 = 1 / (1 - self.ab)

    def u(self, c):
        " Utility "
        return np.log(c)

    def u_prime(self, c):
        return 1 / c

    def f(self, k):
        " Deterministic part of production function.  "
        return k**self.alpha

    def f_prime(self, k):
        return self.alpha * k**(self.alpha - 1)

    def c_star(self, y):
        " True optimal policy.  "
        return (1 - self.alpha * self.beta) * y

    def v_star(self, y):
        " True value function. "
        return self.c1 + self.c2 * (self.c3 - self.c4) + self.c4 * np.log(y)



lg = LogLinearOG()
# == Unpack parameters / functions for convenience == #
alpha, beta, mu, s = lg.alpha, lg.beta, lg.mu, lg.s
v_star = lg.v_star

grid_max = 4         # Largest grid point
grid_size = 200      # Number of grid points
shock_size = 250     # Number of shock draws in Monte Carlo integral

grid = np.linspace(1e-5, grid_max, grid_size)
shocks = np.exp(mu + s * np.random.randn(shock_size))
tol = 1e-9
epsilon_init = 1
def sims(s, exo, v_init, tol, epsilon_init):
    epsilon = epsilon_init
    v = v_init
    while(epsilon >= tol):
        Tv = bellman_operator(v,
                             grid,
                             beta,
                             np.log,
                             lambda k: k**alpha,
                             s,
                             exo,
                             shocks
                             )
        epsilon = ((((Tv)-(v))/(v))**2).sum()
        v = Tv
    return v



#plotting
w = sims(lambda y: 0.95*y,
          0,
          v_star(grid),
          tol,
          epsilon_init
          )
w1 = sims(lambda y: 0.95*y,
          1,
          v_star(grid),
          tol,
          epsilon_init
          )
w2 = sims(lambda y: sp.stats.lognorm.cdf(y, 0.5)*y,
          1,
          v_star(grid),
          tol,
          epsilon_init
          )


fig, ax = plt.subplots(figsize=(9, 5))
ax.set_ylim(-60, -24)
ax.plot(grid, w, lw=2, alpha=0.6, label=r'$Tv^*$')
ax.plot(grid, w1, lw=2, alpha=0.6, label=r'$Tv^*_\sigma1$')
ax.plot(grid, w2, lw=2, alpha=0.6, label=r'$Tv^*_\sigma2$')
ax.plot(grid, v_star(grid), lw=2, alpha=0.6, label='$v^*$')
ax.legend(loc='lower right')
plt.show()