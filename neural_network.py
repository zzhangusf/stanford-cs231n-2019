import numpy as np
from numpy.random import randn

N = 64
D_in = 1000
H = 100
D_out = 10

x = randn(N, D_in)
y = randn(N, D_out)

w1 = randn(D_in, H)
w2 = randn(H, D_out)



for _ in range(2000):

	# sigmoid activation function
	h = 1.0 / (1.0 + np.exp(- x @ w1))

	y_pred = h @ w2

	loss = (y_pred - y) ** 2.0

	grad_y_pred = 2.0 * (y_pred - y)

	grad_w2 = h.T @ grad_y_pred

	grad_h = grad_y_pred @ w2.T

	grad_w1 = x.T @ (grad_h * h * (1-h))

	w1 -= 1.0e-4 * grad_w1
	w2 -= 1.0e-4 * grad_w2


print (np.linalg.norm(y))
print (np.linalg.norm(y - y_pred))

