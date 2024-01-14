#!/usr/local/bin
import torch
from functools import reduce 
import matplotlib.pyplot as plt
import math
import torch.nn.functional as F 

# makemore video: https://www.youtube.com/watch?v=PaCmpygFfXo
# need to look into this a bit before jumping into the transformer arch

f = open('./names.txt')

words = []

for l in f:
    words.append(l.strip())


# bigram dictionary
B = {}

# some try words
for  w in words:
    # use "." to identify start and end
    w = ["."] + list(w) +["."]

    # zip gives you a tuple from both lists
    for (ch1, ch2) in zip(w, w[1:]):
        #print("{0} {1}".format(ch1, ch2))
        k = ch1 + ch2
        B[ch1+ ch2] = B.get(ch1+ch2,0) + 1

l = list(B.items())

l.sort(key=lambda x:x[1])

print("these are the most common tuples: {0}".format(l[-10:]))

# rather than keeping this info in a 2 dimensional array , let's use a matrix
# where rows are going to be the 1st char and columns will be the second char appearances 
# we include start and end chars so we have 28
# you index this N[1,3] = blah

# marks start/end of words
SPECIAL_TOKEN ='.'

vocab = list(reduce(set.union, [set(w) for w in words]))
# for some reason we wnat special token to appaear at the beginning
vocab = [SPECIAL_TOKEN] + vocab
print(vocab)


# 26 letters + special token
vocab_size = len(vocab) 

print("vacab size:{0}".format(vocab_size))

N = torch.zeros([vocab_size,vocab_size], dtype=torch.int32)

print("tensor shape".format(N.shape))
# turn this into a hash

itos = { k:v for (k,v) in enumerate(vocab)}

stoi = {itos[k]:k for k in itos.keys()}

print(itos)
print(stoi)

# now put all this into the tensor so we can build teh table 
# tensor only will have numbers
# zip gives you a tuple from both lists
   
for i in range(vocab_size):
    for j in range(vocab_size):
        c1 = itos[i]
        c2 = itos[j]
        N[i,j] = B.get(c1+c2,0)

#print(N)


# print it pretty
plt.figure(figsize=(16,16))
plt.imshow(N, cmap='Blues')

for i in range(vocab_size):
    for j in range(vocab_size):
        chrs = itos[i] + itos[j]
        plt.text(i, j, chrs, va='bottom', color='gray')
        plt.text(i, j, N[i,j].item(), va='top', color='gray')



plt.axis('off')
#plt.show()

# uncomment below to see figure
#import time
#time.sleep(300)

######### sampling from the distribution we have , transform 1st row on a row of probabilities

# probabilities  for char at index 0 of our tensor
p = N[0].float()
p = p/p.sum()


# let's create a matrix that holds probabilities
# call P 
P = torch.zeros([vocab_size,vocab_size])

for i in range(vocab_size):
    # this adds a fake count of 1 shoudl our count for taht pair be zero
    # so no combination of chars is "impossible"
    p = (N[i]+1).float()
    P[i] = p/p.sum()

# this array of probabilities gives us the probability of a character being the next one
# to sample we are going to use a multinomial distribution given a probability returns an integer
# we need to make it deterministic to repro video

g = torch.Generator().manual_seed(2147483647)
#r  = torch.rand(3, generator=g)
#r = r/r.sum()

# sample 1 item using our probabilities pretending this is a multinomial distribution
# we will get the index (how are we binding this between 0 and 27?)
# ah because the initial probability set has 27 distinct items
idx = torch.multinomial(p, num_samples=1, replacement = True, generator = g)

print(idx.item())
print(N.shape)

# now let's write a loop to sample a set of chars for a name according to this distribution
# we start at index 0 (special char, start token) and from there we sample from the row that expresses 0 + other chars


for i in range(0,10):
    ix = 0
    name = ''
    while True:
        name += itos[ix]
        p = P[ix]
        
        # we can try a uniform distribution (= equal probabilities)
        # to see how things would look without having trained the model
        # this assigns 1/27 for teh 27 chars we have
        # p = torch.ones(27)/27
        
        # next char distribution of probabilitiesi (we are just drawing a single sample)
       
        idx = torch.multinomial(p, num_samples=1, replacement = True, generator = g)
        
        ix = idx.item()
        
        # if we got teh special char just exit 
        if ix == stoi[SPECIAL_TOKEN]:
            break;

    print(name)


# now we want to evaluate the quality of model into a single number
# the equal probability would be 1/27 -> 0.037 -> 4%

# to estimate quality we are going to use likehood, the product of all these probabilities
# likehood estimation (product of all probabilities) (if it was 1/27 => (1/27)^27)
# log likehood => -27log(27) 
# if all probabilities are 1 log_likehood will be zero , if prob are smaller (<<<0), log_likehood => - infinity 
# log(ab) = log(a) + log(b)

log_likehood = 0
n = 0
# see loss of diustribution in a set of words
for w in ['qnuria', 'mateo', 'sofia']:
    chrs = [SPECIAL_TOKEN] + list(w) + [SPECIAL_TOKEN]
    for (ch1, ch2) in zip(chrs, chrs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        # this matrix has the computed probabilities from our training set
        prob = P[ix1, ix2]
        log_prob = torch.log(prob) 
        log_likehood += log_prob
        print(f'{ch1} {ch2}: {prob*100:.4f} {log_prob:.4f}')
        n = n + 1

uniform_log_likehood = -27 * math.log(27)
print(f'{log_likehood} versus uniform log likehood {uniform_log_likehood}')

# we want to invert semantics such closer to zero means less loss

# negative_loglikehood
nll = (-1) * log_likehood
avg_nll = nll/n
print (f'negative log likehood: {nll:.4f}, normalized : {avg_nll:.4f}')

######## now let's move this problem into the NN framework ##############
# it is still a bigram level NN , one layer followed by a softmax function

# upon receiving a char 
# the NN will run it through some weights and it 
# will output the probability distribution of the next char in the sequence
# we will just have one layer
# we will still be using the log likehood to estimate the loss
# since we have the loss function we are going to minimize it using gradient based optimization
# (we are tunning paarmeters via minimizing the loss function)


# step 1 . create training set of all the bigrams 

bigrams = []

xs, ys = [], [] 

for w in words[:1]:
    chrs = [SPECIAL_TOKEN] + list(w) + [SPECIAL_TOKEN]
    for (ch1, ch2) in zip(chrs, chrs[1:]):
        int1 = stoi[ch1]
        int2 = stoi[ch2]
        print(f'{ch1} {ch2}')
        xs.append(int1)
        ys.append(int2)

# we will create tensors out of these lists
xs = torch.tensor(xs)
ys = torch.tensor(ys)

# these are  an integer vector whose items represent chars on our map
"""
if we use word 'emma'
. e
e m
m m
m a
a .
tensor([ 0,  8, 21, 21,  7])
tensor([ 8, 21, 21,  7,  0])
But to be able to use these values on the NN
we are going to use 1 hot encoding
you can transform a tendsor made our of integers into a 2d matrix with 1 hot encoding
not hot: tensor([ 0, 12,  3,  3, 23])
tensor([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
"""

"""
nlls = torch.zeros(5)

step by step of how negative log likehood is calculated

for i in range(5):
    x =  xs[i].item() # input
    y  = ys[i].item() # label (next char in bigram sequence)
    
    # one hot encoded y label coincides with char numbers
    

    xs = tensor([ 0,  8, 21, 21,  7])
    ys tensor([ 8, 21, 21,  7,  0])

    because of 1 hot encoding xs is rows: 5 columns: 27 and  same for ys
    to see prediction of 1st item and compute loss we want to look at prediction for position 8 on row 0 , 21 for next item, position 21 on row 1 etc
    p = prob[i,y]
    logp = torch.log(p)
    nll = -logp
    nlls[i] = nll

print ('averaae negative log likehood, 1 sample, random weights (this num should be very small)', nlls.mean().item())
"""
#plt.imshow(xenc)


print(ys)


# we are going to add our 1st neuron
# which will do a dot product y = wx+b 
# normal distribution of ramdom numbers, so mostly arround zero
# we want the dimensionality of output to match dimensionality of input
# so output needs to have also 27 dimensions
# a (1, 27) will be 1 neuron in deep learning speak +> colum matrix with 27 values
# a (27,27) matrix is what we end up using


# try to use all words now, which means taht there is an explosion on row dimension

xs = []
ys = []

for w in words:
    chrs = [SPECIAL_TOKEN] + list(w) + [SPECIAL_TOKEN]
    for (ch1, ch2) in zip(chrs, chrs[1:]):
        int1 = stoi[ch1]
        int2 = stoi[ch2]
        #print(f'{ch1} {ch2}')
        xs.append(int1)
        ys.append(int2)

# we will create tensors out of these lists
xs = torch.tensor(xs)
ys = torch.tensor(ys)

nums = xs.nelement()
print ("number of samples:", nums)

g = torch.Generator().manual_seed(2147483647)

# teh requires grad is needed for later backpropagate and adjust weights, initial guess is random
W = torch.rand((27,27), generator=g, requires_grad=True)

######## this is called a forward pass ##########

# despite these being one hot encoding we want floats so we can get floats at the end
xenc = F.one_hot(xs, num_classes=27).float()
yenc = F.one_hot(ys, num_classes=27).float()

# we wnat to get a probability distribution, 
# for that we interpret the output of the NN as log (counts) 
# and from that count we get the distribution
# we would expect that with this methodology of random initialization
# we will converge to teh loss we had on our counting approach
# so GRADIENT BASED learning is giving us a result that is equivalent to the
# count and normalize one


# this is gradient descent
# it is going to give us a similar loss to probabilistic setup but it is more flexible
# cause prob setup is hard to expand if insteads of bigrams we are keeping the prior ten chars

for k in range(100):
    
    ######## Forward pass
    # the wya we calculate the logits will be more complex in a more complex neural net 
    # but fundamentally the idea is the same

    xenc = F.one_hot(xs, num_classes=27).float()
    logits = xenc @ W #logcount prediction with initial random guess

    # softmax , goes from counts to prob
    counts = logits.exp()
    prob = counts/counts.sum(1, keepdims= True)


    # now, while we started with a random guess we can 
    # get better guesses by minimizing the loss function 


    # torch.arange(5) is [0,1,2,3,4]

    loss = -prob[torch.arange(nums), ys].log().mean()

    # this loss is a matrix rows 5 columns 27
    print(loss.item())

    # now we want to improve weights
    ####### Backward pass
    W.grad = None # reset gradients to zero

    # this is pretty magical
    # pytorch  has build a computational graph from the forward pass above
    # and now reverses the operations such W.grad now is full 
    loss.backward()

    #print(W.grad)

    # now update the weights , where does this -0.1 come from?
    # it is called the learning rate
    # you can move the -0.1 while looking at loss 
    # W.data  += -0.1 * W.grad
    
    W.data  += -10 * W.grad



# now let's sample from this NN
print('sampling from NN')

for i in range(5):
    out = []
    ix = 0

    while True:
        #BEFORE 
        #p = P[ix]
    
        xenc = F.one_hot(torch.tensor([ix]), num_classes=27).float()
        # just a linear layer we have tuned up weights above
        #  using loss and backpropagation
        logits = xenc @ W 

        # softmax , goes from counts to prob
        counts = logits.exp()
        p = counts/counts.sum(1, keepdims= True)
        
        
        ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
        out.append(itos[ix])
        
        if ix == 0:
            break;
        

    print ("".join(out))




