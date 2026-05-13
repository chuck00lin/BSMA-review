# L ECTURE 10:

# S TOCHASTIC M ODELS

# OUTLINE

10.1 There’s Nothing Like a Random World

10.2 Random Numbers

10.3 Sampling Strategies

10.4 Applications to Differential Equations

10.5 Markov Processes

# 10.1 T HERE ’ S N OTHING L IKE A R W ORLD

 Biological systems (like many other systems) are subject to apparently random fluctuations. That is, either the state variables themselves or the parameters are perturbed at random times and by random amounts.

 Repeatedly simulating random models allows us to estimate characteristics of the probabilistic model response (e.g., the distribution's dispersion and ce tendency). This process is called Monte Carlo simulation .

# 10.1 T HERE ’ S N OTHING L IKE A R W ORLD

 There are three broad areas in which probabilistic models and Monte Carlo simulation are useful in biological simulation:

Statistical Hypotheses

Differential and Difference Equations

Markov Processes

# 10.1 T HERE ’ S N OTHING L IKE A R W ORLD

 When faced with random variation in systems, modelers have two fundamental choices to make. They can either ignore these random changes and model mean behavior, or they can incorporate randomness by constructing stochastic models and couching predictions in terms of probable outcomes.

 In this chapter, we will discuss the following topic

- (1) the mechanics of generating and using computergenerated random numbers in simulation,
- (2) simulating stochastic differential equations, and
- (3) Markov chains.


# 10.2 R ANDOM N UMBERS

 The reason for unpredictability is that a large num unknown physical events are interacting in complex ways.

 The combinations of events and interactions are so that from the human perspective of limited knowledg the outcome is unpredictable.

 At times, we want to select numbers (also called deviates ) from normal, exponential, gamma, or other distributions. Or, we may wish to choose numbers fro empirical distributions.

 For a large class of distributions, if we can genera random numbers from a uniform distribution, then it a rather simple matter to use these numbers to obta deviate from the desired distribution.

# 10.2 R ANDOM N UMBERS

#  Generating Uniform Random Numbers

 For the methods that use recursive equations, the last number produced is used to calculate the next. To emphasize the deterministic origins of the numbers, we call them pseudo-random numbers

 One such operation that lies at the heart of many algorithms is the mod or modulus arithmetic operation. ( y mod x ) produces the integer remainder obtained by dividing y by

 For example,

$$
mod  31417 2 1 n n x x  
$$

If we begin with x 0 = 123, we generate the following sequence of numbers: 123, 15129, 13796, 5430, 15754, 25633, 26968, 891, 8456, 30261, 16822.

# 10.2 R ANDOM N UMBERS

 Generating Uniform Random Numbers

 There are several critical characteristics of good algorithms.

- 1. They should produce long sequences before repeating.
- 2. They should be fast.
- 3. They should reproduce the major components of the desired distribution (mean, variance, skew, distribution at the tails, etc.).
- 4. They should minimize the use of computer memory.


# 10.2 R ANDOM N UMBERS

#  Generating Uniform Random Numbers

 Almost all modern compilers provide a built-in function that returns a random number from a uniform distribution. Although it varies among compiler manufacturers, the linear congruential method is most commonly used. It is the recursive function:

$$
(10.1) mod m c aU U i i ) ( 1   
$$

where a , c , and m are machine-dependent constants chosen to produce a good fit to a uniform distribution. For example, on an IBM mainframe computer, a = 3 14,159,269; c = 453,806,245; and = 2 31 . If c = 0, it is a multiplicative congruential method.

# 10.2 R ANDOM N UMBERS

#  Generating Uniform Random Numbers

 Modern implementations now frequently use m = 2 32 1. For most compilers in which the longest integer is 32 bits, the period is close to 2

 The shuffling method (Press et al. 1992) gives a period of about 2 x 10 18 . In this method, a computed random number r n is not output as the n -th random number, but rather at a randomized later call.

# 10.2 R ANDOM N UMBERS

 Generating Uniform Random Numbers

 Test for random number generators:

- 1. Check for frequency distribution.
- 2. Chi-square test.
- 3. Lattice test (scatter diagram).


0

80

0.40

0.20

0.20

0.40

0.60

0.80

and(n + 2) -

1.00

0.50

0.00

# 10.2 R ANDOM N UMBERS

#  Generating Normal Deviates

 The Box-Muller method involves combining two uniform random numbers ( U 1 , U 2 , obtained from 2 separate calls to the uniform generator) to produce two random numbers from a normal distribution ( z 2 ) having a mean of 0 and a standard deviation of 1.0 [i.e., N (0, 1)]:

$$
) )) sin(2 2ln( ( ) )) cos(2 2ln( ( 2 1 2 2 1 1 U U z U U z      
$$

# 10.2 R ANDOM N UMBERS

#  Inverse Cumulative Methods

 To sample from the distribution, we use table lookup. The random deviate is the mid-point of the bin. Notice that the initial width of the categories determines the resolution of the deviate generated.

(b)

(a)

(c) 1.0

5

25

4

8

1

20

1

3

6

15

2

1

2

0g

0'20 30 40 50 60 70 80 90

Temperaturo Categories (F)

Ternperature Categories (F)

Temperature Categories (F)

Figure 10.1: Frequency distributions of observed temperatures:   (a) raw frequencies; (b) relative frequencies, and (c) cumulative distribution. The arrow indicates the random temperature generated after selecting a random uniform number 0.65.

# 10.2 R ANDOM N UMBERS

 Inverse Cumulative Methods

 An example of the wrapped Cauchy distribution

The probability density function

$$
(10.2)      )] cos( 2 [1 2 1 ) ( 2 2 f       
$$

The cumulative distribution function is the integral of the pdf

$$
(10.4) (10.3)                                     0.5)) (0,1) ( tan( 1 1 2arctan ) ( 2 tan 1 1 arctan 1 ) cos( 2 1 2 1 ) ( 1 2 2 U F C dx F                
$$

# 10.2 R ANDOM N UMBERS

 Inverse Cumulative Methods

 An example of the wrapped Cauchy distribution To summarize, the method to sample a deviate x is:

- 1. Determine the pdf of x [ f ( x )].
- 2. Integrate to get the cdf [ F ( x )].
- 3. Determine the constant of integration at and/or F ( x ) = 0.
- 4. Set F ( x ) to be a value from the uniform distribution [ U (0, 1)].
- 5. Invert F ( x ) and solve for x .


# 10.2 R ANDOM N UMBERS

#  Methods for Other Distributions

 Methods for the Cauchy, log-normal, exponential, gamma, F, and Weibull continuous distributions, and the binomial, Poisson, hypergeometric, and negative binomial discrete distributions can be found in numerical software packages [e.g., the GNU Scientific Library (GSL), International Mathematical and Statistical Library (IMSL), Numerical Algorithm Group (NAG), Mathematica, etc.] or in more advanced texts.

# 10.2 R ANDOM N UMBERS

 Methods for Other Distributions

 MATLAB functions

Syntax

Y = random(name,A) Y = random(name,A,B) Y = random(name,A,B,C) Y = random(...,m,n,...) Y = random(...,[m,n,...])

# Examples

1. Generate a 2-by-4 array of random values from th distribution with mean 0 and standard deviation 1:

x1 = random('Normal',0,1,2,4)

2. Generate a single random value from Poisson dist parameters 1, 2, ..., 6, respectively:

x2 = random('Poisson',1:6,1,6)

# 10.2 R ANDOM N UMBERS

 Methods for Other Distributions

 MATLAB functions

|nane|Distribution|Input Parameter A|Input Parameter B|Input Parameter €|
|---|---|---|---|---|
|or Beca|Beta Distribution| | | |
|'bino or 'Binorial|Binomial Distribution|n: number of trials|p: probability of success for each trial| |
|chi2' or 'Chiaquare|Chi-Square Distribution|degrees of freedom| | |
|or Exponential' 'exp'|Exponential Distribution| | | |
|'ev' or Extrere Value|Extreme Value Distribution|p; location parameter|0; scale parameter| |
| |Distribution|vl: numerator degrees of freedom|v2; denominator degrees of freedom| |
|gar or|Gamma Distribution|parameter shape|b: scale parameter| |
|'gev' Or 'Generalized Excrere Value|Generalized Extreme Value Distribution| |0; scale parameter|p: location parameter|
|or Generalized Parero|Generalized Pareto Distribution|Y: tail index (shape) parameter|0; scale parameter|p; threshold (location) parameter|
|geo' Or 'Georetric'|Geometric Distribution|p: probability parameter| | |
|hyge or Hypergeoretric'|Hypergeometric Distribution| |K: number of items with the desired characteristic in the population|n; number of samples drawn|
|'logn or Lognornal'|Lognormal Distribution| | | |
|'nbin|Negative Binomial Distribution|r: number of successes|P: probability of success in a single trial| |


# 10.2 R ANDOM N UMBERS

 Methods for Other Distributions

 MATLAB functions

|nane|Distribution|Input Parameter A|Input Parameter B|Input Parameter €|
|---|---|---|---|---|
| |Noncentral F Distribution|vl: numerator degrees of freedom|V2: denominator degrees of freedom|5; noncentrality parameter|
|'nct or t'|Noncentral t Distribution|degrees of freedom|6; noncentrality parameter| |
|'ncx2 or|Noncentral Chi-Square Distribution|degrees of freedom|6; noncentrality parameter| |
| |Normal Distribution|P: Mean|O: standard deviation| |
| |Poisson Distribution| | | |
| |Rayleigh Distribution|b: scale parameter| | |
| |Student'; t Distribution|degrees of freedom| | |
|'unif or|Uniform Distribution (Continuous)|lower endpoint (minimum)|b: upper endpoint (maximum)| |
|'unid or|Uniform Distribution (Discrete)|W; maximum observable value| | |
| |Weibull Distribution|scale parameter| | |


# 10.2 R ANDOM N UMBERS

#  Multivariate Distributions

 If variables are correlated, then the distribution i multivariate and we can not draw the deviates independently. The method to use depends on the underlying distribution.

 The sampling distribution of a function is portraye by its variance-covariance matrix. This square matr must be considered when drawing deviates from a multivariate distribution.

# 10.2 R ANDOM N UMBERS

#  Multivariate Distributions

 If the distribution of n variates is normal, then the following algorithm returns a deviate for each of t variables. (1) Select n deviates ( z ) from the standard normal distribution using the Box-Mueller method (or equivalent). (2) Convert the n standard deviates into physical deviates with the relation where m is the vector of variable means and square matrix derived from the variance-covariance matrix ( V ).

 The following relationship holds:

$$
V = SS '
$$

When n > 2, we use software to generate the Cholesky decomposition to obtain S .

# 10.2 R ANDOM N UMBERS

 Multivariate Distributions

 When n = 2, we can easily do it by hand as follows.

$$
) / ( 0 / 0 0 2 1 2 12 2 2 22 12 2 1 12 21 2 1 11 22 21 11 22 21 11 2 2 21 12 2 1 '                                          s s s s s s s s s s SS V
$$

# 10.2 R ANDOM N UMBERS

#  Normal Distribution Function

$$
) - (x exp[ 2 2  1 ) (  x f
$$

$$
] 2   2 2   
$$

$$
) ( Var(x)= x E
$$

# 10.2 R ANDOM N UMBERS

#  Lognormal Density Function

# Lognormal

Possible applications

Time to perform some task   [density   takes on shapes   similar to gamma(a,P) and Weibull(a,P) densities for a > 1, but can have a large "spike" close to x = 0 that is often useful]; quantities that are the product of a number of other quantities (by virtue of large

Density (see Fig. 6.6)

Distribution

Parameters

Range

Mean

Variance

Mode

MLE

$$
exp if x>0 f(x) xV2To 20 otherwise
$$

No closed form

[0,%)

+02/2

e4-

$$
e =1) '(e"? ek-02
$$

$$
1/2 2In X; û = ô
$$

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University                                LECTURE 10-24 Comments 1 Xn that are thought to be lognormal , the data   points, In Xn can be data for   purposes of   hypoth-

# 10.2 R ANDOM N UMBERS

#  Lognormal Density Function

- 2 As 0-0, the lognormal distribution becomes degenerate at e" Thus, lognormal densities for small have sharp peak at the mode
- 3 lim f(x) = 0, regardless of the parameter values 1=0


f(x)

0.8

0.6

0.4

0.2

0.5

1,0

1.5

2.0

2.5

3.5

4.0

4.5

5.0

LN(O,0') density functions.

# 10.2 R ANDOM N UMBERS

#  Uniform Distribution Function

Uniform

Possible applications

Density (see Fig. 6.1)

Distribution

Parameters

Range

Mean

U(a,b)

Used as a "first' model for a quantity that is felt to be randomly varying between a and b but about which little else is known. The U(0,1) distribution is essential in generating random values from all other distributions (see Chaps. 7 and 8)

$$
f(x) = 6 a otherwise 0 if x < a F(x) = if a <x<b b 1 if b < x
$$

and b real numbers with a < b; a is a location parameter , a scale parameter

[a,b]

a +b

Variance

$$
12
$$

# 10.2 R ANDOM N UMBERS

#  Uniform Distribution Function

Mode MLE Comments Does not uniquely exist

$$
â = = max X; 1sis 1si <n
$$

The U(O,1) distribution is a case of the beta distribution special

If X~ U(0,1) and [x,x + Ax] is a subinterval of   [0,1] with Ax 20,

$$
1 + J1 P(Xe[x, x + Ax]) =
$$

f (x)

1/(b -0)

x

U(a,b) density function.

# 10.2 R ANDOM N UMBERS

#  Exponential Distribution Function

|Exponential|expo(ß)|
|---|---|
|Possible applications|at a constant rate; lifetimes of devices with constant hazard rate|
|Density (see|if x 2 0 fx) =|
|Distribution|if x 2 0 otherwise|
| |F() = | 0 -|
|Parameter|Scale parametcr R > 0|
|Range|[0, %)|
|Mean| |
|Variance| |
|Mode| |
|MLE|B X(n)|


# 10.2 R ANDOM N UMBERS

#  Exponential Distribution Function

Thc expo(ß) distribution is a special case of both the gamma and Weibull distributons (for shape parameter = 1 and scale parameter ß in both cases)

Comments

- 2 + X, X gamma( m, ß), also called the m-Erlang distribution
- 3 . memorylcss property (see Appendix 8A)


f(x)

1.2

0.8

0.6

0.2

56*

1

expo( I ) density function

10.2 RANDOM NUMBERS

#  Binomial Frequency Function

## p(x)  Cx p q 

m x m x

E(x) = mp, Var(x) = mpq

10.2 RANDOM NUMBERS

#  Poisson Frequency Function

### 

x

 = mp <6

( ) 

p x

x e

!



  Var(x) =

 

#### E x p x x

( ) ( )



x

0

# 10.2 R ANDOM N UMBERS

#  Geometric Distribution Function

$$
      0              otherwise {0,1,...} if x x p p x p ) (1 ) ( Var(x)= 2 1 1 ) ( p p p p x E   
$$

p (x)

p (x)

0.6

0.25

0.50

0.5-

0.5

0.4

0.4

0.3

0.2-

0.

3

4

geom(p) mass functions.

# 10.2 R ANDOM N UMBERS

|Geometric|geom( p)|
|---|---|
|Possible applications|Number of failures before the first success in a sequence of indepen- of success on number of items inspected before encountering the first defective item; number of items in batch of random size; number of items demanded from an inventory|
|Mass (see Fig. 6.14)|= p) if x € {0,1, otherwise p(x) =|
|Distribution|if x20 otherwise|
|Parameter Range|(0,1)|
|Mean| |
|Variance| |
|Mode MLE|0 X(n) + 1|


is a sequence of independent Bernoulli( p) random variables and X = min {i:Y; = 1} - 1, then X geom( p) Yz *

Comments

- 2 Xs are independent geom(p) random variables; + X, has a negative binomial distribution with parameters and p
- 3 The geometric distribution is the discrete analog of the exponential distribution, in the sense that it is the only discrete distribu-


# 10.2 R ANDOM N UMBERS

#  Gamma Density Function

Gamme

Density (see Fig. 6.3)

Distribution gamma(a,B)

Parameters

Range

Mean

Variance

Mode

$$
if x>0 f(x) = T(a) (o otherwise
$$

for any real number z > 0. Some properties of the gamma function: [(z +1) = z[(z) for any z >0, T(k + 1) = k! for any nonnegative integer for any positive 1)/2*

If a is not an integer, there is no closed form. If a positive integer, then

$$
if x >0 F(x) = j-0 j! (o otherwise
$$

Shape parameter & > 0, scale parameter ß > 0

$$

$$

# 10.2 R ANDOM N UMBERS

#  Gamma Density Function

The following two equations must be satisfied:

MLE

1.2

$$
In X; In Ê + Y(â) = âß = X(n)
$$

which could be solved numerically . and is called the digamma function; F' denotes the derivative of Alteratively, approximations to â and Ê can be obtained by letting T = [In X(n) using Table 6.19 (see 6A) to obtain â as function of T, and letting B = X(n)Iâ. [See Choi and Wette (1969) for the dcrivation of this procedure and of Table 6.191 APP.

0.8

0.6

0.2 -

# 10.2 R ANDOM N UMBERS

#  Weibull Density Function

Wcibull

Possible applications

Density (see 5.4) Fig.

Distribution

Parameters

Range

Mean

Variance

Mode Wcibullla; ß)

Widely used in rcliability  models for lifetimes of devices; time t0 complete some task (density takes on shapcs similar to gamma densities)

$$
if x'> 0 fx) = 'otherwise
$$

$$
~ if x > 0 F(x) otherwise
$$

Shape parameter œ > 0, scale parameter ß > 0

[0,

$$

$$

$$
à (2)-[r()1
$$

$$
Ja [(")
$$

# 10.2 R ANDOM N UMBERS

#  Weibull Density Function

Comments

- 1 The expo(ß) and Weibull(1 , ß) distributions are the same
- 2 X Weibullla, B) if and only if X
- 3 . The (natural) logarithm of a Weibull random variable has distribution. known as the extreme-value or Gumbel distribution [see [17], Mann [26}, and part (b) of Prob. 7.1}
- 4 0 the Weibull distribution becomes degenerate at ß. Thus, Weibull densities for large œ have a sharp peak at the mode
- 5


$$
if œ < | lim fx) 10 6 if a > |
$$

12

1.0

0 = 2

0.8

0.6

=

0.4

0

# 10.2 R ANDOM N UMBERS

#  Beta Density Function

Beta

Possible applications

0,

Used as rough model in the absence of data (sec Scc . 6.9); distribution of random   proportion, such as the proportion of defective items in shipment; time to complete task, €.g-, in PERT network

$$
Density (see Fig. 6.7) f(x) o otherwise
$$

where B(a1,œ2) is the beta function, defined by

Distribution

Parameters

Range

Mean

Variance

$$
=
$$

for any real numbers z1 >0 and z2 > 0. Some properties of the beta function:

$$
B(z1,z2) B(z2,2,) T(z, + 22)
$$

No closed form, in general. If either %, Or œ2 is a positive integer, a binomial   expansion can be used to obtain F(x), which will be polynomial in x, and the powers of x will be, in general, positive real numbers ranging from 0 through € + 02

Shape parameters œ1 > 0 and 02 >0

[0,1]

$$
01 01 + 02
$$

$$
+1) + 02
$$

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 10.2 R ANDOM N UMBERS

#  Beta Density Function

MLE

The following two equations must be satisfied:

$$

$$

where 4 is the digamma function, G, = and G2 X,)] [see Gnanadesikan, Pinkham, and Hughes (1967)]; note that G, + G2 =1These  equations could be solved numerically (see Beckman and Tietjen (1978)], or approximations to â1 and â2 can be obtaincd from Table 6.20 (see 6A), which was computed for particular (G1,G2) pairs by modifications of the methods in Beckman and Tietjen (1978) App.

1.5

"2

"1

5 , 02

7 5

"2*3

0.2

0.4

0.6

0.8

0.6

0.2

0.4

(b)

"1

"2

2 ,

"2

0.8

"0.2, %2

"2 " 0.5

# 10.3 S AMPLING S TRATEGIES

 Random Sampling: This is the simplest strategy. With sufficient number of draws, this method will produce sample of selected values whose distribution resemb that of the original. This method is inefficient in generating deviates from the tails of the distribut

 Stratified Sampling: A strategy to protect against potential small-sample bias by classifying the popu by the relevant groups or categories and then selec randomly from each of these sub-populations.

# 10.3 SAMPLING STRATEGIES

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 10.4 A PPLICATIONS TO D IFFERENTIAL E QUATIONS

 Randomness may be implemented in differential equation models in the initial conditions, driving variables, parameters, or on the state variables dire

 The most common application is to randomize driving variables and parameters.

# 10.4 A PPLICATIONS TO D IFFERENTIAL E QUATIONS

 To incorporate stochastic events in parameter value use a differential equation in which the parameters time t are affected by random deviates from some distribution (e.g., normal). For example, a stochasti density-independent population model might be

$$
(10.5) X r N dt dX t )] , ( [ 2   
$$

# 10.4 A PPLICATIONS TO D IFFERENTIAL E QUATIONS

#  Steps for the Simulation:

- 1. Determine the probability distribution to use for t and estimate the descriptive statistics (mean and v
- 2. Inside the simulation loop, sample the distribution resulting random deviate as the parameter value in differential equation.
- 3. Save the resulting dynamics in an array for post-si statistical analysis.
- 4. Repeat steps 2 and 3 a large number of times to obt Monte Carlo replicates on which to do statistics. T "large" depends on the question being addressed, th underlying variability of the biological process, a of time and money available to answer the question, 10,000 replicates is not uncommon.
- 5. Perform statistical analysis on the resulting rando


# 10.4 A PPLICATIONS TO D IFFERENTIAL E QUATIONS

 Example of a stochastic density-independent population model

(a)

250

200

0 =0.1

Deterministlc

150

1

100

50

(b)

250

200

1

150

100

50

0.3

20

60

40

Time

80

100

20

60

40

Time

80

100

Figure 10.3: Two sets of three random sequences of density-independent population growth using additive normal variation of r. (a) Standard deviation of r = 0.1, (b) standard deviation of r = 0.3.

# 10.4 A PPLICATIONS TO D IFFERENTIAL E QUATIONS

 Some Questions in Analyzing Random System Dynamics

 What is the nature of the state variable values of a single system subject to environmental stochasticit

 What is the nature of the statistical distribution o ensemble of systems , where each is subject to similar environmental stochasticity?

 What are the stability properties of the random dynamics?

# 10.4 A PPLICATIONS TO D IFFERENTIAL E QUATIONS

 An Example of Stochastic Logistic Equation (May 1973):

$$
1 K V rV dt dV        
$$

Eliminating   by dividing both sides by r/K r

$$
  ) / ( V V K dt r K dV  
$$

model of stochastic variation in and an additive Defining a new time variable ) ( K r/K t  

$$
(10.6) ) ) (0, ( 2 V N V K d dV     
$$

10.4 APPLICATIONS TO DIFFERENTIAL EQUATIONS

#  An Example of Stochastic Logistic Equation (May 1973):

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 10.5 M ARKOV P ROCESSES

 A Markov process is a probabilistic model of system dynamics when the system variables possess only a finite number of possible states.

 The rules that describe the changes can be either deterministic or probabilistic; normally, we are interested in the latter form.

 There are two possible ways of viewing the system. we may think of the system as an individual object, which case the system visits the various states sequentially. Second, we may envision the system to an ensemble of individuals that are not explicitly modeled, but each of which is viewed as changing sta randomly.

# 10.5 M ARKOV P ROCESSES

 Both approaches can be described with the same mathematics. The central concept is the transition matrix. A transition matrix is a special case of a probability matrix which is an n x n matrix in which all elements are non-negative, and the elements in the rows sum to 1.0. For example,

$$
(10.7)            3 1 3 1 3 1 2 1 4 1 4 1 0 1 0 P
$$

 Two important facts of these matrices are: (1) If are probability matrices, then PQ is a probability matrix. (2) If P is a probability matrix, then there is a row vector t such that

$$
(10.8) tP t 
$$

# 10.5 M ARKOV P ROCESSES

#  Biological Applications of Markov Processes

 Since P is the probability of moving from the current state to the next state, it is convenient to call th one-step transition probability matrix (Hillier and Lieberman 1980).

 P multiplied by itself ( P (2) ) is the two-step transition probability matrix and represents the probabilities moving from state i to state j in two steps. defined similarly for n steps.

 Let p be a row vector of probabilities that an individual is in state i . In the ensemble interpretation, it is the fraction of individuals in state i. Then, can form a recursive equation to generate the probability distribution in the next time step as

P p p t t   1

(10.9)

# 10.5 M ARKOV P ROCESSES

 Biological Applications of Markov Processes

 If P is composed entirely of elements that are constant and independent of p i and if only on p t , (i.e., not on previous p t-m positive integer), then P is a Markov transition matrix . In this case, Eq. 10.9 describes a Markov process. Sometimes this is referred to as a linear; first-order Markov process.

 As stated above, for a given P , there is a in Eq. 10.9, p t+1 = p t . This is, basically, an equilibrium of the probability distribution of the system, and is called the fixed probability distribution can be computed from

$$
) ( 0 n p P p 
$$

10.5 MARKOV PROCESSES

#  Biological Applications of Markov Processes

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 10.5 M ARKOV P ROCESSES

 Simulating Markov and Transition Matrix Models

 The assumptions of a Markov process are biologicall unrealistic. In particular, the current state of the system will often influence the transition probabil so that P will not be constant.

 One approach to relaxing these assumptions is to us semi-Markov processes applied to compartments (e.g., spatial position) in which the probability of leaving increases the longer an object has been in compartment.

# 10.5 M ARKOV P ROCESSES

 Simulating Markov and Transition Matrix Models

 The simulation process can be simplified if the row of the original transition matrix are converted to cumulative distributions. Then we can use table loo up on an empirical distribution. The rows denote th current state; the columns denote the new states. Given the transformed transition matrix ( algorithm is:

- 1. Assign an initial state to the system (
- 2. Obtain a uniform random deviate (
- 3. For row s i,t , determine the column ( p ij < U t  p i(j+1) where p ij is the upper bound of the cumulative distribution for the transition from state i to state j .


j is the new s j,t+1 .

