#!/usr/local/bin
import torch
from functools import reduce 
import matplotlib.pyplot as plt
import math

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
# it is still a bigram level NN
# upon receiving a char 
# the NN will run it through some weights and it 
# will output the probability distribution of the next char in the sequence
# we will still be using the log likehood to estimate the loss
# since we have the loss function we are going to minimize it using gradient based optimization
# (we are tunning paarmeters via minimizing the loss function)


# step 1 . create training set of all the bigrams 

bigrams = []

xs, ys = [], [] 

for w in words:
    chrs = [SPECIAL_TOKEN] + list(w) + [SPECIAL_TOKEN]
    for (ch1, ch2) in zip(chrs, chrs[1:]):
        int1 = stoi[ch1]
        int2 = stoi[ch2]
        xs.append(int1)
        ys.append(int2)

# we will create tensors out of these lists
xs = torch.tensor(xs)
ys = torch.tensor(ys)

