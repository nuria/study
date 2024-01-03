#!/usr/local/bin
# https://pytorch.org
import torch
import torch.nn as nn 
from torch.nn import functional as F

torch.manual_seed(1337)


# building small gpt model, adrej's video: https://www.youtube.com/watch?v=kCc8FmEb1nY
# end result at : https://github.com/karpathy/nanoGPT
# this is all the works of shakespeare
f = open('./tiny.txt')

text = f.read()

print("Text we are reading has {0} characters ".format(len(text)))


print(text[0:1000])
chars = sorted(list(set(text)))

# this below is also call a codebook, we are using chars so our codebook is small 
# and our integer encoding is large
vocab_size = len(chars)

print("vocab size: {0}; {1}".format(vocab_size, "".join(chars)))

# we want to build some strategy to tokenize input text
# tokenizing being changing strings/chars into a numerical encoding
# super simplification below, google uses a much more complicated scheme called 
# that encodes subword strings  https://github.com/google/sentencepiece
# openai uses tiktoken, which also encodes subwords, giving you a shorter sequence for a bit of text 
# as instead of encoding chars  (from 0 to 65, say) it encodes subword from , say, 0 to 50,000
# and thus hello world might be just two tokesn like [567,98]
# in thsi case the vocabulary grows long but the integer encoding is short



# string to integer
stoi = {ch:i for (i,ch) in enumerate(chars)}
itos = {i:ch for (i,ch) in enumerate(chars)}
#print(stoi)
#print(itos)

# encode takes a string and outputs integers
# decode take integers, outputs a string

encode = lambda x: [ stoi[c] for c in x]

# decode takes a list
decode = lambda x: "".join([itos[n] for n in x])


print(encode('you'))
print (decode(encode('you')))

# let's tokenize now teh whole entire training set of tiny shakesperare


tokenized = encode(text)

data = torch.tensor(tokenized, dtype=torch.long)
print(data.shape, data.dtype)
print(data[0:1000])

# let's split data set into training and validation split
n = int(0.9 * len(data))

training_data  = data[0:n]
validation_data = data[n:]


# we now train the model in chuncks of text sampled at random with a maximun length
# this is called block_size or content_length
block_size = 8

# here if sequence is 
# tensor([18, 47, 56, 57, 58,  1, 15, 47, 58])
# we have a few contexts not just once, in the context  of 18 -> 47 comes next but in teh context of 18,47, 56 -> 57 comes next

print(data[0:block_size+1])

# notice our target y is offset from input variable x by 1
x = data[0:block_size+1]
y = data[1:block_size+1]

for t in range(1, block_size):
    x = data[0:t]
    y = data[t]

    print ("for context: {0} predicion is {1}".format(x, y))


# rather than feeding examples and context in serial we do it in parallel
batch_size = 4
# block size is 8 (which means we are predicting ad max for 8 chars which is the one that comes next)

def get_batch(split):
    # generate data for inputs x and targets y
    data = training_data if split =='train' else validation_data
    # returns a vector, like: 504169, 626327, 196701, 663723 
    ix = torch.randint(len(data)-block_size, (batch_size,))
    
    # the points serve as initilization of the paragraph(?) we are going to pass as training
    # since batch size is 4 these are 4 "records" each of context size 8
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x,y

xb, yb = get_batch('train')
print('sample batch, x dimension')
print(xb.shape)
print(xb)
print ('targets, y dimension')
print(yb.shape)
print(yb)

for b in range(batch_size):
    for t in range(block_size):
        context = xb[b, 0:t+1]
        target = yb[b,t]
        #print ("when input is {0} target is {1}".format(context.tolist(), target))




# the simplest transformer architecture we can build here is a bigram language model
# see embedings on pytorch: https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html

class BigramLanguageModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
        # each token reads the logits for the next token from a lookup table
        # this is a matrix with row = size of vocabulary
        # every row represents a word so M[i] => token i in our vacbulary, in this case , say 'letter n'
        # the number of columns is the dimension of our embeding vectore, in this case we are also 
        # making that the vocab_size
        self.token_embeding_table = nn.Embedding(vocab_size, vocab_size)


    def  forward(self,idx, targets=None):
        # idx and targets are both (B,T) tensors of integers, B = batch size (for now 4 , number of rows)
        # and T is the context window (8, also called time)
        # when forward is called with say index 24 that corresponds to char 24
        # the 24th row will be populated?
        # channel (vocab_size, the embeding dimension, 65)
        # this returns log probabilities of odds for all tokens on vocab 
        # (B,T,C)
        logits = self.token_embeding_table(idx) 
        
        # the loss function is just a proabilistic measure that uses entropy , logits 
        # are in [-inf, +inf] range
        # this is a vector of size 65 , ideally if prediction is perfect it will look like [0,0,0,1,0] => 1 hot encoding of word
        # we will have a vector where ideally the loss is small if prediction is good
        # loss agreggates all predictions 

        # we need to reshape logits so we can use cross_entropy as pytorch expects outputs in a different way
        B, T, C = logits.shape
        
        #print("logits shape: {0}". format(logits.shape, logits[0][0]))
                
        #print("logits element (0,0) every element of matrix is a vector size 65: {0}". format(logits[0][0]))


        if targets is None:
            loss = None
        else:
            
            targets = targets.view(B*T)
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)
            # change into 2 dimensions = matrix
                    
        return logits, loss

        """
        idx: current context of some characters in some batch (B, T) matrix 
        generate will extend this (B, T) to be (B, T+1), (B, T+2)... 
        TODO: clarify

        """
    def generate(self, idx, max_new_tokens):
        # idx is a (B,T) array of indexes in the current context
        # i think t is in [1..8] range 
        for _ in range(max_new_tokens):
            # get predictions
            # (we do not use loss) logits was a (B, T, C) tensor => (4, 8, 65)
            # each element is a vector with 65 dimensions
            # this below is calling the forward function
            logits, loss = self(idx)
            # focus only on the last time step
            # last time step for every batch?
            # ya, last time step is the prediction for what comes next
            logits = logits[:, -1, :]  # becomes B, C [4, 65]

            # apply softmax to get probabilities
            probs = F.softmax(logits, dim=1) # B,C
            #print(probs[0,0])
            
            #sample from the distribution and get 1 sample
            # so in each of the batch dimensions we are going to have 1 prediction
            idx_next = torch.multinomial(probs, num_samples=1) # B, 1

            #append sampled index (this is a ventor of probabilities)the running sequence
            # whatever is predicted (idx_next) is concatenated on top of previous idx
            # so if initial matrix idx was (B, T) => this one will be (B, T+1)
            # i think here t is [1..8]
            idx = torch.cat((idx, idx_next), dim=1)

        return idx



m = BigramLanguageModel(vocab_size)
# calling model and passing inputs and targets
# this runs forward function above
(logits, loss) = m(xb, yb)
print(logits.shape)
print ("loss : {0}".format(loss))
# this is how we kick off the generation
# we have a matrix like [0]
# 0 represents a new line in our vocabulary

idx = torch.zeros((1,1), dtype=torch.long)
# because generate works in batches we want to get one batch alone
print(decode(m.generate(idx, max_new_tokens =100)[0].tolist()));





