# L ECTURE 7:

# P ARAMETER E STIMATION

# OUTLINE

7.1 The Problem

7.2 Simple Linear Regression

7.3 Nonlinear Equations Linear in the Parameters

7.4 Equations with Nonlinear Parameters

7.5 Calibration to Dynamic Data

7.6 Evolutionary Techniques

7.7 Parameter Estimation Cautions

# 7.1 T HE P ROBLEM

 Every model that is used to make quantitative predictions contains parameters whose values must be specified.

 It is to be hoped that all of the parameters can be estimated in principle (i.e., have operational definitions), but even if this is true, performing the necessary experiments to estimate these values is often difficult in practice.

# 7.1 T HE P ROBLEM

#  A Model of Population Dynamics

5

4

3

2

20

40

60

80

Number of Females

100

|Females 1|Offspring 5|
|---|---|
|10|4.9|
|25|4.5|
|45|4.0|
|60|3.0|
|70|15|
|75|0.5|


Figure 7.1: Experimental results for number of offspring per female at different densities of females.

$$
3 2 1 k k x k y  
$$

 We wish to know the estimates of the parameters of our function that provide the best fit to the data.

# 7.1 T HE P ROBLEM

 Most concepts of best involve minimizing the distance between the data and the function, summed over all data points.

 Some plausible candidate measures of distance

- 1. Euclidean distance between function and data points
- 2. Square of vertical distance of data from the functi (the least squares criterion)
- 3. The chi-square: square of vertical distance divided the variance of the data. (the basis for the maximu likelihood estimates)
- 4. Absolute value of vertical distance.
- 5. Maximum distance of any one data point from the function as measured by one of the previous methods


# 7.1 T HE P ROBLEM

 We wish to find the parameter values that provide t " best " fit to a particular data set. The statistical mod we use is:

$$
i k i ij p x f y    ) , (
$$

 The standard definition of best is the least-square difference, which attempts to minimize the error ter

$$
           i i k i ij p x f y 2 2 )) , ( ( min min 
$$

 If we wish only to obtain a good fit with a functio passes through as many points as possible, then a cubic spline fit would be a good choice.

# 7.2 S IMPLE L INEAR R EGRESSION

 One of the simplest functions we can attempt to fit data is the linear function ( y = mx + b ), where slope and b is the intercept.

 Static Applications: The easiest case to which line regression applies is a simple experiment with a si independent variable. This is a classical applicati linear regression in which the slope and intercept the parameters of interest.

# 7.2 S IMPLE L INEAR R EGRESSION

#  Dynamic Applications

 The density-independent model is itself a linear equation with the slope equal to r .

$$
rN dt dN 
$$

 The density-dependent model: by dividing both sides by N we produce a new dependent variable 1 /N  dN/dt that is a linear function of N and has a negative slope.       N rN dN 1

$$
        K N rN dt dN 1
$$

N

N

rIK

{

;

N

Figure 7.2: Relation of per capita growth rate to the parameters and K in the densitydependent model.

# 7.2 S IMPLE L INEAR R EGRESSION

 Linear Regression on Transformed Equations

 Regardless of the source of the data for regression (i.e., from static experiments or dynamic data), often the relations are nonlinear. In these cases, we may be able to transform the equation to a linear form.

 Division by a variable : This method was shown above when we created the per capita growth rate by dividing both sides of the differential equation by N. The idea is to reduce a squared term to a linear one.

# 7.2 S IMPLE L INEAR R EGRESSION

 Linear Regression on Transformed Equations

 Logarithms : Power functions are expressions in which the parameter to be estimated is part of the power of a constant or independent variable. These equations can be made linear by a log transform. For example,

$$
(7.1) ) log( log log x b A y Ax y b   
$$

# 7.2 S IMPLE L INEAR R EGRESSION

 Linear Regression on Transformed Equations

 Inverses : Hyperbolic functions can be linearized by inverting the function. A famous example is the Michaelis-Menten relation for enzyme kinetics:

$$
(7.2) Ax y 
$$

$$
(7.3) x B 
$$

$$
A A x B y 1 1 1  
$$

1ly

V

1/V

max

max

1/x

Figure 7.3: Lineweaver-Burk plot to obtain the Michaelis-Menten parameters.

# 7.2 S IMPLE L INEAR R EGRESSION

#  Problems with Transformations

 The important linear regression assumptions to sati are error normality and homoscedasticity straightening a curved line does not ensure that th assumptions are satisfied.

 More advanced and better methods are commonly available in easy-to-use desktop computer statistic packages.

 Linear regression can estimate only two parameters. For example, the sigmoid curve and its linear transformation is A

$$
Cx B y A Be A y Cx            ) ln( 1 ln 1
$$

$$
(7.4)
$$

$$
 
$$

one of these must be assumed in order to estimate t other two.

# 7.2 S IMPLE L INEAR R EGRESSION

#  Problems with Transformations

 Inversion transformations can produce clustering of resulting transformed data; this can produce spurio statistical correlations between the variables.

 Inverse transformations turn small numbers into lar numbers. Often, the measurement of small quantities has large relative errors. These errors will be mag after transformation.

 Since the log of a number less than or equal to 0.0 undefined, logarithms can require that data be discarded or transformed prior to taking the logari

 To make the parameter values stated in their origin (untransformed) units requires that we "detransform the numbers (e.g., take the anti-log of the intercep Sometimes this detransformation will produce biased results.

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

 There are powerful analytical techniques for estima parameters in a special class of nonlinear function characterized by being linear in the parameters. Th that although the equation is nonlinear with respec independent variable, the parameter is not involved nonlinear expression.

 Some examples of equations that are nonlinear in th parameters are: ax

$$
b ax y bx a y x b ax y     ) exp(
$$

 If the equations are linear in the parameters, we ca several analytical techniques ( nonlinear or polynomial regression). If they are nonlinear, we must use iter techniques.

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

#  Multiple Linear Regression

 If the equation can be represented as a sum of terms, each of which is linear in the parameters (such as a polynomial equation), then linear regression can be used to estimate the parameters. For example, if the equation is:

$$
3 cx bx a y   
$$

we notice that if we consider x 3 to be a separate variable (call it w , for example), then the equation is linear, and any of several software packages that can perform multiple linear regression will estimate c .

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

#  Polynomial Regression

 The general model for the relation of an observed dependent variable to a function evaluated at various observed independent variable points is

$$
(7.5) i k i ij p x f y    ) , (
$$

 To implement the least-squares criterion, we wish to choose the p k in order to minimize the sum of squared errors (  i in Eq. 7.5) over all the observations. That is, we want the p

$$
(7.6) 2 2 ) ) , ( ( min min     i ij k i i y p x f 
$$

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

#  Polynomial Regression Derivation

Take the following function as an example:

$$
2 ) , ( i i k i Cx Bx A p x f   
$$

where the problem is to find A, B, and C that satisfy our minimization criterion.

$$
2 2 ) (       i i i i y Cx Bx A 
$$

$$
2 2 ) ) ((      i i i i i i y Cx Bx A g 
$$

after expanding,

$$
)] 2 ) 2 2 ( ) 2 2 2 [( 2 2 4 2 3 2 2 2 2 i i i i i i i i i i i i y y Cx x C Bx y BCx x B Ay ACx ABx A g            (
$$

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

#  Polynomial Regression Derivation

Recall from calculus that the minima and maxima of functions relative to a variable can be found by se the derivative of the function to 0. We wish to min g with respect to three "variables" ( A, B simultaneously.

$$
                                   i i i i i i i i i i i i i i i i i i i i i i i i i i i i i y x x C x B x A C g x y x C x B x A B g y x C x B A y Cx Bx A A g 2 4 3 2 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 ) 2 2 2 (2
$$

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

#  Polynomial Regression Derivation

The error function g will be minimized at those C that cause each of the above partial derivatives to be 0. Therefore, we set the partials to zero to get three equations in three unknowns:

$$
) ( ) ( ) ( 0 / 0 / 0 / 2 4 3 2 3 2 2                              C g y x x C x B x A B g x y x C x B x A A g y x C x B An i i i i i i i i i i i i i i i i i i i i i i i i
$$

# 7.3 N ONLINEAR E QUATIONS L INEAR IN THE P ARAMETERS

#  Polynomial Regression Derivation

Equations such as these can be easily solved once they are re-written in matrix notation:

$$
P S D                                                C B A x x x x x x x x n y x x y y i i i i i i i i i i i i i i i i i i i i i i i i 4 3 2 3 2 2 2
$$

Using matrix operations, we do this by premultiplying both sides of the equation by the inverse of S (denoted S -1 )

$$
P IP SP S S D 1 1     
$$

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

 Some equations are not linear in the parameters and cannot or should not be transformed. Iterative methods must be used to estimate their parameters.

 There are two major approaches for iterative method curvature-based and derivative-free .

 The general problem in parameter estimation is to f the minimum point (i.e., the combination of parameters that corresponds to minimum error).

 Iterative methods start at some arbitrary point in space and move from a parameter combination corresponding to large error to a combination with small error.

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

 The iterative algorithms move down the slope of the surface stopping only when the current parameter se is sufficiently close to the minimum.

(b)

(a)

Pz

Pz

P1

Figure 7.4: Error surface (a) and contour plot (b) for hypothetical fitting function in parameter space. minimum; but more complex error "landscapes" will have multiple local minima.

7.4 EQUATIONS WITH NONLINEAR PARAMETERS

###  Methods for Finding the Minimum of an Error Functio

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Gradient Methods

 For gradient methods, the direction of travel is bas the gradient of the slope, which is orthogonal to th previous direction that brought the current iterati the line minimum.

 Gradient iterative methods, as a class, calculate the and curvature of the surface at the current set of parameters using a Taylor approximation direction to change parameters on the direction of greatest change in the error surface.

 The gradient methods usually require either that th modeler provide the derivative of the function to b or that the derivatives be numerically approximated

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Four Important Gradient Methods

 Gauss This method truncates the Taylor series at the first-order terms. In other words, it approximates the surface solution point to a flat surface. This method requi composed of first-order derivatives be computed and

 Newton-Raphson This method is similar to Gauss' method, but approximates the surface to a quadratic function by Taylor series after the second-order terms . This requires that a complex matrix of firstand second-order derivative and inverted. It has an explicit step-size paramete

 Steepest Descent This is a simplification of the Newton-Raphson method. It eliminates the second-order derivatives inversion, but retains the step-size parameter.

 Levenberg-Marquardt (LM) This method combines steepest descent with second-order derivatives. It is one of the mos

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

 An Example of Two-parameter Fitting

 The basic idea is to iteratively change both parameters simultaneously:

$$
i i 1 i Δp p p (7.7)                                  i i i i i i p p p p p p 2, 1, 2, 1, 1 2, 1 1,
$$

 The problem is to compute a good value for LM method tries to use both the gradient (slope) of the error surface as well as its curvature to estim  p i .

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  An Example of Two-parameter Fitting

 In this two-dimensional case, the gradient is a vector with two elements, one for each parameter. The curvature is the slope of the slopes in all the directions. This Hessian, or curvature, matrix is

$$
(7.8)                          2 2 2 1 2 2 2 1 2 1 1 2 p p p p p p p p     C
$$

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

 An Example of Two-parameter Fitting

 For steepest descent method:

$$
(7.9) ε λ i     i 1 i p p
$$

where  is a constant that determines the size of the step to take.

 By using the relation that the product of the secon derivative of errors and a finite unit of parameter distance will be approximately the first derivative errors, the LM method can be formulated as:

$$
ε ε ε           1 i 1 i 1 C p p C Δp p C
$$

$$
(7.10)
$$

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  An Example of One-Dimension Search

Suppose the error surface was exactly a quadratic function:

$$
2 1 1 0.1 2 10 p p    
$$

The derivatives needed are:

$$
1 1 2 0.2 (7.11) d p dp    
$$

$$
2 '' 2 1 0.2                                               (7.12) d d p    
$$

1,0 If we use only steepest descent, arbitrarily choose 1, and start with initial guess p 20, Eq. 7.9 gives the para    meter value in next iteration as:

$$
1,1 20 (1)[ 2.0 (0.2)20] 18 p     
$$

whereas using curvature as defined in Eq. 7.10 gives:

$$
1,1 20 (1/ 0.2)[ 2.0 (0.2)20] 10 p     
$$

Using Eq. 7.1 1, we see that the minimum is exactly at p 10.

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  The Levenberg-Marquardt (LM) Method

function LM_Fitting %% create the first half of the data xdata = 0:.01:1; ydata = 3.0 ./(1.0+2.5*exp(4.65*xdata)) + randn(size(xdata))*.05; %% call |LSQNONLIN| init_guess = [3.5 2.3 4.9] parameter_hat = lsqnonlin(@mycurve, init_guess, [], [], [], xdata, ydata) %% plot the original data and fitted function plot(xdata,ydata,'b.') hold on fitted = parameter_hat(1) ./ (1.0 + parameter_hat(2) * exp( parameter_hat(3)*xdata) ); plot(xdata,fitted,'r') xlabel('x'); ylabel('y') legend('Data', 'Fit') %% function that reports the error function err = mycurve(parameter, real_x, real_y) fit = parameter(1) ./ (1.0 + parameter(2) * exp( parameter(3)*real_x) ); err = fit real_y; end end

7.4 EQUATIONS WITH NONLINEAR PARAMETERS

##  The Levenberg-Marquardt (LM) Method

A y





BeCx

1

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS



# The Levenberg-Marquardt (LM) Method

import numpy as np from scipy import optimize import matplotlib.pyplotas plt # let's generate x and y, and add some noise into y xdata = np.linspace(0.0, 1.0, 100, endpoint=True) ydata = 3.0/(1.0+2.5*np.exp(4.65*xdata)) + np.random.normal(loc=0.0, scale=0.05, size=xdata.size) # initial quess of the parameters (exact parameter is [3.0, 2.5, 4.65]) parameter = [2.9, 2.3, 4.9] # define the model function def model_func(xdata, a, b, c): y = a / (1.0 + b*np.exp(c*xdata)) return y # Nonlinear regression using the LM method with initial guess p0 parameter_hat, cov = optimize.curve_fit(model_func, xdata, ydata, method='lm', p0=parameter) #parameter_hat, cov = optimize.curve_fit(model_func, xdata, ydata, method='trf', bounds=([2.5, 2.0, 4.0 p0=parameter) # This line is for testing with another algorithm. See scipy.optimize.curve_fit. print('The fitted model function parameters are: ', parameter_hat[0], parameter_hat[1], parameter_hat[ # Calculate the fitted curve using the found parameters predict = model_func(xdata, parameter_hat[0], parameter_hat[1], parameter_hat[2]) # plot the original data and fitted function plt.plot(xdata, ydata, 'b.') plt.plot(xdata, predict, 'r') plt.xlabel('x') plt.ylabel('y') plt.legend(['data', 'fitted curve'], loc=1) plt.show() Python Code

7.4 EQUATIONS WITH NONLINEAR PARAMETERS

##  The Levenberg-Marquardt (LM) Method

A y





BeCx

1

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Direct Methods

 Because of the computational cost of numerically approximating derivatives and performing matrix inversion, direct methods are an attractive alternative.

 Direct methods do not require derivatives and choose the direction for the next move by directly evaluating the error surface in the neighborhood of the current point (Fig. 7.5b).

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Nelder-Mead Simplex Method

 This parameter estimation method is based on moving a geometric object (the simplex) through parameter space until the object encloses the best estimate.

 A simplex is a polygonal figure with one vertex mor than the dimensions of the space in which it is embedded.

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Nelder-Mead Simplex Method

Table 7.1: Fundamental operations on a simplex (see Fig.

|Reflection|Extend a line d units long from W to the midpoint of the B-0 and d units beyond. The end of the line 2d units is the trial vertex (W' ). edge long|
|---|---|
|Expansion|If W' is an improvement, continue the extension of the line another d units in the same direction to W"|
|Contraction|If reflection shows no improvement; extend a line d/2 units from W to the midpoint of the B-0 edge. Create a new vertex (W') at this long point.|
|Shrinkage|If none of the above; create two new vertices; one at the midpoint of the B-0 and the other at the midpoint of the B--W edge|


# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Nelder-Mead Simplex Method

CONTRACTION

di2

B

W

W

W'

SHRINKAGE

REFLECTION

EXPANSION

M

Figure 7.7: The four operations on the vertices of a two-dimensional simplex. W, 0, B = worst, intermediate; and best vertex; m midpoint of an See Table 7.1 for other definitions. edge

7.4 EQUATIONS WITH NONLINEAR PARAMETERS

#  Nelder-Mead Simplex Method

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Nelder-Mead Simplex Method Example

%% Optimal Fit of a Non-linear Function % First, create some sample data and plot it. t = (0:.1:2)'; y = [5.8955 3.5639 2.5173 1.9790 1.8990 1.3938 1.1359 1.0096 1.0343 ... 0.8435 0.6856 0.6100 0.5392 0.3946 0.3903 0.5474 0.3459 0.1370 ... 0.2211 0.1704 0.2636]'; plot(t,y,'ro'); hold on; h = plot(t,y,'b'); hold off; title('Input data'); ylim([0 6]) % y = C(1)*exp(-lambda(1)*t) + C(2)*exp(-lambda(2)*t) type fitfun start = [1;0]; % We use an anonymous function to pass additional parameters t, y, h to the % output function. outputFcn = @(x,optimvalues,state) fitoutputfun(x,optimvalues,state,t,y,h); options = optimset('OutputFcn',outputFcn,'TolX',0.1); estimated_lambda = fminsearch(@(x)fitfun(x,t,y),start,options) displayEndOfDemoMessage(mfilename)

# 7.4 E QUATIONS WITH N ONLINEAR P ARAMETERS

#  Nelder-Mead Simplex Method Example

function err = fitfun(lambda,t,y) %FITFUN Used by FITDEMO. % FITFUN(lambda,t,y) returns the error between the data and the values % computed by the current function of lambda. % % FITFUN assumes a function of the form % y = c(1)*exp(-lambda(1)*t) + ... + c(n)*exp(-lambda(n)*t) % with n linear parameters and n nonlinear parameters. A = zeros(length(t),length(lambda)); for j = 1:length(lambda) A(:,j) = exp(-lambda(j)*t); end c = A\y; z = A*c; err = norm(z-y);

7.4 EQUATIONS WITH NONLINEAR PARAMETERS

#  Nelder-Mead Simplex Method - Example

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 7.5 C ALIBRATION TO D YNAMIC D ATA

 Another approach to fitting parameters in a dynamic model is to find a set of parameters that minimize sum of errors between the dynamic model output (e.g numbers vs time) and similar observed dynamic trajectories over the entire time period simulated.

 There are two cases to consider:

- 1. The function to fit is an analytical solution to a differential equation.
- 2. The function to fit is the results of a simulation model.


# 7.5 C ALIBRATION TO D YNAMIC D ATA

 An Example of Density-Dependent Growth Model

$$
(7.13) rt K t N K N rN dt dN            ) ( 1
$$

$$
e  1
$$

where r is maximum per capita growth rate, capacity, and  is related to the starting population size [ N (0)]. We can estimate all three parameters by fitti function N ( t ) to experimental data consisting of population size over time. Obviously, N ( t ) is nonlinear in the parameters so we must use one of the techniques for nonlinear regression (transformation, gradient or di methods).

# 7.5 C ALIBRATION TO D YNAMIC D ATA

#  An Example of Linear System Model

$$
dy cx dt dy by ax dt dx    
$$

the dynamics [ x ( t ) and y ( t )] can be written as a sum of exponentials. In other words, we can find an solution whose parameters can be estimated using the methods described above. In this special case of sy linear differential equations, the parameter estimat problem is known as system identification .

 When a differential model can not be solved analytically, the calculation of derivatives needed some methods becomes complicated. Therefore, the direct method are effective on this problem.

# 7.6 E VOLUTIONARY T ECHNIQUES

 Parameter estimation is an optimization problem, and radically new approaches have been introduced recen based on analogies with the evolution of biological

 The new methods are members of a loose family of algorithms called evolutionary computation

 The basic idea applied to parameter estimation is t parameter space is searched by a large set of "orga that are defined by their position in the space. Th is the value of the error function at that point in space.

 Organisms with low fitness (large error) are discar Surviving organisms mate and produce slightly diffe offspring by combining the positions of the two par form a new location in parameter space. This proces repeated until organisms do not show further improv

# 7.7 P ARAMETER E STIMATION C AUTIONS

#  All Methods

- 1. Beware of transformations. Nonlinear regression or iterative methods are preferred.
- 2. Examine your data for obvious outliers. You may need to filter the data or apply some other method for eliminating extreme data points.
- 3. Beware of extrapolating beyond your data. Some situations in some methods can also make interpolating between datum points dangerous. Rational functions should not be used for data sets with multiple observations.


# 7.7 P ARAMETER E STIMATION C AUTIONS

#  All Methods

- 4. Beware of using a simple statistical index (e.g., to determine the function to use. An equation with sufficiently large numbers of parameters can be fit to match every little jog in a noisy data set with high r 2 , but may fail to reveal a simpler representation.
- 5. Use a graphics package to view your data and fitted curve. Be suspicious of any obvious departures. We wish to obtain a simple and general description of the observations. Simplicity in the form of equations with small numbers of parameters is usually preferable to complicated equations with a good fit to a particular dataset. The equation is t object of interest, not the r 2 .


# 7.7 P ARAMETER E STIMATION C AUTIONS

#  Iterative Methods

- 1. Non-evolutionary, iterative methods find only local minima. Use several starting points to search for the global minimum. The newer methods using evolutionary computation appear to be better at finding the global minima (or maxima).
- 2. Methods requiring derivatives can be slow and sensitive to the "roughness" of the error surface. Steep gradients and sudden reversals can cause numerical approximation of derivatives to go astray Methods such as simplex that do not use derivatives are less sensitive to this. Test the results with several step sizes.


# 7.7 P ARAMETER E STIMATION C AUTIONS

#  Iterative Methods

- 3. Most iterative methods do not give exact Approximate values can be obtained by strapping or by fitting a polynomial to the error function after a good fit is found.
- 4. Most iterative methods use two stopping criteria: one based on the relative change in the residuals and the other a ceiling on the number of iterations performed. After the algorithm has stopped, verify that sufficient iterations were allowed to ensure that the first criterion (not number of iterations) was used to stop the search.


