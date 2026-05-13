# L ECTURE 6:

# N UMERICAL T ECHNIQUES

# OUTLINE

6.1 Mistakes Computers Make

6.2 Numerical Integration

6.3 Numerical Instability and Stiff Equations

6.4 Integrating ODEs with Variable Time Steps

6.5 PDEs and the Method of Lines

# 6.1 M ISTAKES C OMPUTERS M AKE

#  Representation of Numbers

 In most scientific programming, we are interested in three data types: characters, integers, and real numbers.

 All data types must be stored using a finite number of bits, and this fact produces the opportunity for error.

 The value of integer is determined by the of the computer, which in turn is determined by the size of the databus on the motherboard.

 More powerful computers have wider databuses.

# 6.1 M ISTAKES C OMPUTERS M AKE

#  Representation of Numbers

 A floating point number is a real number represented in such a way that the decimal point can float so that a fixed number of significant dig is always represented, no matter how large or small the absolute value of the number.

 A floating point number is composed of a mantissa and an exponent, either one of which may be positive or negative.

Exponents are integers, while the mantissa is

 Exponents are integers, while the mantissa interpreted as a real number scaled by the exponent.

# 6.1 M ISTAKES C OMPUTERS M AKE

#  Representation of Numbers

 The number of bits used for the mantissa represents the precision (number of significant digits) of the number.

 Single Precision vs. Double Precision

Table 6.1: Format parameters for single and double precision numbers in the IEEE 754 standard for floating numbers. Shown are the number of bits used for mantissa and exponents; the approximate number of decimal significant digits; and the maximum and minimum numbers. point

| |Mantissa|Exponent|Digits Sig:|Max|Min|
|---|---|---|---|---|---|
|Single|23|8|9|3,403 * 1038|1.175 x 10-38|
|Double|52|11|15|1.798 * 10308|2.225 x 10-308|


 If the exponent is negative and the operation on th exponent causes an overflow in the exponent bit pattern, the condition is called floating point since the operation attempted to create a number smaller than that which could be represented.

# 6.1 M ISTAKES C OMPUTERS M AKE

 Round-Off, Truncation, and Propagation Errors

 Storage limitations in the mantissa produce overflow or underflow and these become off errors .

 Modern floating point chips that implement the IEEE 754 provide the programmer the ability to determine what method to use. The choices include always round up , always round down round to nearest . The most accurate (and default) method is to round to nearest.

# 6.1 M ISTAKES C OMPUTERS M AKE

 Round-Off, Truncation, and Propagation Errors

 Round-off issues can have important implications for basic scientific programming.

 Example:

Bad Good mean=0 .0; gmean=0 .0; for (i: 1 7 I) for (i: 1 4 mean mean + A [i] gmean = gmean 4 (A[i]-gmean) /i mean = mean/V

# 6.1 M ISTAKES C OMPUTERS M AKE

#  Round-Off, Truncation, and Propagation Errors

 Two other kinds of errors occur depending on the operations used in the algorithm: truncation errors propagation errors .

 Truncation errors occur because the algorithm approximates a function as an infinite series trunc after the first n terms.

 Propagation errors are errors made at every stage of an iterative algorithm and that accumulate over the en solution.

 In an iterative procedure, these sources produce two types of error: local error (at every solution step) and global error (deviation from the true solution).

# 6.2 N UMERICAL I NTEGRATION

#  Slope Fields

 The solutions of an ordinary differential equation can be plotted in a two-dimensional space in which the y -axis is the dependent variable and the is time ( t ).

Figure 6.1: Slope field and two true solutions of a differential equation.

# 6.2 N UMERICAL I NTEGRATION

#  Slope Fields

 Taking the derivative of the solution function (generally unknown) at a point on the time axis wil give the numerical values of the original differential equation for the particular ( we calculate the derivative at many of these pairs, we will produce a slope field.

 The problem in numerical approximation of the true solution is to find the subset of slopes in th slope field that corresponds to the true solution.

# 6.2 N UMERICAL I NTEGRATION

#  Euler’s Method

 The strategy of numerical integration is to move from the initially correct slope in the slope field the next correct slope, from there to the next correct slope, and so on.

 The Euler method is the simplest, most straightforward approximation.

$$
(6.1) ) , ( t y f t y y t t t t    
$$

# 6.2 N UMERICAL I NTEGRATION

#  Euler’s Method

Yaa

By

Y?a

Ay

Yo

Time

Figure 6.2: A series of Euler approximations (straight lines) to a true solution (curved line) over At solution intervals_

# 6.2 N UMERICAL I NTEGRATION

#  Euler’s Method

 Typically, we must solve several differential equati simultaneously and these equations are a system in sense that their derivatives are functions of the o state variables. For example, a model of predator an prey populations is

$$
(6.2) dP bcVP dt dP bVP rV dt dV    
$$

 In the Euler method, these continuous equations are replaced by the approximations:

$$
    (6.3) t dP bcV P P P t bV P rV V V t t t t t t t t t t t t          
$$

 We should always first calculate the rates (derivat then update the states.

# 6.2 N UMERICAL I NTEGRATION

#  Runge-Kutta Basics

 The Runge-Kutta (RK) method has many advantages. It is easy to code; its numerical behavior is less sensitive to the size of Euler method. In addition, it is remarkably efficien a large  t provides accurate solutions.

 The Runge-Kutta method uses several estimates of the slope of the function.

 The Runge-Kutta is actually a family of algorithms in which the members are distinguished by the number of slope (derivatives) calculations performed and weights given to those slopes.

# 6.2 N UMERICAL I NTEGRATION

 Runge-Kutta Basics

 When the number of derivatives computed is two, we have the second-order Runge-Kutta (RK-2, also known as the mid-point method ).

y

Y

t+At

Time

Figure 6.3; Second-order Runge-Kutta integration. 4?y is the second estimate of the rate 2y and adding to

# 6.2 N UMERICAL I NTEGRATION

 Runge-Kutta Basics

 The algorithm of RK-2

- 1. Calculate derivative 1 using current solution and then first tentative solution

$$
) , ( 1 t t y f y   
$$

$$
(Tentative step based on 1/2 time step) /2 t  
$$

$$
1 1 y y y t
$$

- 2. Calculate derivative 2 using tentative solution 1.


$$
t t t y f y      / 2) , ( 1 2
$$

(No further tentative steps needed)

3. Calculate new value for y by combining the previous  i y with different weights.

$$
) (1 ) (0 2 1 y y y y t t t      
$$

# 6.2 N UMERICAL I NTEGRATION

#  Runge-Kutta Basics

 An example of RK-2

The numerical calculations for one time step of the on the equation dy/dt = ay ,

$$
16.25 6.25 10.0 6.25 6.25 1 5.0 0 6.25 (0.5)(12.5)(1.0) 12.5 5.0 / 2 10 5.0 (0.5)(10)(1.0) 1.0 0.5, 10.0, (0) * 2 2 1                         y y y y y y t a y i t t t t Weighted are : with
$$

$$
 t t
$$

Compare this estimate with the true solution :

$$
16.4872 1.0  y
$$

# 6.2 N UMERICAL I NTEGRATION

 Runge-Kutta Basics

 The algorithm of RK-4

- 1. Calculate derivative 1 using current solution and then first tentative solution

$$
) , ( 1 t t y f y   
$$

$$
(Tentative step based on 1/2 time step) /2 t t  
$$

$$
1 1 y y y
$$

- 2. Calculate derivative 2 using tentative solution 1 a then second tentative solution.

$$
(Tentative step based on 1/2 time step.) /2 / 2) , ( 2 2 1 2 y y y t t t y f y t      
$$

- 3. Calculate derivative 3 using tentative solution 2 a then third tentative solution.


$$
(Tentative step based on 1  whole time step.) y y y t t t y f y t 3 3 2 3 / 2) , (      
$$

# 6.2 N UMERICAL I NTEGRATION

 Runge-Kutta Basics

 The algorithm of RK-4

4. Calculate derivative 4 using tentative solution 3

$$
t t t y f y     ) , ( 3 4
$$

Last tentative solution not needed.

5. Calculate new value for y by combining the previous  i y with different weights.

$$
t y y y y y y y y * 4 3 2 1 * ) 2( ( 6 1         
$$

$$
)
$$

$$
t t t t 
$$

# 6.2 N UMERICAL I NTEGRATION

#  Runge-Kutta Basics

Table 6.2: Comparison of Runge-Kutta and Euler methods solving dyldt = 0.5, At = 1.0,0.5,0.25

|Time|Euler At = 1.0|Euler At = 0.5|Euler At = 0.25|RK-2 At = 1.0|RK4 At = 1.0|True|
|---|---|---|---|---|---|---|
|0.0|10.0|100|10.0|10.0|10.0|10.0|
| |15.0|15,625|16.0181|16.2500|16.4844|16.4872|
|2,0|22.5|24,400|25.6579|25.3900|27.1735|27.1828|


- 1. All methods become less accurate over time.
- 2. The Euler method becomes more accurate as
- 3. The Euler method is less accurate than the Runge-Ku method even when the methods use the same number of derivative calculations [e.g., Euler (  t = 0.5) versus RK-2, and Euler (  t = 0.25) vs RK-4].

- 4. RK-4 is remarkably accurate for this simple ODE.


# 6.3 N UMERICAL I NSTABILITY AND E QUATION

 Desirable integration methods are those that reduce the errors more effectively at large step sizes. RK generally more effective for many more problems tha Euler, but RK fails for certain equations.

 A prime example of these are stiff equations. Stiff can arise when the equations use several, very different time scales.

 Different time scales in equations often cause the solution algorithm to add very large numbers to ver small numbers. This is a situation that produces la round-off and truncation errors.

# 6.3 N UMERICAL I NSTABILITY AND E QUATION

 Some examples of systems whose differential equations may be stiff are:

- 1. Algal Nutrient Uptake and Cellular Division uptake is a rapid process that occurs over microseconds; cell division requires several hours (Abbott 1990).
- 2. Photosynthesis and Enzymatic Reactions light levels will produce a rapid change in enzyme kinetic parameters but a relatively slow change in photosynthesis at the leaf level (Gross 1982).
- 3. Rotating Rocket Orbiting Earth : The rocket rotation is fast compared to the orbiting time (Rice 1983).
- 4. Refinery Control : Chemical reactions occur rapidly compared to the temperature response of the large vats (Rice 1983).


# 6.3 N UMERICAL I NSTABILITY AND E QUATION

 There are two broad approaches to solving this problem of multiple time scales:

- 1. The first method is most applicable to computer simulation in which we create submodels correspond to the subsystems having different time scales.
- 2. The second approach comes from physics and does not attempt to identify and model specific subprocesses that account for the existence of the time scales. Rather than modeling these as separate subsystems, a numerical approach is to find a better method of integrating the equations.


# 6.3 N UMERICAL I NSTABILITY AND E QUATION

#  Examples of Stiff Equations:

 The problem of stiff equations arises simply becaus the parameters in the system of ODES vary over seve magnitudes.

$$
(6.4) v u dt dv v u dt du 1999 999 1998 998     
$$

 Mathematically, stiff equations are a practical prob in linear systems such as this when all the eigenva are negative and the largest eigenvalue is very much larger (at least 10 times) than the smallest eigenv

 There are two possible solutions: (1) decrease the size appropriate to the fastest time scale, and (2) different numerical method.

# 6.3 N UMERICAL I NSTABILITY AND E QUATION

#  Examples of Stiff Equations:

 Robertson’s Chemical Reaction Systems

$$
7 4 0.04 310 10 (slow) (very fast) (fast) A B B B C B B C A C        
$$

which lead to the equations

$$
4 1 1 2 3 1 : 0.04 10 (0) dy A y y y y    
$$

$$
2 1 1 : 0.04 dt dy B y dt   4 7 2 2 3 2 2 10 3 10 (0) 0 y y y y C   
$$

$$
7 2 3 2 3 : 3 10 (0) 0 dy y y dt   
$$

6.3 NUMERICAL INSTABILITY AND EQUATION

#  Examples of Stiff Equations:

 Robertson’s Chemical Reaction Systems

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 6.3 N UMERICAL I NSTABILITY AND E QUATION

 In conclusion, time scales and stiff equations are a problem because biological dynamics occur over many different time scales.

 It is advisable, when studying equations with which does not have much previous experience, to monitor t net rates of changes of each state variable. The re rates of change should stay within reasonable bound

 As a very crude check, if (1 /x i )( dx i /dt ) > 0.2 in any time step, then you should consider reducing the time step or methods developed for stiff equations.

 At the least, during preliminary modeling stages, the modeler should vary the simulation time step over a range to determine the presence of spurious behavio

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

#  Effect of the Step Size on the Global Errors

Round-off

Truncation

Instability

hP

Global error vs. hP

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

 The simplest approach to optimizing the time step f any integration method is to calculate, at every iteration, the estimate for the next value using the current time step and an estimate using a smaller t step.

 If these differ by an unacceptable amount, then the truncation error is too great and a smaller step si needed. This test is repeated as many times as necessary within the current time step until the er criterion is satisfied.

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

#  For the Euler method, the calculations are:

t t t t t t t t t t t t t t t y f t y y t y f t y y t y tf y y                    two     midpoint       step   full         * /2 * /2 * * /2 ) , ( 2) / ( ) , ( 2) / ( ) , (

The absolute (global) error estimate is

$$
t t t t t y y E      *
$$

state variable is and the error relative to the current magnitude of the

$$
t t t y E e   
$$

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

 Given the calculated e  t , we can calculate another which is the time step needed to exactly produce th target or desired error.

 The error estimates are proportional to ( this fact to note that if e  t  (  t ) 2 , then there is a target error proportional to some other time step: e’  t  (  ’t ) 2 . Using these two proportionalities, we have:

$$
1/2 ' '              t t e e t t
$$

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

 This variable time step approach also applies to RK each of the four steps must be performed for both t time step and the two half time steps.

 Therefore, in the step-doubling method for RK-4, we m calculate the derivative 11 times, as compared to 4 nonvariable method.

 The Runge-Kutta-Fehlberg (RKF or RKF45) method which an alternative that also uses an estimate of the tr error to determine the best time step. This method fifth-order RK method that requires six calculation derivatives.

 The major feature of the RKF algorithm is that it g error estimate using only six evaluations of the de rather than the 11 needed for the time step varying method described above.

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

#  MATLAB functions

# Syntax

[T,Y] = solver (odefun,tspan,y0)

[T,Y] = solver (odefun,tspan,y0,options)

[T,Y,TE,YE,IE] = solver (odefun,tspan,y0,options)

sol = solver (odefun,[t0 tf],y0...)

where solver is one of ode45, ode23, ode113, ode15s, ode23s, ode23t, or ode23tb.

|Solver|Problem Type|Order of Accuracy|to Use|
|---|---|---|---|
|ode45 Nonstiff|Medium|Most of the time. This you try.|ode45|
|ode23 Nonstiff|Low|For problems with crude error tolerances or for solving moderately stiff problems.|ode23|
|ode113 Nonstiff|Low to high|For problems with stringent error tolerances or for solving computationally intensive problems.|ode113|
|Stiff|Low to medium Low|If ode45 is slow because If using crude error|ode15s|
|Stiff|Low|If using crude error tolerances to solve stiff systems and the mass matrix is constant.|ode23s|
|ode23t Moderately Stiff|Low|For moderately stiff problems if you need a solution without numerical damping.|ode23t|
|Stiff|Low|If using crude error systems.|ode23tb|


# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

#  MATLAB functions

% Main program ode45demo function ode45demo options = odeset('RelTol', 1e-4, 'AbsTol',[1e-4 1e-5]); [T,Y] = ode45( @model1, [0 600], [100 200], options plot(T,Y(:,1),'-',T,Y(:,2),'-.');

# % Prey Predator Model called by ode45

function dy = model1(t,y) k1 = 0.05; k2 = 0.10; k3 = 0.002; k4 = 0.002; dy = zeros(2,1); % a column vector

$$
dy(1) = (k1-k3*y(2))*y(1); dy(2) = (k4*y(1)-k2)*y(2);
$$

300

250

200

150

100

50

0

0

100

200

300

400

500

600

# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

#  Python Packages

|Package|Key Feature|
|---|---|
|SciPy|ODE solver (stiff & non-stiff)|
|SymPy|Exact solutions for ODEs|
|JAX|differentiable ODEs|
|TensorFlow Probability ODE solvers|in ML models|
|TorchDiffEq|Neural ODEs in PyTorch|
|DifferentialEquations.jl Fastest|solvers via Julia|


# 6.4 I NTEGRATING ODE S WITH V ARIABLE T IME S TEPS

#  Python SciPy Packages

|Functions|When to Use|
|---|---|
|solve_ivp (fun, t_span, y0[, method, t_eval, ...]) Solve an|initial value problem for a system of ODEs|
|RK23 (fun, t0, y0, t_bound[, max_step, rtol, ...]) Explicit|Runge-Kutta method of order 3(2).|
|RK45 (fun, t0, y0, t_bound[, max_step, rtol, ...]) Explicit|Runge-Kutta method of order 5(4).|
|DOP853 (fun, t0, y0, t_bound[, max_step, ...]) Explicit|Runge-Kutta method of order 8.|
|Radau (fun, t0, y0, t_bound[, max_step, ...]) Implicit|Runge-Kutta method of Radau IIA family of|
|BDF (fun, t0, y0, t_bound[, max_step, rtol, ...]) Implicit|method based on backward-differentiation f|
|LSODA (fun, t0, y0, t_bound[, first_step, ...]) Adams/BDF|method with automatic stiffness detection|
|switching. OdeSolver (fun,t0, y0, t_bound, vectorized) Base class|for ODE solvers.|
|DenseOutput (t_old, t) Base class|for local interpolant over step made by|
|OdeSolution (ts, interpolants[, alt_segment]) Continuous|ODE solution.|


6.4 INTEGRATING ODES WITH VARIABLE TIME STEPS

##  Python SciPy functions

import numpy as np from scipy.integrateimport solve_ivp, odeint import matplotlib.pyplotas plt

def lotka_volterra(t, z, k1, k2, k3, k4): x, y = z # Unpack variables dxdt = k1 * x - k3 * x * y dydt = k4 * x * y - k2 * y return [dxdt, dydt]

# Parameters k1, k2, k3, k4 = 0.05, 0.10, 0.002, 0.002 # Initial conditions: x0 = 100 (prey), y0 = 200 (predators) y0 = [100, 200] # Time span t_span = (0, 600) t_eval = np.linspace(0, 600, 1000)

# Solve sol = solve_ivp(lotka_volterra, t_span, y0, args=(k1, k2, k3, k4), t_eval=t_eval)

# Plot plt.plot(sol.t, sol.y[0], label="Prey (x)") plt.plot(sol.t, sol.y[1], label="Predator (y)") plt.xlabel("Time") plt.ylabel("Population") plt.legend() plt.show()

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 6.5 PDE S AND THE M ETHOD OF L

#  Discretization

 To obtain an approximate, numerical solution to the continuous equations, we discretize continuous space into a large, but finite, number of grid points.

 A common approximation for advection at node midpoint of the slope defined by the neighboring nodes : q q q        

$$
(6.5) i i i x i x x q q U x q U                    2 1 1
$$

 Likewise, a reasonable approximation for the secondorder diffusion process is

$$
(6.6) i i i i i i i i i i x q q q D x q q q q D x q D                                    2 1 1 2 1 1 2 2 2 ) ( ) (
$$

# 6.5 PDE S AND THE M ETHOD OF L

#  Discretization

 In typical mass transport models, the processes that move mass (or energy and momentum) are additive in two or three dimensions.

 The above method of discretization is called central differencing because the scheme is centered around node currently being evaluated ( i in Eqs. 6.5 and 6.6).

 There are two broad families of discretization metho If time and space are both discretized, the classica difference or finite element methods based on solvi set of algebraic equations are used.

# 6.5 PDE S AND THE M ETHOD OF L

#  Method of Lines and ODEs

 Consider the flow of a contaminant in a river ( advection, molecular diffusion, and bioaccumulation i biotic components ( b ). A plausible model might be:

$$
    2 (6.7)
$$

$$
b v b kb b B b kb x p D x p U t p x x                       1 1 2
$$

$$
x B t    
$$

where the velocity in the x direction is and contaminant uptake ( k ) by biota decreases as the amount of the biota ( b ) increases to a maximum biomass.

6.5 PDES AND THE METHOD OF L

#  Method of Lines and ODEs

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 6.5 PDE S AND THE M ETHOD OF L

#  Method of Lines and ODEs

 Using i to index the nodes, the ODEs that must be solved at each node are

$$
x b b v B b kb t b B b kb x p p p D x p p U t p i i x i i i i i i x i                                      2 1 1 2 2 1 1 2 1 1 1 1 (6.8)
$$

# 6.5 PDE S AND THE M ETHOD OF L

#  Boundary Conditions

 Equations 6.8 will work well for grid nodes that ar the interior of the space being simulated. We must the boundary nodes differently because they do not have all the neighbors required by the equations.

 Four possible cases of boundary conditions:

- 1. The boundary is a true boundary (edges or corners).
- 2. Boundary of a grid embedded in a larger grid.
- 3. The grid may be embedded in a virtual grid in which boundary nodes are "fictitious“.
- 4. The topology need not conform to physical space.


 Two basic approaches to define edge nodes:

- 1. Force the values of the boundary nodes to specific (e.g., 0.0, but which may vary in time),
- 2. Set the fluxes into or out of the boundary nodes to specific magnitude (which may also vary in time).


# 6.5 PDE S AND THE M ETHOD OF L

#  Example Model of Butterfly Wing Patterns

$$
A 
$$

$$
0 2 5 2 0 1 3 1 0 2 5 0 1 3 0 2 2 2 0 2 5 2 4 0 1 3 2 1 2 1 0 1 3 1 2 1 1 1 k M P P k M P t P k M P k M P t P M D k M P k M k M P t M M D k M P k M k A t M k A t                           
$$

$$
t 
$$

Dilão and Sainhas, 2003

# 6.5 PDE S AND THE M ETHOD OF L

#  Example Model of Butterfly Wing Patterns

6.5 PDES AND THE METHOD OF L

#  Example Model of Rice Kernel Moisture Distribution

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 6.5 PDE S AND THE M ETHOD OF L

 Example Model of Rice Kernel Moisture Distribution

Original Images

Contrast Enhance

Simulated Results

0.5 hr

10

hr

20

hr

30

hr

55

hr

