- L ECTURE 9:
- M ODEL A NALYSIS


# OUTLINE

9.1 Analyzing Model Responses

9.2 Uncertainty Analysis

9.3 Analysis of Model Behavior

9.4 Mathematical Details

# 9.1 A NALYZING M ODEL R ESPONSES

 Validation is model analysis concerned with evaluat model quality relative to the real world using comparisons with empirical data.

 This chapter focuses on analyzing model performance by actively manipulating various components of the model.

 We will discuss two types of manipulations of the model structure.

# 9.2 U NCERTAINTY A NALYSIS

 Sources of Uncertainty in Biological Modeling

 Biological hypotheses and mathematical formulation. We may be ignorant of the correct biological processes involved.

 Parameter values. We may be ignorant of the mean and variance of the population from which our parameter estimates are drawn.

# 9.2 U NCERTAINTY A NALYSIS

 Sources of Uncertainty in Biological Modeling

 There is little we can do about the uncertainty of biological hypotheses and mathematical formulation other than to learn more, design better experiments, and be more clever in our mathematical formulation.

 The effect on our predictions of our uncertainty in parameter values can be investigated using a combination of parameter sensitivity analysis error analysis .

# 9.2 U NCERTAINTY A NALYSIS

#  Parameter Sensitivity Analysis

 Parameter sensitivity analysis involves analyzing differences in model response to small differences in parameter values.

 Author’s interpretation: Parameter sensitivity analysis addresses the question of "What are the dynamical effects of modeler uncertainty about the true mean value of the parameters?”

# 9.2 U NCERTAINTY A NALYSIS

 Uses of Sensitivity Analysis

 There are four major uses of parameter sensitivity analysis.

Validation

Research Design

System Control

Theory

# 9.2 U NCERTAINTY A NALYSIS

 Uses of Sensitivity Analysis Validation

 Two different interpretations of sensitivity result pertain to our general judgments of model quality. First, we have an intuitive belief that most real systems will not respond violently to small changes in the values of the operating parameters or variables.

# 9.2 U NCERTAINTY A NALYSIS

 Uses of Sensitivity Analysis – Research Design

 Model response will be sensitive to some parameters and not to others.

 The sensitive parameters are those to which we should devote the greatest research effort so as to obtain the best estimates, given budget and time constraints.

# 9.2 U NCERTAINTY A NALYSIS

 Uses of Sensitivity Analysis – System Control

 To control a system means that by altering parameters and variables we can produce desirable output.

 If varying a parameter does not alter system output (i.e., the system is insensitive to the parameter), then that parameter is not useful for control.

# 9.2 U NCERTAINTY A NALYSIS

 Uses of Sensitivity Analysis – Theory

 Often the model objective is to investigate a theoretical concept (e.g., conditions for system stability). The response of model output to different parameters may become the central question.

 Interesting theoretical questions are to determine which equations can show a particular model behavior and which parameters are responsible for it.

# 9.2 U NCERTAINTY A NALYSIS

#  Sensitivity Variables

 The state variables at one or more fixed times.

 Time averages of state variables.

 Extreme values (e.g., maximum or minimum) of state variables over a run.

 Times within a run at which significant events (e.g extreme values) occur.

 Simple combinations of state variables are also used, for example, sums, ratios.

# 9.2 U NCERTAINTY A NALYSIS

#  Sensitivity Analysis Methods

 When we perform sensitivity analysis we want to answer two questions: (1) How variable is the response? and (2) What are the ranges of model responses to the parameter changes?

Model Response

(b)

(a)

P1

Sensitivity

or

'low

PvPz

high

Figure 9.1: Model response to two parameters displayed as a surface (a) and contour lines (b) The sensitivity point

# 9.2 U NCERTAINTY A NALYSIS

#  Sensitivity Analysis Methods

 To determine the nature of the surface, sensitivity analysis involves performing numerical experiments in which parameters are systematically changed and resultant model response analyzed.

(a)

(b)

N

low

low

high

high

Pz

Pz

Figure 9.2: Two strategies for parameter sensitivity analyses. (a) Vary single parameters over a large domain and (b) vary multiple parameters over a small range. Contour lines are isoclines of model sensitivity: "N" represents nominal or best parameter values.

# 9.2 U NCERTAINTY A NALYSIS

 Single Parameter Sensitivity

 Sensitivity index S is the ratio of the standardize change in model response (output) to the standardized change in parameter values (input).

$$
(9.1) n n a n n a P P P R R R S ) / ( ) / (   
$$

 The question of which parameters and the degree of alteration to study is dependent on the objectives and the purposes of the sensitivity analysis.

# 9.2 U NCERTAINTY A NALYSIS

#  Single Parameter Sensitivity

 There are two strategies for determining the amount by which parameters are altered. In the uniform approach , all parameters are altered by the same percentage of the nominal values. The variable approach weights the altered interval by the variance of the parameter estimates, if this is known.

Table 9.1: Sensitivity of density-independent growth to r,

|Parm|Nominal input|Nominal output|Altered input|Altered output|5|
|---|---|---|---|---|---|
| |0.1|5.4|0.12|6.6|1.15|
| |0.1| |0.08|4.5|0.88|


# 9.2 U NCERTAINTY A NALYSIS

 Single Parameter Sensitivity

 Normally, we are interested in more than a single parameter, so this table would have additional entries. Also, we are typically interested in more than one response variable.

 A graphical presentation showing actual model response (not sensitivity, Fig. 9.3) can be more informative than Table 9.1.

P

L

1.0

Figure 9.3: Model responses to relative changes in single parameters.   The abscissa is

# 9.2 U NCERTAINTY A NALYSIS

 Multiple Parameter Sensitivity

 For multiple parameter sensitivity, the numerator of Eq. 9.1 does not change, but we must replace the denominator by a distance measure that works in multiple dimensions:

$$
2 ' 2 2 2 ' 1 1 ) ( ) ( p p p p d    
$$

 An alternative that summarizes the responses of multiple variables over time is:

$$
  i j ij S S
$$

where i indexes time and j indexes the variable.

# 9.2 U NCERTAINTY A NALYSIS

 Multiple Parameter Sensitivity

 An alternative approach is based on a fractional factorial. This approach treats parameter sensitivity analysis as if it were an experimental design for a statistical analysis of empirical data (ANOVA).

 The primary sensitivity index is not S statistic that is computed for analyses of variance This is used only as a convenient index, and not as a variable for formal hypothesis testing, as it is i true ANOVA.

# 9.2 U NCERTAINTY A NALYSIS

 Dynamics of Sensitivity

 It is useful to display the altered model behavior over time. One can also graph the dynamics of the sensitivity index rather than the actual model response.

1

+

-

nominal

1

+

-

nominal

Time

Time

and p; are parameters that are increased and decreased (respectively) from the nominal parameters.

# 9.2 U NCERTAINTY A NALYSIS

#  Error Analysis

 Whereas sensitivity analysis is concerned with the effects of model response to small changes in the mean parameter values, the author interpret error analysis to be concerned with changes of model response due to the variance of the parameter values.

# 9.2 U NCERTAINTY A NALYSIS

#  Error Analysis

(b)

(a)

z

z

Z

X

Figure 9.5: Error propagation in simple functions when there is error (o2) around the mean of the independent variable (X). Depending on the function and the mean of the independent variable (X), the error may be amplified (a) or compensated (b)

# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis

 The error around functions can be calculated based on the Taylor series expansion of a function in the neighborhood of a point.

$$
, ) ) ( ( 2! ) ) ( ( ) ( ) ( ) ( ) ( 3 3 3 2 2 2 ⋯              a x x f a x x x f a x x x f a f x f
$$

$$
(9.2) 3 !  x
$$

 Multivariable form of the Taylor series for functions of more than one independent variable

$$
) ( ) , , ( ) ( ) , , ( ) ( ) , , ( ) , , ( ) , , ( c z z y x f b y y z y x f a x x z y x f a b c f z y x f            
$$

$$
z 
$$

# 9.2 U NCERTAINTY A NALYSIS

#  Error Analysis

 The first-order Taylor series is the approach we ta for developing error propagation equations, the use of which we will call analytical error analysis.

$$
) ( ) ( ) , ( y y y f x x x f y x f z z          
$$

The expected value of the function is

$$
) , ( y x f z 
$$

$$
2 2 2 2 2 2 2 ) ( ) )( ( 2 ) ( ) ( ) ( ) , ( ) ( ) ( ) , ( ) ( y y y f y y x x y f x f x x x f y y y f x x x f y x f y y y f x x x f y x f z z                                                                
$$

# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis

 In general, for n variables

$$
(9.3) ) )( ( ) ( ) var( 1 1 2 j j i i j n j n i i x x x x x f x f z z z            
$$

Table 9.2: Variance formulae for simple functions with correlated and uncorrelated ables; vari -

|Function|Uncorrelated|Correlated|
|---|---|---|
| |2 X 0? =02 +02|= 4 +20xy 02 0? +02|
| |= " 02|= 20xy 0? 0?|
|2 = xy|+70}|+ 02|
|z = xly|z 4 (|02 02|


# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis – Analytical Error Analysis

 Analytical error analysis uses the error propagatio of functions, given that the model can be reduced to a single equation that predicts some quantity of interest.

 Uncertainties of the true values of the parameters will propagate to create uncertainties of the predicted probability.

# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis – Analytical Error Analysis

 A simple example model of the probability of extinction due to demographic stochasticity (Pielou, 1977):

$$
(9.4) n b d P       
$$

Applying Eq. 9.3 to Eq. 9.4 to estimate the prediction uncertainty

$$
(9.5) 2 2 2 2 2 1 2 2 1 ln ) var( n n b n n n d n n b d b d b b nd b nd P                                                
$$

# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis – Analytical Error Analysis

 Suppose we have these values for means and standard deviations:

| |d|b|n|
|---|---|---|---|
|mean|0.8|0.9|10|
|std. dev.|0.157|0.174|0.69|


Then, the expected P = 0.308; the variance is var( = 0.72; and the standard deviation is 0.849. The 95% confidence intervals around the mean is

$$
   
$$

$$
1.972 (1.96)(0.849) 0.308 1.356 (1.96)(0.849) 0.308    upper lower CI CI
$$

# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis – Monte Carlo Error Analysis

 Error analysis using Monte Carlo techniques (Chapter 10) can be applied to complex dynamic models and do not require extensive mathematical analysis.

 The method is to simulate repeatedly a system of equations using randomly selected parameter values. The output of each run is collected and statistically analyzed after all runs have been performed.

# 9.2 U NCERTAINTY A NALYSIS

 Error Analysis – Monte Carlo Error Analysis

 Two important practical problems arise when implementing a Monte Carlo analysis of error. First we must decide what probability distribution from which to choose the parameters.

 If the parameter distribution is unknown, another problem is to choose a distribution that is consistent with basic biological knowledge.

9.2 UNCERTAINTY ANALYSIS

#  Error Analysis – Monte Carlo Error Analysis

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 9.2 U NCERTAINTY A NALYSIS

#  Aggregation Analysis

 We wish our models to be as simple as possible. One approach is to maintain a high degree of biological detail but curtail the extent of the system. Another approach to simplification is to lump system variables together.

 This strategy of lumping variables is known as "aggregation," and we want to estimate the errors that aggregation introduces into model output.

 In practice, all models are aggregated at some level of biological organization.

# 9.2 U NCERTAINTY A NALYSIS

#  Aggregation Analysis

 Iwasa et al. (1987) developed an aggregation theory based on a restrictive definition. Perfect aggregation by their definition, is an aggregation that produces identical dynamics at each point of time considered

 Additional progress has been made with a more relaxed attitude toward dynamic similarity. One suc relaxation is that the equilibrium of the sum of th state variables of the detailed model should equal the equilibrium of the aggregated model.

 There are few analytical tools to assess the amount of error that is made by our choice of state variab This leaves us with Monte Carlo simulation of particular cases as the main tool to unravel errors that arise from lumping state variables.

# 9.2 U NCERTAINTY A NALYSIS

 Uncertainty Analysis and Validation

 Sensitivity analysis, error analysis, and aggregation analysis, are all methods that allow us to explore model behavior in different regions of “prediction space”.

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Equilibria

 A system of differential or difference equations is equilibrium if the values of the state variables ar not changing in time. Equilibrium analysis seeks to identify the values of all the equilibria.

 Knowing the equilibria of a model is useful for several reasons:

 First, it characterizes the long-term behavior of th model by providing a set of algebraic equations tha depend on the parameters and state variables.

 Second, knowing the location and number of equilibria for a model can help us interpret the transient dynamics that we observe from simulation.

 Third, the equilibria are the points at which we discuss the stability properties of the model.

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Equilibria – Example of Lotka-Volerra Equations

$$
  bVP aV dt dV
$$

$$
  dP cbVP dt dP
$$

Solving for the equilibria gives

$$
(9.7) 0 * * *   bV P aV
$$

$$
(9.8) 0 * * *  P -dP cbV
$$

  and     for   Solving * P V *

$$
(9.9) / / * *   cb d V b a P
$$

$$
(9.10) 0 0 * *   P V
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Stability: The Concept

 Stability analysis is the analysis of a system of differential equations to determine the dynamics over short times of the system in response to small perturbations.

 Intuitively, a system is stable following a perturbation of one or more of the state variables the system returns to the specific point in state space or to a specific orbit (trajectory) in state

 In general, we are interested in the global response of the system to perturbations. This is difficult f many nonlinear systems, and we usually are able to complete only a local (or neighborhood) analysis.

9.3 ANALYSIS OF MODEL BEHAVIOR

#  A Menagerie of System Responses

9.3 ANALYSIS OF MODEL BEHAVIOR

#  A Menagerie of System Responses

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nullclines and Graphical Stability

 The nullclines of a system of differential equations are the set of points in state space that satisfy t equilibria equations for each of the state variables

 For Lotka-Volterra model (Eqs. 9.7 and 9.8), there are two nullclines for each state variable.

$$
Victim equilibria       (9.11)    bVP aV 0
$$

equilibria   Predator      dP cbVP 0

P

20

alb

dP = 0

d(bc)

Figure 9.9: Lotka-Volterra predator-prey nullclines.  Two equilibria are located at and

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Nullclines and Graphical Stability

 The two-species Gause Competition equations

$$
  1 1 2 1 1 2 1 1 1 1 1 1 1 1 1 1 unrestricted growth intra specific inter specific competition competition 1.0 (9.13) r n n dn n n r n n r n r n dt K K K                        
$$

$$
2 2 2 2 1 2 2 2 2 2 2 2 2 2 1.0 r n dn n n r n n r n r n dt K K                         1 2 (9.14) n K
$$

Four nullclines can be obtained:

$$
1 1 2 1 1 and 0 nullclines                  (9.15) n K n n n     
$$

$$
2 2 1 2 2 and 0 nullclines                 (9.1 n K n n n      6)
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nullclines and Graphical Stability

 The two-species Gause Competition equations

dn1_0

(b)

(a) &

dl

dt

nz

slope

4

dne_0

Anz

dt

nz

B

0

K,

n

Figure 9.10; (a) One of the n1 nullclines from the Gause competition equations. At point = 0 at dt > 0. Le. below the nullcline; population 1 increases; above the nullcline; it decreases. (b) All of the nullclines and equilibria for both species with the vectors of change for each and the resultant vector, The four equilibrla are cicled:.  Note that n1 = 0 ís a nullcline lor n, and nz Is a nullcline for n?. On those nullclines; the other population moves as the arrows indicate (towards their carrying capacity; point dn,

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Nullclines and Graphical Stability

 The two-species Gause Competition equations

# Determination of equilibria :

$$
Factor                                    (9.17) Substitute Eq. 9.15 into Eq. 9.16 1 2 * 2 1 2 * 2 1 2 * 2 * 2 * 1 2 1 1 ) ( ) , ), ( 0) (0 ( (0 0) K K n K K n K K n n n ,K , , ,  K ,                   
$$

$$
into Eq. 9.15       (9.18) Substitute * 2 2 1 * 1 1 n K K n    
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nullclines and Graphical Stability

 The two-species Gause Competition equations

1 1 The rates of change of the population at and at a A B

$$
  1 1 1 1 2 1 1 1 1 2 2 1 1 1 1 1.0 0 1.0 A A A A A A A B dn n n rn dt K n n n dn rn dt K                                                
$$

$$
(9.19)
$$

Rearraging Eq. 9.19 as

$$
1 1 1 1 1 1 2 2 1 1 1 1 1 2 2 1 1 1 1 1 1 1 1 1.0 (9.20) Thus 0 A A A B A A A B A dn n n n rn dt K K dn n n rn rn dt K K dn dn dt dt                                                            
$$

9.3 ANALYSIS OF MODEL BEHAVIOR

#  Nullclines and Graphical Stability

 The two-species Gause Competition equations

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Linear System Stability Analysis

 To address stability in nonlinear models, we must linearize the equations at the equilibria, then use the techniques that apply for linear equations.

 The linear approximation is valid only for small regions around the equilibrium.

 Consider the standard linear model in population ecology, the density-independent growth equation:

$$
rN dN 
$$

$$
(9.22) (9.21) rt t N e N dt 0 
$$

If r > 0, the system will move away from the equilibrium and will be unstable . Otherwise, the system will be stable .

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Linear System Stability Analysis

 An example of a linear, two-state variable model:

$$
(9.24) (9.23) t t c e x c e x x a x a x a x a x x a a a a dt dx dt dx   2 2 1 1 2 22 1 21 2 12 1 11 2 1 22 21 12 11 2 1                                  
$$

 Track 1: Derivative of the Proposed Solution

$$
(9.25) t c e dx   1 1 
$$

$$
dt
$$

$$
(9.26) t c e dt dx   2 2 
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Linear System Stability Analysis

 Track 2: Insert Proposed Solution into Differential Equations

$$
      1 11 1 12 2 11 1 12 2 (9.27) t t t dx a x a x a c e a c e dt e a c a c         
$$

$$
  11 1 12 2 2 21 1 22 2 (9.28) t dx e a c a c dt   
$$

 Combining Tracks 1 and 2

2 12 1 11 1 c a c a c   

- (from Eqs. 9.25 and 9.27)

$$
2 22 1 21 2 c a c a c   
$$

- (from Eqs. 9.26 and 9.28)


# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Linear System Stability Analysis

 Combining Tracks 1 and 2

$$
    0 ) ( 0 ) )( ( 0 det 0 0 21 12 22 11 22 11 2 21 12 22 11 22 21 12 11 2 1 22 21 12 11 2 1                                             a a a a a a a a a a a a a a c c a a a a c c            (9.32) (9.31) (9.30) (9.29) I A I c A Ac c Ac c
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Linear System Stability Analysis

 Interpreting 

$$
1 1 2 2 (9.33) t t x c e x c e    
$$

$$
1 2 1 2 1 1 11 2 12 2 1 21 2 22 (9.34) t t t t x c e c e x c e c e          
$$

  11 21 , 1 The vector c a c c    12 22 1 2 , 2 nd c are the eigenvectors associated with and , resp c c   

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Linear System Stability Analysis

# For real 

 If the largest  i is positive, the time solutions increase; that is, the system dynamics take the perturbation further f equilibrium point and the system is unstable.

 If the largest  i is negative, the perturbation decreases with time and the system is stable.

 If the largest  i is positive and at least one is negative, we have a saddle (or mountain pass): the system is sta a finite number of paths (the mountain ridge), but for all other perturbations.

 If  = 0, the perturbation neither increases or decrease the system has neutral stability.

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

# 

Linear System Stability Analysis For imaginary 

$$
(9.35) t i t t i t         
$$

$$
        ) cos( ) sin( ) sin( ) cos( ) ( ) cos( ) sin( ) sin( ) cos( ) ( ) sin( ) cos( ) ( ) ( 22 21 2 22 21 1 12 11 2 12 11 1 22 2 21 1 12 2 11 1 t c t c e t c t c e t y t c t c e t c t c e t x t i t e e e c e e c t y e e c e e c t x t t t t t i t i t t i t                                      
$$

$$
(9.36)
$$

This tells us that the long-term dynamics of a syst linear differential equations without a forcing fun be a sum of sines and cosines. Cycles can be produce these simple models in two or more dimensions, where they could not be produced in systems with a single variable.

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Linear System Stability Analysis For imaginary 

 If  = 0 and   0, the solution is a sum of a cosine and sine function with constant amplitude. Therefore, a perturbation of the equilibrium will cause undamped oscillations (neutral stability, Fig. 9.8a).

 If  > 0, the amplitudes of oscillations grow exponentially and the solution is unstable (Fig. 9.

 If  < 0, the oscillations are damped and the solution is stable (Fig. 9.8g).

 The frequency of the oscillations are determined by  i .

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations

 We wish to convert a nonlinear equation to a linear equation so that the above neighborhood stability analysis can be performed. Basically, we wish to define a new function of the deviations of the system following perturbation from the equilibrium.

 To show the linearization method for by perturbing the equilibrium point by an amount

$$
) ( ) ( 1 * 1 1 * 1 x X f dt x d X   
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations

$$
order first order zero * * ) ( ) ( x f x X f dt x d X       
$$

It is also true that

$$
* * ) ( dt dx dt dX dt x d X   
$$

So we have the first -order approximation

$$
x f x dt dx   
$$

Therefore, for a system of two ODEs

$$
(9.37) * * * * X X X X y g y x g x dt dy y f y x f x dt dx            
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations Example

$$
  
$$

$$
                           3 3 3 2 3 1 3 2 1 3 3 3 2 3 2 2 2 1 2 1 3 2 1 2 2 3 1 3 2 1 2 1 1 1 3 2 1 1 1 ) , , ( ) , , ( ) , , ( x f x x f x x f x x x x f dt dx x f x x f x x f x x x x f dt dx x f x x f x x f x x x x f dt dx
$$

$$
3 2 1
$$

We can write this set of equations as a matrix

$$
(9.38)  Jx x ɺ
$$

$$
(9.39)                                                3 2 1 3 3 2 3 1 3 3 2 2 2 1 2 3 1 2 1 1 1 x x x x f x f x f x f x f x f x f x f x f
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations Example

: and for deviations from the equilibrium defined by The Gause Eqs. 9.13 and 9.14 have the following Jacobian * 2 * 1 n n

$$
(9.40b) (9.40a) 2 * 1 2 2 * 2 2 2 2 2 2 * 2 2 1 2 1 * 1 1 2 1 1 * 2 1 1 * 1 1 1 1 1 2 2 K r n K r n r n f K r n n f K rn n f K rn K rn r n f                      
$$

|r 1||K 1|r 2||K 2|
|---|---|---|---|---|---|
|0.05|0.2|200|0.05|6.0|1100|


# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations – Example

$$
0.093765171 0.0460379 0 0.000113636 0.04772727 0 ) 0.022772727 ( 0.1363636 0.005 ) 0.025 ( 0.022772727 0.1363636 0.005 0.025 2                           2 1 The roots of the polynomial are       J
$$

Since the largest eigenvalue is positive, we conclude system is not stable. Since  2 is negative, we have a saddle point (Fig. 9.8f), that is, a ridge along whic system will converge to the equilibrium. This ridge sometimes called a separatrix .

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations

 Since the roots are determined completely from the coefficients of the polynomial contained in the elements of the Jacobian matrix. It is possible, therefore, to ascertain the sign of the eigenvalue simply by inspecting the constants of the matrix.

 These relationships have been codified in several stability criteria. Two of the more important of these are the criteria of Routh and Hurwitz.

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Nonlinear Equations

 As an example of the method, consider a general characteristic equation for a system of m state variables:

$$
(9.41) 0 2 2 1 1        m m m m a a a ⋯   
$$

# 9.3 A NALYSIS OF M ODEL B EHAVIOR

#  Displaying Stability Analyses

 Stability diagrams are (usually) two dimensional graphs each axis of which is a parameter (or combination of parameters) that are chosen because they are important in controlling the system's stability properties. In the graph, lines a drawn demarcating regions of this parameter space that have different stability properties (e.g., "sta equilibrium," "limit-cycle", etc). Examples of these can be seen in Figs. 14.7, 18.5, 18.20.

# 9.3 A NALYSIS OF M ODEL B EHAVIOR



Pr é cis on Stability Analysis Steps in Doing a Neighborhood Stability Analysis

- 1. Determine equilibria for particular parameters.
- 2. If nonlinear, compute the Jacobian matrix.
- 3. Create the characteristic equation and compute eigenvalues.
- 4. Inspect the real part of  i : max(Re  i ) < 0 implies stability.
- 5. Or, use the Routh-Hurwitz criteria.


# 9.3 A NALYSIS OF M ODEL B EHAVIOR

 Pr é cis on Stability Analysis

 Stability analysis is an elegant, but limited, tool.

 It is not always possible to find a closed form sol for the equilibria (even if it does exist in the mod Nullcline analysis addresses the same questions, but graphically. It has great heuristic power, but is di to perform for more than three state variables.

 Overall, stability analysis is one of several tools available for understanding model behavior to be used where appropriate.

# 9.4 M ATHEMATICAL D ETAILS

#  Why Equation 9.32 Must Be True

$$
1 11 21 2 2 11 12 21 2 22 1 11 21 2 11 12 21 1 21 1 11 21 2 12 1 11 11 21 2 1 2 1 22 21 12 11 2 2 22 1 21 1 2 12 1 11 0 ) ( b d d b x d d d x d b d d x d d d x d b d d x d x d d d b b x x d d d d b x d x d b x d x d                                          add to Eq. 9.42b to get : (9.42b) (9.42a)
$$

# 9.4 M ATHEMATICAL D ETAILS

 Why Equation 9.32 Must Be True

$$
12 21 11 22 1 21 2 11 2 11 1 21 2 11 11 12 21 11 22 2 d d d d b d b d x d b d b d d d d d d x              
$$

$$
(9.43)
$$

: Substitute Eq. 9.43 into Eq. 9.42b and solve for 1 x

$$
(9.44) 12 21 11 22 12 2 22 1 1 d d d d b d b d x   
$$

The solution of n equations and n unknowns is the ratio of determinants, the denominator of which is t determinant of the original matrix of coefficients. is a very deep result; it is known as Cramer’s Rule

# 9.4 M ATHEMATICAL D ETAILS

 Why Equation 9.32 Must Be True

$$
) det( 0 ) ( d 0 x I c A     (9.45)
$$

Defining the matrix d for the stability problem and re -arranging:

) det( 0 x d 

$$
) det( 0 I x A    (9.46)
$$

. ) det( 0 I x A    interest, equation are 0 (trivial solution), or, in the non- trivial case of in that unknowns,  which yields Eq. 9.46. Either all the with equations The problem was to find the solution to a system of x n n i

# 9.4 M ATHEMATICAL D ETAILS

#  Eigenvectors

 An eigenvector is an n -valued vector, where dimension, or number of state variables. There is one eigenvector associated with each eigenvalue. The elements of the eigenvector c satisfy

$$
or 0 ) (    I c A Ac c  
$$

$$
(9.47)
$$

$$
i i
$$

 The eigenvalue determines how steeply its exponential increases or decreases in The elements of the eigenvector determine the relative distribution of that change over the two state variables.

# 9.4 M ATHEMATICAL D ETAILS

#  Eigenvectors Example

$$
then              3,1) ( 5 2 6 3 i  A
$$

To find the eigenvectors for  2 1 

$$
(9.48)                                  22 21 22 21 22 21 0 6 2 0 6 2 0 0 1 5 2 6 1 3 c c c c c c
$$

$$
  or, choosing    2 22 21 1,1/3 3 1 1 , c c c
$$

Another quick method to calculate the eigenvectors

$$
(9.49) 1 and 1                   12 11 2 12 11 1 a a a a  
$$

