function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%
% add feature zero

h = theta'*X';
term = h'-y;

% remove 1st column
theta_r = [0; theta(2:end)];
term = term.^2;
term2 = theta_r' * theta_r;

J = 1/(2*m)*(sum(term)+lambda*sum(term2));

% gradient has to have same dimensions as theta
grad = 1/m*(h'-y)'*X  ;
grad = grad';
grad = grad + ((lambda/m )* theta_r);


% =========================================================================



end
