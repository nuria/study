function P = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Attention returns result like 
% (for 3 labels) [ 0 0 1; 0 1 0; 0 0 1] if result is [3 2 1]

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

P = zeros(size(X, 1), num_labels);
% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

% do we need to add 1?
% Add ones to the X data matrix

% layer 1
X = [ones(m, 1) X];

size(X);
% layer 2
a1 = sigmoid(Theta1*X');
a1 = a1';
k = size(a1);
% layer 3

a1 = [ones(k,1) a1];
size(a1);
h = sigmoid(Theta2*a1');

%return (for 3 labels) [ 0 0 1; 0 1 0; 0 0 1] if result is [3 2 1]

%for c = 1:m
    % max per column and index
%    [_max,i] = max(h(:,c));
%    p(c) = max;

%end
P = h';

% remapping now 
%for c = 1:m
 %   pi = p(c);
    
  %  P(c,pi) = ;
%end


% =========================================================================


end
