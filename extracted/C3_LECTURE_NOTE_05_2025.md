# L ECTURE 5:

# Q UANTITATIVE M ODEL F ORMULATION : II

# OUTLINE

5.1 Physical Processes

5.2 Using the Toolbox of Biological Processes

5.3 Useful Functions

5.4 Examples

# 5.1 P HYSICAL P ROCESSES

#  Conservation of Mass and Energy

 Biological systems are physical systems that exist three dimensional space and are subject to fundamental physical laws and process.

 The central idea of mass and energy conservation is that material or energy that flows from one place to another is lost from the first and an equa amount is gained by the second place.

# 5.1 P HYSICAL P ROCESSES

#  Ecosystem Example

A

1

9

abTr

Figure 5.1: Carbon flow in a simple terrestrial ecosystem. D=deer; L-lumped excretion

# 5.1 P HYSICAL P ROCESSES

#  Ecosystem Example

$$
(5.1) d D e rD D abG aT G dt dD T            ) ( 1
$$

$$
(5.2) D abG aT G uG dt dG T          1
$$

$$
(5.3) cL d D e dt dL    ) (
$$

$$
(5.4) cL rD uG dt dA    
$$

Table 5.1: Parameter definitions for a carbon flow model.

Deër successful search rate for grass

- b Deer handling time while eating grass
- c Rate of decomposition of fcces and dead deer by bacteria
- d Rate of feces production by deer


Fraction of deer carbon becoming rotting corpses

r Rate of deer production of gaseous carbon (respiration)

Tr Total time for foraging

4 Rate of atmosphcric_Carbon uptake by grass

# 5.1 P HYSICAL P ROCESSES

#  Spatial Flows

 When the spatial resolution is such that only a few large regions are modeled (such as broad areas in a lake), then the problem can be treated just as we treated the carbon flow problem. We write differential for each spatial area with appropriate flows between the various spatial regions.

 In situations where we can not reasonably assume homogeneous regions (i.e., where there is a continuo gradation of the spatial structure), we must use a different conceptual framework. In these cases, the framework we use is based on partial differential equations (PDEs) .

# 5.1 P HYSICAL P ROCESSES

 Spatial Flows

 Four fundamental processes affecting fluids and solutes recur in models which have two independent variables (time and space) over which the state variable (C) varies:

- 1. Advection
- 2. Molecular diffusion
- 3. Turbulent diffusion
- 4. Reaction.


# 5.1 P HYSICAL P ROCESSES

#  Spatial Flows

miolecular

roacton

diffusion

input

X+Ax

2

Fout

reaction

output

Figure 5.2: Flows and processes in one-dimensional fluid flow. Advection flow is from left to right. Solid dots represent particles of the substance of Interest:.  The vertical dotted lines represent arbitrary imaginary boundaries located at x and r + Ax

# 5.1 P HYSICAL P ROCESSES

#  Spatial Flows

 Discrete formulation of ordinary differential equat

$$
  (5.5) ) ( t t NetChange y y t t t    
$$

 Finite difference equation based on discretized spac

$$
    dx dC x C C x x NetChange C C x x NetChange C C x x x x x x x in out               0 ) ( ) ( lim (5.6)
$$

 When we add time and require conservation of mass, we must insure that the temporal changes in C equal the spatial changes in C.

$$
(5.7) x F t C      
$$

# 5.1 P HYSICAL P ROCESSES

 Spatial Flows

 The rate of change of the concentration in a segmen must equal the inflow minus the outflow.

$$
x x F F F F x x x out       
$$

 The statement of the principle of conservation of m

$$
x x x F F A F M out in F x F x                          
$$

# 5.1 P HYSICAL P ROCESSES

#  Spatial Flows

 Advection : Advection is the flow of media and the solute from point to point. If the velocity is a co over a small spatial interval, then the flux of C is

$$
UC F 
$$

by conservation of mass

$$
(5.8) x UC x F t C           ) (
$$

# 5.1 P HYSICAL P ROCESSES

#  Spatial Flows

 Diffusion: Molecular diffusion is the movement of mass due to random motion of individual molecules. D is constant called diffusivity and is assumed here to be constant over x.

$$
C D F  
$$

$$
2 2 x C D x x C D x F t C x                 (5.9)
$$

 Putting advection and diffusion together to find changes in C, we have the conservation equation

$$
(5.10) x UC x C D t C         ) ( 2 2
$$

# 5.1 P HYSICAL P ROCESSES

#  Spatial Flows

 Reactions: Reaction processes are any processes other than advection and diffusion that change the concentration of a solute inside the spatial interv These may be chemical interactions, or biological uptake and excretion.

 An example of reaction-diffusion equation

$$
(5.11) excretion uptake m advection diffusion eS N K NP x UN x N D t N            max 2 2 ) ( 
$$

# 5.1 P HYSICAL P ROCESSES

 Turing system

 Alan Turing, 1952

 A diffusion reaction system

 Two or more chemical species

 Different rate of diffusion for the participants

 Chemical interactions

$$
) , ( 2 u v f u D u u    
$$

$$
) , ( 2 g u v v D t v t v      
$$

# 5.1 P HYSICAL P ROCESSES

#  Turing system

$$
) ) , ( 2 u v f u D t u u      
$$

$$
, ( 2 g u v v D t v v    
$$

degradation

autocatalysis

activator u

diffuse

inhibit

activate

degradation

inhibitor v

diffuse

Activator-inhibitor system

# 5.1 P HYSICAL P ROCESSES

 Turing system

 Gray-Scott Model

# Chemical Reaction

$$
2 3 U V V  
$$

$$
V P 
$$

Flower-Dattern: F-0.055

Mazes-pattern:F-0.029

# Model Equations

$$
2 2 (1 ) u u D u uv F u t       
$$

$$
2 2 ( ) v v D v uv F k v t       
$$

Solitons-oattern: F-0.03

# Reference and Simulation Link:

https://itp.uni-frankfurt.de/~gros/StudentProjects/Projects_2020/projekt_schulz_kaefer/

# 5.1 PHYSICAL PROCESSES

##  Pattern formation modeling of zebrafish

Asai et al., 1999

# 5.1 PHYSICAL PROCESSES

 Simulation of butterfly wing pattern elements

# 5.1 P HYSICAL P ROCESSES

 Simulation of butterfly wing pattern elements

Tlmc-0

Tlmc-0

05

05

# 5.1 P HYSICAL P ROCESSES

 Simulation of eyespots in wing veins

# 5.1 P HYSICAL P ROCESSES

#  Discontinuous Functions

 For reasons of simplicity and convenience if nothin else, we often choose to represent the phenomena as discontinuous. A hypothetical example is

$$
            x . bx             if . . x . if . . x x                   if R 10 10 10 05 10 05 0 2
$$

 An example of describing the opening of the stomata on the leaf surface.

0)

$$
      otherwise . b P b P         if b P b P a e e g g e e g g 0 0
$$

# 5.1 P HYSICAL P ROCESSES

#  Time and Driving Variables

 Driving variables described by a time-dependent equ

$$
            211) ( 365 2 25cos 40 )) ( cos( 0 t T t t A M y   (5.12)
$$

 Incorporating time in functions used in computer simulations using look-up table .

(a)

(b)

cos(x)

60

1.0

1

0.5

40

0.5

20

Mean Daily Temperalure

41,0

~I2

312

512

100

200

300

Day

Figure 5.3; (a) An untranslated cosine function. (b) General cosine function with parameters fitting a hypothetical time series of seasonal temperature values.

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

 Basic Tools in our Toolbox for Reading and Constructing:

- 1. Constant rates
- 2. Relative rates
- 3. Feedback
- 4. Mass action
- 5. Conservation of mass
- 6. Limitation by multiple controls
- 7. Discontinuous functions
- 8. Time dependence


 An approach to successfully reading and constructin quantitative models is to combine these basic formu in ways that represent the biological hypotheses.

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Checking Units

 The physical units of the derivative must match the units of the equation on the right-hand side.

 This will check for two types of errors:

- 1. Inappropriate expressions (e.g., dividing when you subtract).
- 2. Bad logic that requires parameter values with incor


 Example: logistic equation (Eq. 4.14)

$$
2 1 (4.14) 1 dN N r r N rN N dt K K numbers numbers numbers unitless numbers                      
$$

$$
time time numbers time  
$$

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conversion to Dimensionless Format

 A useful procedure reduces the number of parameters by converting the differential equation to a dimensionless form, thereby creating new variables a parameters, but also eliminating many old variables and parameters.

 The net gain is fewer parameters.

 The objective, then, is to manipulate the equation to replace all parameters and variables with dimension quantities.

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conversion to Dimensionless Format

#  Example:

$$
K N rN dt dN 1      
$$

$$
(5.14) divided by multiply by create unitless variables (5.13) N K NN trN t d d N t K NN trNN t d d NN K NN rNN t t d d NN 1 ) ( ) ( 1 ) ( ) ( 1 ) ( ) (                                    ⌣ ⌣ ⌣ ⌣ ⌣ ⌣ ⌣ ⌣ ⌣ ⌣ ⌣ ⌣
$$

$$
  (5.15) define   and N t N N t d d N 1 ) ( ) (    ⌣ ⌣
$$

  and     are   quanties new   the   where K N r t . 1/   ⌣ ⌣

We have reduced the number of parameters from 2 to 0,

and population size by K. and we have essentially scaled time by r 1/

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conversion to Dimensionless Format

#  Mechanical Steps:

1  . Make a table of the state variables and parameters and their units.

then for every occurrence of x in the original equations, write : ). E.g., if x is measured in gmC/liter, representing 1  unit of that variable ( ) and a variable a product of a dimensionless scaling variable ( 2. Re - write the differential equations, substituting for each state variable x x ⌣

$$
xx x ⌣ 
$$

E.g., a single, linear ODE would be :

: yields

$$
ax dt dx 
$$

$$
(5.16) axx dtt dxx ⌣ ⌣ ⌣ 
$$

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conversion to Dimensionless Format

 Mechanical Steps:

possible. For example, Eq. 5.16 becomes : any Do this for all differential equations before proceeding. Cancel by 3. Make the left -hand - side of the ODES unitless by multiplying both sides x x t ⌣ ⌣ ⌣ . /

$$
at x dt dx ⌣ 
$$

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conversion to Dimensionless Format

#  Creative Steps:

modified equations to obtain the dimensionless equations with fewer parameters. The goal of this step is to substitute the definition of the new parameters into the

Collect the terms with units together in the equations.

, so try to define the latter first. will generally be easier to define than the 5. x t ⌣ ⌣

. For example, if use that component to define appears as the only variable in one of the components of the equation, then 6. If x x ⌣ ⌣

$$
yxy tQx tKxx dt dy ⌣ ⌣ ⌣ ⌣ ⌣ 2  
$$

from the first component on the right define

$$
tK x ⌣ ⌣ 1 
$$

earlier. now stands alone. Use the same logic to define it as you did , in to the second component so that Substitute the new definition of x y x ⌣ ⌣ ⌣

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conversion to Dimensionless Format

#  Creative Steps:

the Michaelis-Menten component of the chemostat model to as much as possible before trying definitions. For example, simplify should be simplified 7. Complicated algebraic expressions involving x ⌣

$$
N N K N V m ⌣ max           
$$

before defining N ⌣ .

. use only constants and ) : ) in terms of another ( 8. It is not a good idea to define one variable ( t x y ⌣ ⌣ ⌣

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

 An Example without a Biological Interpretation

$$
fxy cy dt dy by ax dt dx     2 2 3 (5.17)
$$

|Variable|Units|
|---|---|
| |1/(t . x2)|
|b| |
|X|Unspecified|
| |Unspecified|


# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  An Example without a Biological Interpretation

Making the left side non - dimensional yields :

: define

$$
(5.18a) 2 2 3 2 y y x bt x tax dt dx   ⌣ ⌣ ⌣ ⌣ ⌣
$$

$$
(5.18b) 2 ftxxy t cyy dt dy   ⌣⌣ ⌣ ⌣
$$

$$
(5.19) and 1 1 ct y ft x   ⌣ ⌣ ⌣ ⌣
$$

after substitution :

$$
2 c t f dt xy y dt dy  
$$

$$
2 2 3 2 y bf x a dx   ⌣
$$

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  An Example without a Biological Interpretation

as : parameters. Defining needs to be defined in terms of constants and chosen to eliminate The first component on the right side, however, still has   which t t ⌣ ⌣

$$
2 f a t  ⌣
$$

The final non -dimensional equations are :

$$
2 2 1 3 xy y dy a y x dt dx    
$$

$$
(5.20) dt
$$

$$
2 1 2 bf a f y f    ⌣ ⌣
$$

$$
(5.21) where c ac a x
$$

to be unitless. substituting the units from the above table, shows which reduces the number of parameters from 4 to 1, and 1 a

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Scaling Dimensionless Quantities

 Once the non-dimensional equations are derived, we need to provide some interpretations of the constan Often these provide insight into the processes of interest.

 Non-dimensionalization has revealed to us the basic form of the equation. We can recover all the other equation of the same form that might apply to a particular model (e.g. population model) by stretch or shrinking our dimensionless time and state varia

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Buckingham Pi

 In 1914, Edgar Buckingham proved a theorem that says Given a physical relationship with P parameters and dimensional units, the number of independent dimensionless groups is P D . In other words, if the original model has P parameters, it can be reduced, without changing the mathematical behavior, to a model with PD parameters.

 Knowing the number of variables in the problem and the number of fundamental units (clearer in physica problems than biological ones), the Buckingham Pi Theorem states we can write the model using P D independent parameters.

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

#  Conservation Principle

 If a model uses a conserved quantity (e.g., g C) all whose sources and sinks are accounted for, then a st variable can be eliminated from the system of equations. Suppose a fixed amount K of carbon flows among three state variables ( x i ), each described by an ODE. Since K = x 1 + x 2 + x 3 , and K is a constant, we can rewrite any one of the x i in terms of the other state variables and total C: x 3 = K x 1 x 2 . x 3 effectively becomes an auxiliary variable and we can substitute x 1 x 2 anywhere x 3 is used.

# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

 Rule of Thumb

 Some maxims of model formulation

- 1. Know the purpose.
- 2. Know the question.
- 3. Understand the objects.
- 4. Reconcile the diagram with the rate equation.
- 5. Check the units.
- 6. Extrapolate the functions.
- 7. Simplify the model.


# 5.2 U SING THE T OOLBOX OF B IOLOGICAL P ROCESSES

 Rule of Thumb

 Techniques for model simplification:

- 1. Reduce the equations to dimensionless variables.
- 2. Aggregate state variables.
- 3. Exploit conservation principles.
- 4. Use linear functions initially.
- 5. Use descriptive, phenomenological representations before detailed, mechanistic processes. When objectives or model failure require it, increase the level of details.
- 6. Assume homogeneous space.


# 5.3 U SEFUL F UNCTIONS

#  Introduction

 Many of the biological processes can be represented by a variety of equations (e.g., hyperbolic saturation as either Michaelis-Menten or Holling disc equation). Some are nearly identical in shape, but use different parameters.

 Choosing among these, unless there are theoretical reasons, is largely a matter of taste an the appropriateness of the normal interpretation of the parameters.

# 5.3 U SEFUL F UNCTIONS

#  Linear

$$
k x k y 2 1  
$$



Exponential

$$
x k k e y 2 1 
$$

 Power

4

EXPONENTIAL

k?

k

10

15

0.1

10

20

20

40

B

k,

k,

kr

0

21

219

3

~50

B

G0

40

20

40

10

$$
3 2 1 k k x k y  
$$

# 5.3 U SEFUL F UNCTIONS

#  Saturation

$$
) ( ) ( 3 1 k x k k x k y          
$$

$$
) (1 2 1 3 2 x k e k y    
$$

 Hill

$$
          2 2 2 3 1 k k k x k x k y
$$

1.0

0.8

0.6

SATURATION

B /

0,4

k,

k

hyperbolic

exponentlal _

20

40

60

1

1

02

0

100

D

HILL

0,0

B

0.6

0,4

kz

ka

20

1

20

0,?

20

6u

# 5.3 U SEFUL F UNCTIONS

 Richards Absolute

$$
4 4 3 1/ 2 1 1 1 1 k x k k e k k k y                    
$$

 Richards Relative

$$
                  2 3 2 1 1 k k x x k k y
$$

150

AICHARDS

k,

(absoluto)

100

3

03

100

100

03

5

10o

25

100

50

100

200

J00

50o

F

RICHARDS

(relatlvø)

0,04

0,02

C

D

kz

5 100

03

100

1

,03

2

100

03

3

100

46

60

00

# 5.3 U SEFUL F UNCTIONS

 Blumberg

$$
                  2 4 3 1 1 k k k x k x y
$$

0,8

0.6

0,4

0.2

k kz

ka

A ,05

2 100

100

D

00 1,4

100

 Complemented Weibull

$$
                3 2 1 exp k k x k y
$$

20

40

60

80

H

WEIBULL

0.8

D

0,6

A

0,4

k;

k

100

2

1

75

100

1

100

6

1

100

20

1

60

100

10

# 5.3 U SEFUL F UNCTIONS

#  Triangular

$$
        3 5 4 3 2 1 k x    if x k k k x    if x k k y
$$

#  Maxima

$$
(1 4 2 3 2 1 x k x k x k k k e k e y e k x y   
$$

$$
) 3 1
$$

I

15

0.05*

ITRIANGULAR

125

100

20

40

60

80

k,

kz

8

06

41

k

MAXIMUM

100

# 5.3 U SEFUL F UNCTIONS

 Temperature Optimum

$$
                         6 5 2 5 7 2 4 2 1 ) ( exp ) ( ) ( 3 3 3 k k k x k k k x k k x k y k k k
$$

5

0,5

k,

ka

20.0 30

2

283 30

2

38.7

2

28.3 J0

2

k

0

40

kz

02

02

02

K

TEMPERATURE

OPTIMUM

D

 Double Weibull

$$
  5 4 3 2 ) / ( ) / ( 1 1 k k k x k x e e k y    
$$

10

20

30

40

50

DOUBLE

k,

Kz

WEIBULL

125

15

18

2

5

A -

2

50 10   50

0.5

20

40

60

80

100

# 5.3 U SEFUL F UNCTIONS

#  Trigonometric

$$
     N i i i i x x A M y 1 0 )) ( cos( 
$$

#  Cubic Spline

Cubic splines is such a method that uses a third order polynomial for each subset of the data and smoothly joins the separate cubic equations together.

$$
n n k x k x k x k y      … 2 2 1 0
$$

#  Polynomial

$$
n n a x a x a x a y      … 2 2 1 0
$$

#  Rational Functions

$$
n n n n b x b x b x b a x a x a x a y           … … 2 2 1 0 2 2 1 0 1
$$

5.3 USEFUL FUNCTIONS

#  Summary of Useful Functions

5.3 USEFUL FUNCTIONS

#  Summary of Useful Functions

5.3 USEFUL FUNCTIONS

#  Using software to find suitable functions

http://www.sigmaplot.co.uk/products/tablecurve2d/ta https://simfit.uk/simfit.html

# 5.3 U SEFUL F UNCTIONS

 Function Categories

 Linear Equations

 Polynomial Equations

 Rational Equations

 High Precision Polynomials and Rationals

 Chebyshev Series Equations

 Fourier Series Equations

 Constrained Non-Linear Rationals

 Non-linear Equations

 Peak Functions

 Transition Functions

 Kinetic Functions

 Waveform Equations

 General Non-Linear Equations

# 5.4 E XAMPLES

#  Flows with Different Units

Since the state variables have different units, we m parallel model, with information flows between state variables and rates to indicate the interactions.

2

9 P

$$
dP aP - dt
$$

b

Mass

$$
= cQ-dQ dt
$$

Figure 5.5: Flows with different units.

# 5.4 E XAMPLES

#  Driving Variable

$$
dX =
$$

$$
dt T = M + Acos(wt)
$$

Temp

Elloct

Figure 5.6: Driving variable and multiple input and outputs.

# 5.4 E XAMPLES

#  Riding a Bike

The problem is to describe the dynamics of the fron two-wheeled bicycle when it is driven (a) with hand normal position (left hand on the left handlebar, r the right handlebar) and (b) with hands reversed.

Right Hand

$$
dr = aD dt dl = ~bD dt dD = dt
$$

Lelt Hand

Pressura

Prassure

Ditlarence

Wheal

Devlation

Figure 5.7: Feedback control for riding a bicycle.

# 5.4 E XAMPLES

#  Brewing Beer

 There is only a finite amount of sugar at the begin depleted over time.

 Excessive alcohol will kill yeast cells.

$$
dS dt dY 7 dYA dt dA abs Y
$$

Sugar

s:Y

Mass

9 €

Yeast

Action

Alcohol

$$
dt
$$

Figure 5.8: Alcohol production by yeast in beer fermentation.

# 5.4 E XAMPLES

#  Brewing Beer

 Vensim Model

# Simple Beer Brewing Model

brewing status

Beer

Yeast

Yeastcell

Yeast cell death

3.75

formation rate

rate

Sugar -

yeast

23

mass acton

Sugar

Alcohol

production rate

Sugar

breakdown rate

that yields CO2

Alcohol

125

2

3

4 5  6

7

8

9

10

Alcohol

Current vdfx

Sugar

Current vdfx

Yeast

Current vdfx

