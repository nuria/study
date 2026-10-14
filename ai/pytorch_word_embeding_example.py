# nn is PyTorch's torch.nn module, the neural-network building blocks. i

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


import torch

# Example from word embedings tutorial in pytorch
# https://docs.pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html

# N-Gram Language Modeling
# we will compute the loss function on some training examples and update the parameters with backpropagation.




CONTEXT_SIZE = 2
EMBEDDING_DIM = 10
# We will use Shakespeare Sonnet 2
test_sentence = """When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery so gazed on now,
Will be a totter'd weed of small worth held:
Then being asked, where all thy beauty lies,
Where all the treasure of thy lusty days;
To say, within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserv'd thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse,'
Proving his beauty by succession thine!
This were to be new made when thou art old,
And see thy blood warm when thou feel'st it cold.""".split()
# we should tokenize the input, but we will ignore that for now
# build a list of tuples.
# Each tuple is ([ word_(i-CONTEXT_SIZE), ..., word_i-1 ], target word)
ngrams = [
    (
        [test_sentence[i - j - 1] for j in range(CONTEXT_SIZE)],
        test_sentence[i]
    )
    for i in range(CONTEXT_SIZE, len(test_sentence))
]

print ("Context size: {0}  and embeding dimension:{1}\n".format(CONTEXT_SIZE, EMBEDDING_DIM))
print(test_sentence)
print("ngrams ([·word_(i-CONTEXT_SIZE),·...,·word_i-1·],·target·word)")

# Print the first 3, just so you can see what they look like.
print(ngrams[:3])

vocab = set(test_sentence)
word_to_ix = {word: i for i, word in enumerate(vocab)}


class NGramLanguageModeler(nn.Module):

    def __init__(self, vocab_size, embedding_dim, context_size):

        # weights: numbers inside the model that training adjusts 
        # They start random, and learning is changing them until the predictions get good. 
        # In PyTorch they're also called parameters, and model.parameters() returns all of them.
        
        super(NGramLanguageModeler, self).__init__()
        print ("instatiating NGram language modeler with vocab size {0}, emnbeding dimension {1}".format(vocab_size,embedding_dim))
        # a lookup table that turns a word index into a trainable vector of 10 numbers (10 is embeding_dim).
        

        # the weights , in the absence of seeds are random
        self.embeddings = nn.Embedding(vocab_size, embedding_dim) # weights created here, one vector of 10 numbers (embedding dimension) per word (97 in vocab)
        
        print("embedings look like this")
        print (self.embeddings)

        # a fully connected layer, y = Wx + b. 
        # linear1 takes the 2 context words × 10 dimensions = 20 inputs to 128 outputs, 
        # and linear2 takes the 128 to 97 one score per vocabulary word (vocab size is 97)
        # there is also relu between layers 
        # relu(x) = max(0, x) to avoid having a multilayer model colapsing to only one layer
        # in this model relu is applied to the  output of the 1st layer: out = F.relu(self.linear1(embeds))
        self.linear1 = nn.Linear(context_size * embedding_dim, 128)  # 128×20 matrix plus 128 bias values , 2,560 + 128 = 2,688
        self.linear2 = nn.Linear(128, vocab_size)   #  a 97 * 128   matrix plus 97 bias values, 12,416 + 97 = 12,513

    def forward(self, inputs):
        embeds = self.embeddings(inputs).view((1, -1))
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)
        log_probs = F.log_softmax(out, dim=1)
        return log_probs


losses = []
loss_function = nn.NLLLoss()
model = NGramLanguageModeler(len(vocab), EMBEDDING_DIM, CONTEXT_SIZE)
optimizer = optim.SGD(model.parameters(), lr=0.001)

# this loops over the whole dataset 10 times
for epoch in range(10):
    total_loss = 0
   
    # remember how this looks: [(['forty', 'When'], 'winters'), (['winters', 'forty'], 'shall'), (['shall', 'winters'], 'besiege')]
    for context, target in ngrams:

        # Step 1. Prepare the inputs to be passed to the model (i.e, turn the words
        # into integer indices and wrap them in tensors)
        # this would translate (['forty',·'When'],·'winters') to something like tensor([45,6])
        context_idxs = torch.tensor([word_to_ix[w] for w in context], dtype=torch.long)
        
        """
        A gradient is the number that says how much, and in which direction, 
        to change a weight to reduce the loss. loss.backward() computes one gradient 
        for every weight and stores it on the weight, in its .grad attribute.

        PyTorch adds each new gradient to the value already stored. It doesn't replace it. 
        That's deliberate, because it lets you sum gradients over several batches before taking one step. 
        In this loop there are no batches  you want each update to reflect only the current example.
        """

        # Step 2. Recall that torch *accumulates* gradients. Before passing in a
        # new instance, you need to zero out the gradients from the old
        # instance
        model.zero_grad()

        # Step 3. Run the forward pass, getting log probabilities over next words
        # the forward pass. It embeds the two words, 
        # runs them through the two linear layers, these were the layers dimensions: (10* 2 => 128, 128=>65)
        # and returns a log-probability for every word in the vocabulary (that is why last dimension vector is vocab size).
        log_probs = model(context_idxs)

        # Step 4. Compute your loss function. (Again, Torch wants the target
        # word wrapped in a tensor)
        # NLLLoss takes the log-probabilityi (log softmax) the model gave the correct next word. 
        # A low probability on the right word gives a high loss
        loss = loss_function(log_probs, torch.tensor([word_to_ix[target]], dtype=torch.long))

        # Step 5. Do the backward pass and update the gradient
        # this is the part where we need to drive changes to the model itself
        # so turn the loss into an actual change in the model
        
        # - backward() works backwards through the calculation (log_softmax, linear2, relu, linear1, then the embeddings). 
        # It uses the chain rule from calculus to work out, for every weight, how the loss would change if that weight went up a little.
        # now relu and softmax do not have weights (they are a fixed formula) so it applies only to linear1 and linear2 
        # a positive gradient means increasing weight increases lost, negative gradient, increasing it reduces lost
        
        # notice that backpropagation is going all the way 
        # back to the embedings themselves
        # - nn.Embedding creates a weight table of 97 rows × 10 columns. 
        # It's a normal learnable parameter, so it's included in model.parameters()
        # loss.backward() continues through it and fills model.embeddings.weight.grad.
        loss.backward()
        
        #  The optimizer here is SGD with learning rate 0.001. For every weight it does:
        # weight = weight - 0.001 * weight.grad, It moves each weight a small step in the direction that lowers the loss. 
        optimizer.step()

        # Get the Python number from a 1-element Tensor by calling tensor.item()
        total_loss += loss.item()

        # in one training step, only the rows for the words in the context get a non-zero gradient. 
        # For ['forty', 'When'], only the forty and When rows move. The other 95 rows receive zero gradient and stay unchanged for that step.
        if 'beauty' in context:
            print ("embedding of one particular word")
            # To get the embedding of a particular word, e.g. "beauty"
            print(model.embeddings.weight[word_to_ix["beauty"]])

    losses.append(total_loss)

print("loss over the 10 backpropagation steps, it should decrease")
print(losses)  # The loss decreased every iteration over the training data!

print ("embedding of one particular word")
# To get the embedding of a particular word, e.g. "beauty"
print(model.embeddings.weight[word_to_ix["beauty"]])




