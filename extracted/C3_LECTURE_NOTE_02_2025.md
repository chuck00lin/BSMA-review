# L ECTURE 2:

# T HE M ODELING P ROCESS

# OUTLINE

2.1 Models Are Problems

2.2 Two Alternative Approaches

2.3 An Example: Population Doubling Time

2.4 Model Objectives

# 2.1 M ODELS A RE P ROBLEMS

 The modeling process is a semi-formal set of rules that guides us to create a model.

 Four steps to solving mathematical problems (Polya, 1973)

- (1) Understand the problem (i.e., What is the question?)
- (2) Devise a plan for solving the problem (i.e., How do we solve it?)
- (3) Execute the plan (i.e., What is an answer?)
- (4) Check the correctness of the answer (i.e., Was it right?).


 Modeling is the hypothetico-deductive approach to science and vice versa.

## 2.2 TWO ALTERNATIVE APPROACHES

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 2.2 T WO A LTERNATIVE A PPROACHES

#  The Classical View

Objectives

Hypotheses

Mathematical Formulation

Verification

Calibration

Analysis and Evaluation

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Objectives

 The objective statement is a document that defines the reasons for producing the model in the first place.

 The objective statement answers the following questions:

 What is the system to be modeled?

 What are the major questions to be addressed by the (How will the model be applied?)

 What is the stopping rule for the modeling activity? (How good must the model be? To what will it be compared?)

 How will the model output be analyzed, summarized,

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Hypotheses

 The second stage is to translate the objectives and current knowledge of the system into a list of specific hypotheses.

 The hypotheses can be qualitatively stated or can be used with more quantitative relationships.

 At the stage of making hypotheses, the modeler must be cognizant of the fundamental uses of the model articulated in the objectives: understanding, prediction, or control.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Mathematical Formulation

 Qualitative hypotheses must be converted into specific, quantitative relations that can be formulated with mathematical equations.

 In this stage, the actual equations are defined.

 This step uses the initial physical, chemical, and biological information available for model construction to derive and check the correctness of the equations we hope to describe the dynamic behavior of system objects.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Verification

 Verification stage is a set of activities in which equations are translated into computer code. At this stage, it is necessary to verify that the computer algorithms and code are correct for the mathematical relationships defined.

 The choice of algorithm is important and can influence the predictions of the model.

 In writing a computer program to solve the equations, it is a nontrivial exercise to demonstrat that the computer output is correct.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Calibration

 Calibration is the set of activities by which numer values for the initial conditions (e.g., the startin number of species on an island) and constants in th equations must be specified.

 The basic problem involved is parameter estimation

 Calibration involves defining relations between observed quantities and the parameters so that statistical methods (e.g., linear regression) can be applied to produce the best estimates for the parameters. These relations may require that specif laboratory experiments be performed.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Analysis and Evaluation

 Once the model is calibrated, we can use it to produce the answer that our objectives specified.

 For numerical models, this involves running a computer program and recording the numbers produced.

 For analytical models, execution may range from simple computations to complicated mathematical argument and theorem proving.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Analysis and Evaluation

 If the model passes the validation criteria specifi in the objectives, the project, as defined by the objectives, is complete. If it fails, then errors wer made earlier in the modeling process and the hypotheses and/or mathematical formulations need to be revised. The entire process is repeated. Finally, depending on the objectives, further analyses of the model through computer simulation or mathematical analyses are performed.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Analysis and Evaluation

Define problem, Make simplifying assumptions, Review basic principles

Biological or Physical Problem

Mathematical Model

Perform mathematical manipulation

Mathematical Inferences

Conduct experiment

Observed Phenomena

Make mathematical checks, Review assumptions, Relate model to original problem

Development of Mathematical Models (Adapted from Nahikian)

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Problems with the Classical View

 The major problem with the classical approach is th independent data sets necessary for validation are often difficult or expensive to obtain. A modificat the classical approach, based on multiple hypotheses and models, avoids this problem.

 Multiple or alternative models are valuable for answering the question that whether the original model was unique in its accuracy or not.

 However, if we do create them in the sequential method illustrated by the classical view, we risk overfitting the model to the data.

2.2 TWO ALTERNATIVE APPROACHES

#  Problems with the Classical View

###  Overfitting

Noisy (roughly linear) data is fitted to both linear and polynomial functions. Although the polynomial function passes through each data point, and the linear function through few, the linear version is a better fit. If the regression curves were used to extrapolate the data, the overfit would do worse.

# 2.2 T WO A LTERNATIVE A PPROACHES

#  Problems with the Classical View

 Overfitting (for example in neural network training)

The red curve is the error on the validation set over several epochs. The blue curve is the error of the training set. When the error for the validation set increases while the training error steadily decreases then a problem of overfitting may occur (the learning is too specialized and does not generalized enough)

# 2.2 T WO A LTERNATIVE A PPROACHES

 Multiple Working Hypotheses

 An alternative to the sequential approach parallel approach that involves implementing and evaluating several different competing hypotheses and models simultaneously.

 In a multiple working hypotheses approach, every model is compared simultaneously (in parallel) to all of the validation data that are independent of data used to construct the model.

2.2 TWO ALTERNATIVE APPROACHES

##  Multiple Working Hypotheses

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 2.2 T WO A LTERNATIVE A PPROACHES

 Multiple Working Hypotheses

 An example of foraging behavior of ants

Foraging Behavior

Marnory Only

Phorcmone Trail

Random Walk

Memory'

Omniscient

Pheroticties

Figure 2.3: A family of competing hypotheses on the mechanisms used by ants to find seeds and recruit nest mates.

 The two extreme models, random and omniscient, bound the range of possible explanations.

 “A theory should be as simple as necessary, but no simpler.” Albert Einstein

 Occam’s Razor – Principle of Parsimony

# 2.3 A N E XAMPLE : P OPULATION D OUBLING

#  Objective:

Construct a description of the dynamics of the world's population such that the time when the population size is twice its starting value can be computed.

 Multiple Working Hypotheses Models:

 The first model assumes that per capita growth rate does not vary with increasing population size (density-independent growth)

 The second model assumes that the growth rate decreases linearly with population size (densitydependent growth).

# 2.3 A N E XAMPLE : P OPULATION D OUBLING

 Common Assumptions of the Two Models:

- 1. Per capita growth rate is not influenced by any extrinsic variable (e.g., ozone, UV radiation, temperature).
- 2. The sex ratio is 1: 1 (or we assume there is only a single sex).
- 3. There are no age differences among individuals (no age classes).
- 4. There are no geographical differences in growth rates (all countries and regions of the world are t same).


# 2.3 A N E XAMPLE : P OPULATION D OUBLING

 The Base Model in General Functional Form:

$$
(2.1) ) ( 1 t t t t N f N N N   
$$

 The Equations of the Second Model:

$$
(2.4) (2.3) (2.2) ] ) / ( [ ) ( ) ( 1 t t t t t t t t t t r K N r N N bN a f N N N f N N N         
$$

 The Equation of the First Model:

$$
(2.5) t t t rN N N    1
$$

# 2.3 A N E XAMPLE : P OPULATION D OUBLING

#  The First Model:

(b)

(a)

Ni+1

N

f() = rM

N

R

E

Time

Figure 2.4: (a) The ESR scheme and (b) a typical dynamic trajectory for densityindependent population growth using Eq. 2.5.

#  The Second Model:

(a)

(b)

N

f() = rM (1-MIK)

N

R

E

Time

Figure 2.5: (a) The ESR scheme and (b) a typical dynamic  trajectory for density- dependent population growth using Eq. 2.4.

# 2.3 A N E XAMPLE : P OPULATION D OUBLING

 With the two alternatives defined, we can analyze bo their properties, validity, and relative suitability objectives.

 Calibration of the Models:

$$
Second Model First Model t t t t t t t N K r r N N N N N N r        1 1
$$

 In the less mature disciplines such as ecology, espe where mechanisms are not understood, there is greate uncertainty, and the effects of using a particular s equations need to be investigated with alternative

# 2.4 M ODEL O BJECTIVES

 A careful statement of the objectives of a model is important because it defines the problem to be solved and can, therefore, be used to devise the implementation and analysis of the model.

 The objective statement can also define the domain of applicability of the model.

 Effective objectives are those that are stated as goals with purposes . For example, "Construct a model of photosynthesis [goal] to determine the effects of elevated UV light [purpose]."

# 2.4 M ODEL O BJECTIVES

 An objective statement must provide the following information :

- 1. The objective question (s).
- 2. The perturbations and stimuli accommodated in the model.
- 3. The exact system and environment which the model addresses.
- 4. The temporal and spatial scales over which the system is to be described.
- 5. The temporal and spatial scales of extrapolation and prediction .
- 6. The factual information and theoretical concepts in model construction (data, assumptions, sources, et
- 7. The criteria of validation (empirical and theoretical).


