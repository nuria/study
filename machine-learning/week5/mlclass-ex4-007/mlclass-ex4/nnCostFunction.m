function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% ----------------------------------------------

% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m

% m, y,x,lambda, theta1 theta2
% x is 400 vector
% Theta1                25x401                    80200  double
% Theta2                10x26                      2080  double
% num_labels is "k"
% we need to calculate this for theta1 y theta2
% so it works for any number of labels but only for a 2 layer network
% Theta1 and Theta2

% y needs to be remapped from [3 2 1] (if 3 labels) to [0 0 1;0 1 0; 0 0 1]
Y = zeros(m,num_labels);

% remapping now 
for c = 1:m
    yi = y(c);
    
    Y(c,yi) = 1;
end



% layer 1, predict function is doing this no need
%X = [ones(m, 1) X];

% predict(Theta1, Theta2, X)
% needs to return (if 3 labels)  [0 0 1;0 1 0; 0 0 1] for [ 3 2 1] classification

term1 = -Y .* (log( predict(Theta1, Theta2, X)));
term2 = (1-Y).* (log(1-predict(Theta1, Theta2, X)));

J1 = term1 - term2;

% size of J1 is 10 (columns) 5000 rows
% 1st sum every row

J1 = sum(J1');

% we need to sum every 

J = 1/m*sum(J1');

% now the regularization,

Theta1_r = Theta1;
% remove 1st column
Theta1_r(:,1) = [];

Theta2_r = Theta2;
Theta2_r(:,1) = [];

% the ":" makes 1st the sum of colums and after sum of rows
reg1 = sumsq(Theta1_r(:));
reg2 = sumsq(Theta2_r(:));



J = J + (lambda/(2*m))*(reg1+reg2);

% -------------------------------------------------------------

% =========================================================================

% backpropagation 
% forward propagation 1st
% not sure where do we put the random initialization?

% assuming two layers
D2 = 0;
D1 = 0;

for i = 1:m
    a1 = X(i,:)';
    a1 = [1 ; a1];
    z2 = Theta1*a1;
    a2 = sigmoid(z2);
    a2 = [1 ; a2];
    z3 = Theta2*a2;
    a3 = sigmoid(z3);

    d3 = a3 - Y(i,:)';
    d2 = (Theta2_r'* d3).* sigmoidGradient(z2);

    % says this is needed but if we use it grad1 doesn't look right 
    %d2 = d2(2:end);

    % this looks strange but it is assigning elements to the matrix
    D1 = D1+ d2 *a1';
    D2 = D2 +d3* a2';
end



Theta1_grad = (1/m)* D1; % size 25 *401
Theta2_grad = (1/m)* D2; % size 10*26


% Theta1 is 25 *401
% Theta2 26* 10
% 24* 401 size(Theta1_grad)
% 10* 26 size(Theta2_grad)

% remove 1st colum
Theta1_grad_r = Theta1_grad;
Theta1_grad_r(:,1) = [];

%size(Theta1_grad_r) % 25 * 400

Theta2_grad_r = Theta2_grad;
Theta2_grad_r(:,1) = [];

%size(Theta2_grad_r) % 10*25

Theta1_grad_r = Theta1_grad_r + ((lambda / m) * Theta1_r);
Theta2_grad_r = Theta2_grad_r + ((lambda / m) * Theta2_r);

Theta1_grad(:,2:end) = Theta1_grad_r;
Theta2_grad(:,2:end) = Theta2_grad_r;

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];

end
