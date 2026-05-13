- L ECTURE 8:
- M ODEL V ALIDATION


# OUTLINE

8.1 Insight and Illumination

8.2 Validation: When Models Go Bad

8.3 The Techniques of Validation

8.4 Model Discrimination

8.5 Meta-Models

8.6 Pr é cis on Validation

# 8.1 I NSIGHT AND I LLUMINATION

 Modeling, like computing and statistics, should produce insight , not merely numbers.

 Three general areas that help evaluate the meaning the number:

 Validity : Validation concerns the degree of our faith in th quality of the model with respect to the external w

 Uncertainty : Ignorance and uncertainty occur at many points in the modeling process: in the equations, the para and in the definition of the system itself.

 Behavior : The change of state variables over time is the lowest level of system understanding. To grasp fund interactions, we need to visualize the covariation b coupled variables, and identify system conditions i the dynamics of the variables are qualitatively sim

# 8.2 V ALIDATION : W HEN M ODELS

 The system scientists who use the word it to mean model quality with respect to the object of the modeling project.

 More recently, however, several authors have argued for using corroboration or confirmation

 The author thinks the adjective plausible accurately reflects the nature of tested biological models and the skeptical attitude we should adopt.

 Model quality, if it is quantifiable at all, is a con variable and perfection is probably not achievable.

 The process of model evaluation is unending.

# 8.2 V ALIDATION : W HEN M ODELS

 Important Criteria for Quality

 Usefulness for system control or management

 Understanding or insight provided

 Accuracy of predictions

 Simplicity or elegance

 Generality (number of systems subsumed by the model)

 Robustness (insensitivity to assumptions)

 Low cost of running or constructing the model.

 The model objectives will determine the weighting to be given to the different components.

# 8.2 V ALIDATION : W HEN M ODELS

 The Logic of Falsifying Complex Simulation Models

 An Aristotelian syllogism is a sequence of logical steps that in totality is true regardless of the tr falsity of the component steps.

 The basis of the modern concept of scientific falsification is a syllogism called modus tollens

Form :              Example :

B A 

B 

Spock does not act illogically. if Spock is human, then he will act illogically. (8.1)

----------

A 

Therefore, Spock is not human.

# 8.2 V ALIDATION : W HEN M ODELS

 The Logic of Falsifying Complex Simulation Models

 In applications of this argument in science, "A" is general hypothesis (law) and "B" is the implication prediction that follows from the law in a particula instance.

 The fallacy of affirming the consequent

Form :              Example :

B A 

B

Frodo is ill. if Frodo loses the ring, then he will be ill (8.2) .

----------

A

Therefore, Frodo has lost the ring.

# 8.2 V ALIDATION : W HEN M ODELS

 The Logic of Falsifying Complex Simulation Models

 Even though one observes many instances of the majo premise, this neither establishes it as a law nor pe one to infer the conditional (A) based solely on th observation of the prediction (B).

 Modus tollens is difficult to implement in mathematical models because the law ("A'' in Eq. 8.1) is actuall conjunction of a large number of separate assumptio

$$
) ( ) ( 3 2 1 3 2 1 n n a a a a B B a a a a              ⋯ ⋯
$$

 We can perform independent experiments to estimate parameters, perform parameter sensitivity analysis t evaluate their effects on model response, or create investigate alternative models.

# 8.2 V ALIDATION : W HEN M ODELS

#  The Geometry of Validation

 Mankin et al. (1977) considered validation in terms the relation of sets of measurements that can be ma on systems and models (Fig. 8.1).

P

M

Figure 8.1: Relations of sets of observations on the system (S) and model (M) for idation. is the set of correct predictions. (From Mankin et al. (1977), Fig. 1.@ 1977 Simulation Councils; Inc. Reprinted with permission Simulation Councils; publisher:) valInc ,

# 8.2 V ALIDATION : W HEN M ODELS

#  The Geometry of Validation

 There are several qualitative relations between the sets that help us understand different validation situations and ways that models can fail (Fig. 8.2)

(b)

(c)

(a)

M

M

M

(d)

(e)

M

M

Figure 8.2: Relations of model predictions and system observations.

# 8.2 V ALIDATION : W HEN M ODELS

#  The Geometry of Validation

 If Q is empty, there is no intersection between model and observation, and the model is useless nonempty, we say the model is useful .

 Mankin et al. (1977) also suggested that reliability is the ratio of the size of Q to the size of Model adequacy is the ratio of the size of of S .

# 8.2 V ALIDATION : W HEN M ODELS

#  The Geometry of Validation

 We must investigate both reliability and adequacy. published validation exercises focus on the size of at best, on model adequacy. Model reliability is inherently more difficult to evaluate.

 Error analysis and sensitivity analysis can provide insight into the true range of model predictions and, consequently, the size of M.

 To address model reliability, the model must be test in imaginative ways. For example, it should be teste against

 Different systems [e.g., different organisms, or ha (aquatic vs terrestrial)];

 Different geographical areas;

 Using different parameter values and environmental driving variables and perturbations.

# 8.2 V ALIDATION : W HEN M ODELS

#  Variables and Levels for Validation

 Usually, the model objectives will dictate which quantities should be compared between model and data. The most common are the dynamics of the state variables and derived measures in the form of Forrester auxiliary variables.

 The derived measures may be (1) functions of individual state variables [e.g., a state variable scaled to ot units], (2) the time or spatial averages or frequenc distributions of a state variable, (3) the maximum o state variable, or (4) the time that a state variabl achieves a particular value (e.g., its maximum).

# 8.2 V ALIDATION : W HEN M ODELS

 Variables and Levels for Validation

 In addition to choices of variables, there are degre comparisons.

 We seek objective, statistical criteria to compare m and data.

data

data

3

y

time

time

Figure 8.3: Comparisons between data (solid line) and the predictions of three hypotheti- cal models.

# 8.2 V ALIDATION : W HEN M ODELS

 Conditions for Validation

 Four attributes that will influence the kind of validation that is possible:

Data Independence

Single and Multiple responses

Single and Multiple Comparison Points

Unreplicated Systems and Models

# 8.2 V ALIDATION : W HEN M ODELS

 Conditions for Validation

 Data Independence

 The data used for model validation must be separate from and independent of any data used to formulate model hypotheses and estimate parameters.

# 8.2 V ALIDATION : W HEN M ODELS

 Conditions for Validation

 Single and Multiple Responses

 Our validation test procedure must decide how many and which of all possible responses will be used.

# 8.2 V ALIDATION : W HEN M ODELS

 Conditions for Validation

 Single and Multiple Comparison Points

 We can choose to validate the model either at a single point in time or at several points in time o the series.

 If we choose to evaluate the model at a particular point in time, then we must have a criterion for determining what the point will be.

 If multiple time points are used, then we must use care in applying standard statistical tests.

# 8.2 V ALIDATION : W HEN M ODELS

 Conditions for Validation

 Unreplicated Systems and Models

 Model validation using statistical tests requires some form of variability in either model prediction or observations.

 In real systems, variability is usually produced fro replicated observations. It can be produced in stochastic models from repeated runs that differ in the sequence of random numbers used to generate the modeled randomness.

# 8.3 THE TECHNIQUES OF VALIDATION

# 8.3 THE TECHNIQUES OF VALIDATION

# 8.3 T HE T ECHNIQUES OF V ALIDATION

#  Unreplicated Systems – Turing Tests

 The Turing test is a proposal for a test of a machine's ability to demonstrate intelligence.

 The "standard interpretation" of the Turing Test, in which player C, the interrogator, is tasked with trying to determine which player A or B is a computer and which is a human. The interrogator is limited to using the responses to written questions in order to make the determination.

A

8

8

2

 This approach can be used for biological models by asking experts to distinguish similarly prepared figures or reports of genuine and simulated system dynamics.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Methods for model validation:

Scatter Plots

The Correlation Coefficient

1:1 Regression

Test for Lack-of-Fit

Paired t-test

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Scatter plots:

10

10

10

8

8

8

6

6

6

4

2

2

2

10

10

10

6

4

2

2

Model

Model

Model

Figure 8.4: Three possible scenarios in which a model with poor fit to data results in a high correlation.   Solid circles are data-model and the dashed line is the regression of observations on model predictions.  The solid line is the 1:1 line for a perfect fit between data and model. Left: slope (variance) error; Middle: bias error; Right: bias and slope error. pairs

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Correlation coefficients:

 The correlation coefficient, r , measures the strength of the straight-line relation between model and data.

 While statistical analyses exist to test r correlation), there are no a priori non-zero values of against which to test.

 Sample Pearson correlation coefficient

$$
∑ ∑ ∑ 1 1
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 1:1 Regression:

 The F-statistic to test the slope = 1.0 and interce simultaneously:

$$
Y X i i s X b X a b na F         2 1) ( 1) ( 2 2 2 2 2 (8.2)
$$

$$
i i Y X n Y Y s      2 ˆ ) ( 2 2
$$

$$
i i i bX a X b X Y Y      ) ( ˆ
$$

Small values of F mean the model is a good fit. Thi statistic follows the F distribution with 2 and nof freedom.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Test for Lack-of-Fit:

 This statistic measures the degree that the model does not fit the observations.

 The model is validated if we do not reject the null hypothesis.

 This method requires replicated observations at every model prediction used in the test

 Error = Pure Error + Lack of Fit

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Paired t-test:

 An alternative to 1: 1 regression testing, is to tre model and data as paired samples and use a paired t-test to test H o :  X  Y = 0.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Type I Error and Type II Error:

 Type II error: failure to reject a false null hypothesis

 Type I error occurs when we reject a true null hypothesis.

 We can err if we rely on a single test or index.

 In large part, choosing which measure to rely on depends on the relative importance one gives to Type I or Type II errors.

8.3 THE TECHNIQUES OF VALIDATION

#  Unreplicated Systems – Observed vs Predicted Regression

 Type I Error & Type II Error:

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Observed vs Predicted Regression

 Important Assumptions of Linear Regression:

 The X i must be known exactly.

 The variance of the errors must be constant for all values of X i .

 The Y i are independent.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Indices

 Inequality coefficient (Theil’s U ) : Accurate models have small U .

$$
      2 2 2 1 1 ) ( 1 i i i i Y n X n Y X n U
$$

 Mean square error of predictions, MSEP:

$$
(8.3) 2 2 2 2 2 ) (1 ) ( ) ( ) ( 1 Y Y X i i S r rS S Y X Y X n MSEP         
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Indices

 MSEP is composed of three components associated wit

- 1. Differences between the model and system means (i.e., a nonzero intercept or bias error): MC,
- 2. Differences between the variance of model output and the variance of observations (i.e., slope-notunity error): SC,
- 3. The deviation of the correlation of model and observation values from 1.0 (i.e., random error): RC


$$
MSEP S r MSEP rS S MSEP Y X Y Y X 2 2 2 2 ) (1 ) ( ) ( 1          RC SC MC
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Indices

 A number of additional indices can be defined to fu quantify model. To a certain extent, these indices c thought of as measures of model adequacy.

 Mean absolute error, MAE:

$$
n X Y MAE i i   
$$

 Mean absolute percent error, MA%E:

$$
   i i i Y X Y n E MA 100 %
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Indices

 Two indices that scale the model error to the varia of the observed data are model efficiency Janus coefficient ( J 2 )

$$
        n i i m i i i Y Y X Y EF 1 2 1 2 ) ( ) ( 1
$$

$$
       n i i i m i i i n X Y m X Y J 1 2 ' ' 1 2 2 / ) ( / ) (
$$

where Y i ' and X i ’ are the data and model predictions, respectively, for the dataset used to create and parameterize the model, and where m sample sizes of the two comparisons.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

#  Unreplicated Systems – Indices

 Power (1993) defined model accuracy as suggests an F test of the hypothesis that accuracy equals 0 ( m and n g degrees of freedom, g =number of parameters).

 Power also calls the numerator of J 2 the model's predictive error and the denominator the model's replicative error.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Unreplicated Systems – Multiple Responses

 All previous methods presume a single response variable, but models with several state variables ar typical. One solution is to repeat the analyses for response independently. Alternatively, one can analy indices as the sum over all response variables:

$$
or       K k k s K k k S MSEP MSEP U K U 1 1 1
$$

$$
(8.4)
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

#  Replicated Systems or Models

 Replication in the system observations means that w have multiple, independent observations at points in time.

 Model replication means we have a stochastic model that has been run several times or a deterministic that is run several times with randomly selected parameter values.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models Boxplot

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Single Value

 If only a single value (e.g., the maximum of a state variable) is being tested, then standard statistical can be done (e.g., t -tests or ANOVA).

 If variability exists in only one component (e.g., t then we use a single-sample t -test ( H o : compares the mean of the replicated data with the single number of the unreplicated number (model prediction).

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 As with unreplicated situations, time series introduc autocorrelations.

 Measured values in real systems also tend to be correlated. These correlations can violate basic assumptions of standard statistical analyses so tha extreme care must be exercised in their application

 Single-factor repeated measures analyses designs or the multivariate profile analysis appropriate techniques for time series analysis.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Repeated Measures

 Single-factor repeated measures and split-plot desi types of analysis of variance (ANOVA).

 Single-factor repeated measures designs use a singl treatments applied sequentially to all of a single individuals (e.g., a sequence of drugs applied to p

 A split-plot design applied to repeated measures si generalizes this approach to include multiple facto not all individuals receive all treatments (e.g., d partitioned by chemical properties).

 A split-plot design partitions the error among a ma (e.g., system or location) and subdivides or splits these error components into effects associated with treatments.

 Both approaches assume that the correlation of resp among treatments is known and is constant over time

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Repeated Measures – Single-Factor Repeated Measures

Fador

5

10

144

15

15

210

1

10

10

1

Response data from &

repeated Mejsures

| |62|
|---|---|
|Time| |
| |2;2|


8.3 THE TECHNIQUES OF VALIDATION

#  Replicated Systems or Models – Time Series

##  Repeated Measures – Split-plot Design

Split-plot experimental design consisting of 3 replicates of two genotypes: transgenic and isoline. Ma split among 3 crops consisting of sweet corn, potatoes, and winter squash. Transgenic cultivars target in corn, Coleopterain potato and aphid-transmitted viruses in squash. (Hoheiseland Fleischer, 2007)

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis

 Profile analysis is a multivariate method that tests the hypothesis that the trajectories of data and model output are parallel.

 The approach does not make assumptions about the nature of the variance or covariance relationships of the variables, so it is a more gene approach to repeated measures problems.

 Profile analysis permits us to examine the relation the data and the model for several output variables (i.e., several state variables) simultaneously.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis

 For profile analysis, the null hypothesis tested is the difference between model and data is 0.0 for each and all time values of comparison. This is analogous to the paired t -test.

 Profile analysis calculates Hotelling's T which probability tables are available.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 Data and Null Hypothesis:

$$
0 2 2 1 1 : 0       ) m( ) d( ) m( ) d( ) m( ) d( k k H ⋯
$$

Table 8.2:  Hypothetical data and model response for six replicates and three points in time for phytoplankton (ug chl-alliter) and zooplankton biomass (uglliter) . Columns are time (1,2,3); rows are the replicates and the model prediction:

|Phytoplankton| | | |Zooplankton| | |
|---|---|---|---|---|---|---|
|Samnple| |2|3|1|2|3|
|1|2.5|4.0|1.0|10|50|20|
|2|2.0|3.9|1.3|15|60|18|
|3|2.3|3.8|0.9|12|55|22|
|4|1,9|4.1| |9|48|19|
|5|1,5|3.2|0.7|18|60|18|
|6|2.2|3.8|1.1|16|64|21|
|Model| |3.8|10|13|56|20|


# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 Prediction Deviation:

Table 8.3: Deviations of data and model response for six replicates and three points in time for phytoplankton and zooplankton biomass. Columns are time; rows are replicates.

|Phytoplankton| | | |Zooplankton| | |
|---|---|---|---|---|---|---|
|Sample|1|2|3|1|2|3|
| |0.4|0.2| |~3| | |
|2|~.1|0.1|0.3| | |2|
|3|0.2|0.0|4.1| | | |
| | | |03| | | |
| |0.1|0.0|0.1|3| | |


# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 Time Differences:

Table 8.4: and zooplankton responses. Columns are differences, rows are replicates. The dot in the shown in the last row.

|Sample|Apl'|~ Ap2'|~ 822|8z-2 ~|
|---|---|---|---|---|
|1 2 ; 6|0.2|0.2|3|6|
| |4.2|4.2| | |
| |0.2|0.1| | |
| | |93| | |
| |0.1|4.| | |
|Means| |~0.03|0.17|0.50|


# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 Table 8.4 is a one-sample multivariate test of the equality of means, and so is a generalization of the one-sample univariate test based on Student's

 The test in the general case is based on Hotelling' T 2 for which the general formula for data of this type is

$$
) ( )' )( ( 0 1 0 2 Y Y n T     Y S Y
$$

where Y Y 0 is a column vector of the average differences between observed ( Y ) and expected ( means, and S -1 is the inverse of the covariance matrix for the test variables

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 In this case, we are using the deviation of the mode from the data; thus, the expected mean is 0, so Hotelling's T 2 for model validation is:

$$
(8.5) Y S Y 1 2 ' ) (   n T
$$

 The variance-covariance matrix computed from Table 8.4 is

$$
                   42.7000 17.5000 1.1600 0.2600 17.5000 10.9667 0.3267 0.2933 1.1600 0.3267 0.0387 0.0067 0.2600 0.2933 0.0067 0.0747 S
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 Provided that sufficient replicates are available, t inverse of S can be obtained from standard software packages as the matrix in:

$$
  0.0463 0.50 0.17 0.03 0.03 2.64 2.22 61.47 5.94 2.22 2.03 50.36 4.28 61.47 50.36 1469.80 147.43 5.94 4.28 147.43 30.44 0.03,0.17,0.50 0.03, 6 2                                                   T
$$

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Profile Analysis – Example

 To determine the significance level of table of Upper Percentage Points of Hotelling's for T  ( p, v ), where p is q ( k 1) [i.e., 2(3 1) = 4], ( the probability level for the test, and 5). The values for our case corresponding to 0.01, 0.05, and 0.10 are

494 . 992 (4,5) 0.01  T

434 . 92 (4,5) 468 . 192 (4,5) 0.10 0.05   T T

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 Cross-correlation :

 Qualitatively, this procedure attempts to quantify the correlation between two autocorrelated time series for a given lag. The lag accounts for the autocorrelation.

# 8.3 T HE T ECHNIQUES OF V ALIDATION

 Replicated Systems or Models – Time Series

 95% Confidence Interval Method :

 One can simply plot model output and the data on th same graph and count the number of times the model output (or mean model output) falls within the data 95% confidence intervals. These intervals are

$$
X n s t X ] [ 1) (0.05,  
$$

 This criterion is a possible measure of model adequ

|Phytoplankton|Zooplankton|
|---|---|
|t1 : 1.17 _ 2.97|t1 ; 4.18 =|
|t2 : 2.99 - 5.97| |
| |t3 : 15.47 23.87 .|


# 8.4 M ODEL D ISCRIMINATION

#  General Description

 Model discrimination is an approach to content ourselves with deciding among a set of models based their relative adequacy .

 Calculating probabilities is central to model discrimination.

 There are two broad types of model discrimination: parametric and structural .

# 8.4 M ODEL D ISCRIMINATION

#  Likelihood Functions

 The likelihood of a sample is the probability that the sample would be drawn from a specified probability distribution with known parameters.

 A likelihood function that calculates the likelihoo sample is a mathematical function that results from applying a probability distribution to a particular in which one or more of the distribution parameters allowed to vary as the function's independent varia

# 8.4 M ODEL D ISCRIMINATION

 Likelihood Functions – Is the Die True?

 For example, suppose we roll the die five times and observe two occurrences of the number 3. How likely this outcome if the die is true?

 The underlying probability distribution for this ki problem is the binomial distribution:

$$
x n x x n x n b x n     ) (1 )! !( ! ) , ; (   
$$

 In the problem, however, we do not know the true we form the likelihood function:

$$
(8.6) 3 2 ) (1 2!(3)! 5 ! ]) , |[ (      x n L
$$

# 8.4 M ODEL D ISCRIMINATION

 Likelihood Functions – Is the Die True?

Lmax

0.3

1

0.2

0.1

0.2

0.4

0.6

0.8

1.0

Theta (0)

Figure 8.6: The likelihood function for the binomial probability distribution with n = 5 and x = 2. The maximum likelihood estimator is the 0 associated with maximum of the function.

 From this we see that the probability of a face app is associated with the maximum likelihood of the sa 0.4, not 0.1667, which we would expect if the die w So this discrepancy between expected and most likel suggests that the die is not true.

# 8.4 M ODEL D ISCRIMINATION

#  Likelihood Functions – Is the Die True?

 We quantify the amount of discrepancy by forming th likelihood ratio ( R ): L (  0.4 ) / L (  0.17 ). In this case, the ratio is 2.15. So we say that the observed sample i times as likely if  = 0.4 than if  = 0.167.

 A rule of thumb, Reilly (1970) states that if R is g than 10, then we consider the discrepancy is large enough to reject the hypothesis that the die is tru

# 8.4 M ODEL D ISCRIMINATION

 Likelihood Functions – Aside on Terminology?

 In informal presentations, one often sees the likeli function portrayed as:

L (data I hypothesis) or L (data I model)

 To compute L, we need not only the data 8.6), but also the value of  , another argument of the function. So, the more correct presentation would be

L (  I [model, data ]),

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

40

Model

Model 2

2

3

Modal 3

-1.290

5.318

7,049

19.886

30

y

Data

1

2

Model I:

20

Model 2

10

- Model 3:
- Model 4


y =

2

X

Figure 8.7: Four models fit to hypothetical data as a basis for discriminating among them: Model 1 is nested in Model 2 which is nested in Model 3.

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

 To compute the maximum likelihood for all four mode we need: (1) parameters to maximize, (2) some data, and (3) a probability distribution that depends on model parameters.

 We also need a probability distribution that will compute the probability of observing the data, given model.

 Each observed y value can be considered as being equal to a function plus an error term:

$$
(8.7) ij j i i x f y     ) , (
$$

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

 The probability of the total error is just what we by the probability of observing the y i . This, then, is the probability distribution we need for the likelihood the y . So, a general likelihood function is

$$
(8.8) model    n i i p L 1 ) , | ( /a0 ✂ /a0 
$$

✁

 The probability density function (pdf) for a single normal distribution is

$$
  (8.9)                    2 2 2 2 exp 2 1 ) , ; (      x n x
$$

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

 The particular likelihood function assuming normall distributed errors for all datum points (all y model j , and the independent data x needed by the model is 2

$$
 
$$

$$
  (8.10)                                2 2 2 1 2 2 2 2 2 ) , ( exp 2 1 2 ) , ( exp 2 1 ]) (), , | [ (        n i j i i n n i j i i i i i j x f y x f y x f y L
$$

 This equation has the following important propertie f( x i ,  j )) 2 =RSS (residual sum of squares) is the least-squared error between data and model. (2) Models and parame sets that have large errors (poor fits) have small values. (3) There is a single maximum, the maximum likelihood, which corresponds to the minimum of RSS set of (  j ,  2 ) associated with the maximum is the best set of model parameters for model i. These (  j ,  2 maximum likelihood estimator s of the parameters.

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

 To fairly compare and discriminate among a set of models, we want to use, for each model, the model's parameters that make the data the most likely, i.e., maximum likelihood estimates of  j and model. When we have these estimates, we will also have the maximum likelihood estimate RSS/n = MSEP. When MSEP is estimated, and substituted for 8.10, the maximum likelihood function for model

$$
/ 2 2 2 1 ( | [ , (), ]) exp( )                    (8.11) ˆ 2 2 n j i j i n L y f x          
$$

$$
2 2 ˆ ln( ( | [ , (), ])) ln( ) ln(2 ) (8.12) 2 2 2 j i j i n n n L y f x       
$$

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

 In the special case that the models are nested we c use the likelihood ratio test (LRT). Model A is nes (simpler than) Model B if the former can be obtaine from the latter by setting one or more parameters t zero.

 The likelihood ratio test is based on the ratio of likelihoods or, equivalently, the difference between log-likelihood of the simpler model (In( L complex model (ln( L c )). This quantity is with the null hypothesis that ln( L s ) = In( with degrees of freedom equal to the difference in number of parameters between the two models:

$$
)] ln( ) 2[ln( 2 c s L L    
$$

# 8.4 M ODEL D ISCRIMINATION

#  Empirical Model Likelihood

Table 8.5: Likelihood comparisons of four models on data in Fig. 8.7

|Model|RSS|ô2|In(L;)|In(Li) = In(Lmax=3)| |df|P|
|---|---|---|---|---|---|---|---|
|1|28.465|7.116|23.925|~1.603|3.206|2|0.201|
|2|22.473|5.618| |~1130|2.260| |0.133|
|3|12.773|3.193|~2.322|0.000| | | |
| |11.854|2.964| | | | | |


8.4 MODEL DISCRIMINATION

#  Mechanistic Model Discrimination

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 8.4 M ODEL D ISCRIMINATION

#  Mechanistic Model Discrimination

Table 8.6: Maximum likelihood values; ratios; and chi-square values for the seven models of Dursban movement. = 36. Not all models are nested in the best model (4a) df = degrees of freedom for the chi-square test = difference in number of parameters. P is the probability that a x? value as large or larger than observed would occur by random sampling. AIC is the Akaike Information Criterion tor each model; A; is the difference between a model's AIC and the smallest AIC in the set of models.

|Model|RSS| |In(Li)| | |df|P|AIC|Ai|
|---|---|---|---|---|---|---|---|---|---|
| |5374|149,3|~90.11|~81.34|162.7|4|0.001|188.22|154.7|
|2a|1964|54.56|~71.99|~63.22| | | |153,98|120.44|
|2b|848|23.56|-56.87|748.10|96,20|3|0.001|123,74|90.20|
|3a| |5.786|~31.60|~22.83|45.66| |0.001|75.20|41.66|
|3b|207.9|5.775| |~22.79| | | |77.12|43.56|
| |58.6|1.628|~8.772|0,00|0.00| | |33.54|0.000|
|4b| |2.206|~14.24|~5.,468| | | |42.48|8.940|


# 8.4 M ODEL D ISCRIMINATION

#  Information-based Discrimination

 More parameters often produce functions with more complicated structure (e.g., curvi-linearity, or many maxima and minima), which might be better able to match complicated, non-smooth data.

 However, all parameters are estimated with errors, an it often happens that the total error of the functi positively related to the number of parameters as t each contribute their individual errors. This is propagation and is discussed in Chapter 9.

 A number of schemes have been proposed to incorporate the number of parameters into the model discrimination process. All of these decrease model "quality" as the number of parameters increase.

# 8.4 M ODEL D ISCRIMINATION

#  Information-based Discrimination

 As Burnham and Anderson describe, if one model is considered the focal or "true" model, then a second model is viewed as approximating the first. The dis between the two is the information that is lost, if use the second model in lieu of the true model.

 Information theory provides a formula for the dista (the Kullback-Liebler distance) from a candidate mod to a focal model based on particular values of the parameters required by the two models.

# 8.4 M ODEL D ISCRIMINATION

 Information-based Discrimination AIC

 The Akaike Information Criterion (AIC) provides an unbiased approximation that can be applied to empir data based on the log-likelihood function. This approximation is computed for each model j:

$$
(8.13) K x f y L AIC j j 2 ])) (), , |[ ˆ ( 2ln( 2    
$$

where K is the number of parameters estimated in fitting the model to the data. K equals all the unknown coefficients in the model itself plus parameters of error distribution that must be specified. Thus, represents a penalty we incur by using complicated models to represent the data.

# 8.4 M ODEL D ISCRIMINATION

 Information-based Discrimination AIC

 When the models analyzed by AIC are nested, there is relationship between AIC and LRT:

$$
(8.14) k AIC AIC LRT j l 2   
$$

 Burnham and Anderson (1998) suggest, as a rough rule of thumb, that if  l  2 (  l = AIC l AIC min performs similarly to the best model and should not eliminated; if  l > 10, model I is not close in quality to the best model and can be eliminated.

# 8.4 M ODEL D ISCRIMINATION

#  Bayesian Inference

 The likelihood method quantitatively ranks the adequacy of a set of competing models by their abil to fit the data, but it does not actually compute th probability that the models are correct. One method calculating this probability uses Bayes' Theorem

# 8.4 M ODEL D ISCRIMINATION

#  Bayesian Inference

 The basis for this approach to inference is Bayes' Theorem which in the present context is a recipe fo calculating the probability that model is true, give observed data and a finite set of m alternative mod The Bayesian probability is

$$
(8.15)    m j j j i i i M P P M M P P M P M 1 ) | ( ) ( ) | ( ) ( ) | (
$$

✄

✄

✄

where m is the number of alternative models, P( the prior probability that model i is true, and P( the probability of observing Y values given that true. This latter quantity is typically estimated a maximum likelihood estimator of Y . The denominator is a scaling factor that normalizes the likelihood of particular model to the total likelihood of all the

# 8.4 M ODEL D ISCRIMINATION

#  Bayesian Inference

 Other users of Bayesian inference, however, recommend not using any previous experience. They suggest assigning the prior of each model an equal probability: 1/ m , where m is the number of models. Such priors are termed noninformative .

 The likelihood functions computed using the optimal of parameters to the data can be used as the P( Bayes' Theorem.

$$
(8.16)    m j j j j i i i i x y M L P M x y M L P M P M 1 2 2 ]) , , |[ ˆ ( ) ( ]) , , |[ ˆ ( ) ( ) | (   
$$

☎

# 8.4 M ODEL D ISCRIMINATION

#  Bayesian Inference

Table 8.7; Bayesian posterior probabilities of seven Dursban models.  Column 2 = probability of model i, column 3 Likelihood of model, column 4 = posterior probability of model i. (Recalculated from Blau and Neely (1975) and Carpenter (1990).) prior

|Model|P(M;)|Li|P(M; | Y)|
|---|---|---|---|
| |0.1429|1.049 x 10-40|4.716 x 10-36|
|2a|0.1429|7.763 x 10-3}|3.491 x 10-28|
|2b|0.1429|2.861 x 10-26|1.287 x 10-21|
|3a|0.1429|2.700 x 10-15|1.214 x 10-10|
|3b| |2.809 x 10-15|1.263 x 10-10|
|4a|0.1429|2.214 x 10-5|0.9958|
|4b|0.1429|9.344 X 10-8| |
|Denominator = 2.224 x 10-5| | | |


# 8.5 M ETA -M ODELS

 A meta-model is a nonlinear regression model of the of a dynamic model.

 The method developed by Kleijnen is as follows.

- 1. Use a series of original model runs to generate a d
- 2. Identify a set of potentially interesting relations linear or nonlinear functions to the model data set
- 3. Validate the meta-model by running the original mod second set of times with different input values (e. driving temperatures). If valid, the meta-model sho correctly predict the quantitative meta-relationshi new runs.


# 8.6 P RÉCIS ON V ALIDATION

 The relation of model validation and model discrimi has yet to be firmly established. They share import statistical similarities, and combined with carefull independent experiments.

 They represent different philosophies toward model evaluation.

 In practice, statistical validation emphasizes model adequacy; incorporating model complexity into our u assessments of model performance may be one approac measuring model reliability.

