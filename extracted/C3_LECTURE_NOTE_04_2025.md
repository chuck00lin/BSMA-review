# L ECTURE 4:

# Q UANTITATIVE M ODEL F ORMULATION : I

# OUTLINE

4.1 From Qualitative to Quantitative

4.2 Finite Difference Equations and Differential Equations

4.3 Biological Feedback in Quantitative Models

4.4 Example Model

# 4.1 F ROM Q UALITATIVE TO Q UANTITATIVE

 The boxes of Forrester diagrams represent the objec of interest: the variables whose dynamic quantities wish to determine over time.

 For the boxes of Forrester diagrams, we must supply state (dynamic) equation that relates the value of variable at the next point in the future with the current value and all of the inputs to and outputs the variable's box.

 The rate equations involve the parameters, auxiliary equations, and driving variables as specified by the Forrester diagram.

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

 Finite Difference Equations

 The finite difference equations have the general form:

$$
(4.1) ) ( 1 t t f N N  
$$

 The function f () can be arbitrarily complicated. For some f (), we can isolate N t as a separate element:

parameters   variables,   state ( 1 f N N t t   

 Suppose f () = rN , which is the classical ecological model for density-independent population growth:

$$
(4.3) t t t rN N N    1
$$

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Finite Difference Equations

2

Figure 4.1: Forrester diagram for density-independent population growth

 Classical analytical solution to the densityindependent growth model in discrete time:

$$
(4.4) 1 0 1 3 0 2 2 3 2 0 0 1 1 1 2 0 0 0 1 ) (1 ) (1 ) (1 ) (1 ) )(1 (1 ) (1 ) (1                        t t t r N r N N r N rN N N r N r r N r N rN N N r N rN N N ⋮
$$

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Finite Difference Equations

 Recursive finite difference equations assume time i discrete. This implies that no events or processes between increments of time.

 Many biological systems match this situation to a satisfactory degree. An example is the life cycle o insect that breeds synchronously in the fall. Birth death in this case defines the discrete nature of t

 When we use finite difference equations we are asserting that time and biological processes are discontinuous and that the equations are exact representations

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Differential Equations

 Differential equations are the continuous time version of finite difference equations.

 The derivative of a function y with respect to a single variable x is:

$$
(4.5) x y y dx dy x x x x       0 lim
$$

 Two general approaches to obtaining the integral:

 Treating the integral as a summation.

 Applying the rules of integration.

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Differential Equations

 Treating the integral as a summation:

$$
(4.6) x x y y derivative i i x i     ) (2
$$

(a)

150

50

(b)

20

15

dy

dx

10

5

~10

0

10

10

Figure 4.2: (a) The parabola y = (b) The derivative x2 4 C, dyldx = 2x (solid line) and a discretization of the derivative. of y =

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Differential Equations

 Applying the rules of integration:

$$
dy  2
$$

C x y C x dx x C y dy dx x dy xdx dy x dx                 2 2 2 1 2 2 2 2 gives   integrals   these   Equating side   right   integrate     side   left   integrate     variables   separate      

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Integrating ODEs

 An ordinary differential equation (ODE) is any equa involving a derivative of a dependent variable with respect to its independent variable.

 The ODE of the density-independent population model in ecology:

$$
(4.7) rN dt dN 
$$

 There are, as before, two general strategies for find the integral: apply the rules of integration, or approximate the area under a curve by summing.

# 4.2 F INITE D IFFERENCE E QUATIONS AND D IFFERENTIAL E QUATIONS

#  Integrating ODEs

 Applying the rules of integration:

$$
rt rt C C rt t N e e e e N C rt N C rt dt r rdt C N dN N rdt N dN rN dt dN 0 3 2 1 3 3 ln ln 1                    integrate right side integrate left side separate variables
$$

 Summation technique using Euler approximation

$$
(4.8) t rN N N derivative t t t t     ) (
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  From Forrester Diagram to Equations

- 1. The first rule is that every level in a Forrester diagram is a state variable that requires a differential (or difference) equation.
- 2. The second rule is that, at a minimum, every material flow into and out of a state variable requires an e algebraic expression. The sum of these expressions associated with the inflow and outflow arrows is th right-hand side of the differential equation.

$$
    outflows inflows dt dx
$$

- 3. The third rule is that although biological systems are complex, many of them share a few basic processes that have similar mathematical expressions.


# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Constant and Bulk Flow Rates

Fin

F

Dut

ds

5

Fout

Fin

dt

Fin

5

Time

5

Figure 4.3: Constant rate of flow into a state variable.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Constant and Bulk Flow Rates

S2

6,2

4

Fo1

S1

Faz

Sourceo

6s

^

Figure 4.4: Modified Forrester diagram for constant rates of flow among three state variables.

$$
34 32 13 3 24 32 12 2 13 12 01 1 F F F dt dS F F F dt dS F F F dt dS          (4.9)
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Dynamic Relative Rates

B

S2

S,

Figure 4.5; Simple information transfer illustrating the influences of state varlables on rates.

$$
(4.10) ⋯ ⋯    1 1 ) ( A S dt dS
$$

$$
(4.11) ⋯ ⋯    2 1 ) ( B S dt dS
$$

$$
(4.12) ⋯ ⋯    2 1 1 ) ( ) ( B S A S dt dS
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Dynamic Relative Rates

 The quantities A and B are relative or per capita rates

 An example of the island biogeography model:

$$
(4.13) P R E I I P R E P R I I dt dR x x x x x x ) ) / (( ) / ( ) / (      
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Feedback

 Feedback is pervasive in biological systems and is one of the fundamental processes that is contained in almost all interesting models.

 Feedback refers to the relationship in which increa or decreases of the value of one or more variables affect the rate at which a process occurs.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Feedback

DIRECT

INDIRECT

A

negative

B

4

B

positive

B

A

B

Figure 4.6: Qualitative analysis of direct and indirect effects of system influences produceither posltive or negative feedback. The sign on each arc represents the effect of the influencing variable on the variable that terminates the arc. ing

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Positive Feedback

 The critical feature of positive feedback is that t increases without bound.

25

1.0

(b)

(a)

ds

0.05 t

0.055

20

0.8

dt

15

0

0.6

0'

ds

s

10

0.4

slope

dt

5

0.2

0

10

15

20

10

20

30

40

50

60

Time

s

Figure 4.7: Direct positive feedback. (a) Relation of absolute rate of change in a state variable to the value of the variable and a differential equation that behaves in this way. (b) The resulting dynamics.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Negative Feedback

 The rate of the process is bounded for positive val of the controlling variable.

 There are three primary mathematical methods by which this condition can be implemented: self-inhibition, limitation by extrinsic factors, process saturation .

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Self-Inhibition

 The density-dependent, logistic population growth:

$$
N K r rN N K N r dt dN             1 2
$$

$$
(4.14)    
$$

$$
(4.15) K rN r dt N dN   1
$$

where r is the maximum per capita rate of change K is the carrying capacity of the population. Since this model has a single state variable, N is the controlling state variable .

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

 Self-Inhibition

 The density-dependent, logistic population growth:

1.5

0.05

(a)

(b)

dNdt

0.04

dNIN dt

1.0

dN

dN

0.03

N dt

dt

0.02

0.5

0.01

20

60

80

100

20

40

60

40

100

80

N

N

Figure 4.8: (a) Per capita rate of change in density-dependent model as a function of population size.   (b) Absolute rate of change in density-dependent model as a function of population size.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Ratios

 An example of additive self-inhibition:

$$
2 cy ay dt dy  
$$

 An example of multiplicative self-inhibition (for y

$$
y b dt dy / 
$$

 A safer formulation of the above equation, which lim dy/dt to b as y approaches 0:

$$
y b dt dy   1 1
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Extrinsic

 The Newton’s Law of Cooling:

$$
) ( T k T dt dT a  
$$

 By an extrinsic factor, we mean any quantity "outsid of the state variable to which the differential equ applies. This other quantity may be in the nebulous "unmodeled" environment (e.g., ambient temperature) or it may be the current state or associated auxili variable of another modeled state variable.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Saturation

 Negative feedback frequently emerges in systems through an interaction between the quantity of the donor variable and the ability of the recipient to convert the donor substance.

 By analogy with chemical dynamics where this is common, negative feedback puts bounds on rates by saturating the recipient.

4.3 BIOLOGICAL FEEDBACK IN QUANTITATIVE MODELS

#  Saturation

 The Michaelis-Menten model of enzyme kinetics:

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Saturation

 The Michaelis-Menten model of enzyme kinetics:

$$
(4.16) k EP k C k C k ES dt dE 3 4 2 1     
$$

$$
(4.17) k C k ES dt dS 2 1   
$$

$$
(4.18) k EP k C k C k ES dt dC 3 4 2 1    
$$

$$
(4.19) k EP k C dt dP 3 4  
$$

 Assuming that (a) the experiments are performed whe present only at negligible concentrations, and (b) formation of C equals its breakdown rate, the rate formation is described by the Michaelis-Menten equa

$$
(4.20) S K S V V m         max
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Saturation

 This basic curve is scaled (parameterized) by two parameters: V max (the maximum reaction velocity) scales the velocity to which the curve is asymptoti at large S ; K m scales how "fast" the curve rises toward the asymptote.

 The Holling disc equation which relates the numbers of prey (y) consumed by a predator in a fixed period of time (e.g., 1 day or 1 experiment duration) to the density of the prey available:

$$
(4.21) ahx x aT y T         1
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Combined Feedback Interaction

 In some systems, saturation or positive feedback can combine with inhibition to produce more complicated relations between variables and rates.

 Usually, this general phenomenon of combined feedback is produced by the action of two or more biological mechanisms (e.g., light saturation of photoreceptors and degradation of enzyme systems at high light intensities, or mate location and competi Consequently, this situation is frequently modeled a the product of two separate factors.

 For example, photoinhibition can be modeled as:

$$
(4.22) e aI P P decrease aI increase           ) ) ( ( 1 max
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Saturation

 Allee effect: The Allee effect is a phenomenon in biology characterized by a positive correlation bet population density and the per capita population growth rate in very small populations.

 A simple example of an Allee effect given by the cub growth model

$$
1 1 dN N N rN dt A K            
$$

where the population has a negetive growth rate for N < A, and a positive growth rate for A < N < K (assuming 0 < A < K). A is called the Allee thresho

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

 Saturation

 Allee effect

Strong Allee Effect

1

K

Weak Allee Effedt

9

1

K

No Allee Effect

1

K

Abundance (N)

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Mass Action

 The Law of Mass Action states that the rate of a reaction is proportional to an integral power of th concentrations of all substances taking part in the reactions.

$$
b a aQ P R 
$$

where a is a constant of proportionality, and are integer powers. The order of the reaction relative to Q or P is a and b , respectively. The order of the overall reaction is the sum of the powers.

 The values of the orders of the relations are often determined by the stoichiometric or weight relations of the compounds involved in the reaction.

$$
k C k AB dt dC 2 2 1   k1 A + 2B
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Mass Action

 An example of the classical Lotka-Volterra predator prey equations:

$$
mass action positive feedback aVP rV dt dV  
$$

$$
(4.24) (4.23) death conversion dP abVP dt dP  
$$

where the victim ( V ) grows in a density-independent fashion with rate r . Predators ( P ) die at a constant per capita rate d . The term aVP (Eq. 4.23) quantifies the rate at which prey ( V ) are consumed by predators ( so a is the search rate. Predators convert the food consumed into new predators with an energetic efficiency b .

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

 Multiple Controlling Factors

 Multiple factors can control a single process rate.

 There are two different, common situations:

 The equation for the rate is a univariate function a primary influencing variable (i.e., the x-axis, suc as available light intensity), and one or more of th parameters of this equation is modeled as a function of a second controlling factor (e.g., g C).

 Second, the rate is the outcome of several interacting factors that combine to create a function having multiple independent variables.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Multiple Controlling Factors

#  Example of the first case:

A simple model of net photosynthesis rate in plants when it is controlled by both light intensity (I) a carbon availability (C). The primary variable of th equation is I and we assume an asymptotic relations analogous to the Michaelis-Menten relation. The eff of carbon is to increase linearly the maximum rate:

$$
a
$$

$$
bIC P bC P P I IP P     a a max max max
$$

$$
(4.25) bC I  a
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Multiple Controlling Factors

 The second case concerns multiple factors affecting process that requires all of the factors.

 The biological case of plant growth in the presence three nutrients (carbon, nitrogen, and phosphorus).

Environment

Environment

Plant

N

N

Environmont

P

Figure 4.10: Plant growth in which three nutrients interact. On the right is shown Monod growth curves as determined by single-variable experiments that hold the other two nutrients constant.

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

#  Methods to Combine the Controlling Variables

Consider the simple case with just a single limitin (N). Nutrient uptake across cell walls is mediated and enzymes, so we use Michaelis-Menten kinetics to relate biomass increase to nutrient concentration. applied to growth rates, we have the Monod equation

$$
N m N N B N K N dt dB N m m           *
$$

where m * N is the maximum rate of incorporation of N into plant material per g N of plant material (i.e., a re per capita rate). The product of m * N and the expression in parentheses is m (the actual relative rate).

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

 Methods to Combine the Controlling Variables

 Leibig’s Law of the Minimum:

$$
                                              P K P N K N C K C P N C m m m , , min * m m
$$

 Multiplicative Rates:

$$
                                      P K P N K N C K C P N C m m m * m m
$$

 Arithmetic Average Rate:

$$
                                      P K P N K N C K C P N C m m m 3 1 * m m
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

 Methods to Combine the Controlling Variables

 Mean Resistance (Harmonic Mean):

$$
(4.26) S B S S eff  
$$

Using the resistance analogy, the integrated effect is computed from:

$$
eff n i i eff eff n i i eff eff eff eff eff eff H S n H S I P N C I * 1 , 1 , 1 1 1 1 1 1 1 m m                                  
$$

# 4.3 B IOLOGICAL F EEDBACK IN Q UANTITATIVE M ODELS

 Methods to Combine the Controlling Variables

 Additive Rates (O’Neill et al., 1989):

$$
k C CN k N CN P PI eff 1 2   
$$

 Summary of Multiple Controls:

 Either replace a constant with a function of the secondary controlling variables (case 1), or use a form of competing factors (case 2).

 In the second case, the harmonic mean and the Law of the Minimum seem to be the most reasonable forms to use, but this can depend on the system.

 If the individual functional forms are MichaelisMenten, then consider using the additive method.

# 4.4 E XAMPLE M ODEL

#  The Chemostat Model

 A chemostat is a piece of laboratory equipment that grows microbes in a flow-through system of constant volume, V , that continuously delivers a constant concentration of nutrients to the population.

$$
P V N K R R K R R N dt dN K R R K R R Y N R R P V dt dR K R R K R R Y N R R P V dt dR m m m m m m ) / ( , min , min ) )( / ( , min ) )( / ( 2 1 2 1 2 1 2 2 1 1 * 2 2 1 1 2 * 2 20 2 2 2 1 1 1 * 1 10 1                                       m m m (4.27)
$$

where m * is max[ m 1 , m 2 ], Y i is a constant to convert cell numbers to appropriate nutrient units, and half-saturation constants.

# 4.4 E XAMPLE M ODEL

#  The Belousov-Zhabotinsky Reaction Model

 The Belousov-Zhabotinsky (BZ) reaction is a classica of a non-equilibrium chemical oscillator in which t components exhibit periodic changes in concentratio Field and Noyes model (1974) can be expressed as fol

A+Y X 

X+T P 

B+X 2X+Z 

2X Q 

Z fY 

This relates to the chemical mechanism by X=HBrO Z=Ce 4+ . A, B, P, Q are non-intermediates and can be regard as constants.

# 4.4 E XAMPLE M ODEL

#  The Belousov-Zhabotinsky Reaction Model

 The Field and Noyes model (1974) expressed in diffe equations:

$$
2 1 2 3 4 1 2 5 3 5 2 dX k AY k XY k BX k X dt dY k AY k XY fk Z dt dZ k BX k Z dt          
$$

 A simpler reaction model by Turner (2009) can be ex as: ( a , b ,  are rate constants)

$$
Q C + A - 2C [A]t+1 [AJt + [A]t (a[B]t [B]t+1 a[A]t) [c]t+1 ß[B]t )
$$

4.4 EXAMPLE MODEL

#  The Belousov-Zhabotinsky Reaction Model

##  Spirals and waves appear spontaneously and unpredictably in the concentration profiles of the reaction components on a scale dictated by the valu of α, β and γ.

For α=β=γ=1 For α=1.2, β=γ=1

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 4.4 E XAMPLE M ODEL

 The Belousov-Zhabotinsky Reaction Model

 Vensim Implementation

# A simple model of the Belousov-Zhabotinsky reaction

Rate constant

Rate constant

Rate constant

beta

alpha

gamma

Reactant A

20

Reactant A

Creation rate

Depleton rate A

10

Reactant B

Depletion rate B

Creation rate €

Reactant €

Time (Second)

Reactant A

Current

Reactant A

Base

α=1.2, β=γ=1 (Base) compared with α=1.6, β=γ=1 (Current)

10

