- L ECTURE 1:
- M ODELS OF S YSTEMS THE M ODELING P ROCESS


# OUTLINE

1.1 Systems, Models, and Modeling

1.2 Uses of Scientific Models

1.3 Example: Island Biogeography

1.4 Classification of Models

1.5 Constraints on Model Structure

1.6 Some Terminology

1.7 Misuses of Models: The Dark Side

1.1 SYSTEMS, MODELS, AND MODELING

#  The famous parable of six blind man inspecting an elephant.

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 1.1 S YSTEMS , M ODELS , AND M ODELING

 A model is a description of a system

 A system is any collection of interrelated objects .

 An object is some elemental unit upon which observations can be made, but whose internal structure either does not exist or is ignored

 A description is a signal that can be decoded or interpreted by humans .

# 1.1 S YSTEMS , M ODELS , AND M ODELING

In short, systems are anything humans wish to discuss and models are one tool that facilitates the discussion.

SYSTEM

MODEL

# 1.2 U SES OF S CIENTIFIC M ODELS

 Model [er]: a device for turning assumptions into conclusions. Schimel (2002)

 Three primary, technical uses of models in science:

 Understanding – of either a real, physical system or of a system of logic such as another scientific theory.

 Prediction – of the future or of some state that is currently unknown.

 Control – to constrain or manipulate a system to produce a desirable condition.

# 1.2 U SES OF S CIENTIFIC M ODELS

 Conceptual framework of systems that defines the three uses of models Karplus (1983)

E

|Type ofProblem|Given|To Find|Uses of Models|
|---|---|---|---|
|Synthesis|Eand 8| |Understand|
|Analysis|Eand $|R|Predict|
|Instrumentation|S and R|E|Control|


Figure 1.1: Systems and the uses of models.  Top: general system represented as an input (E), a system object (S), and the output (R). Bottom: Knowledge needed for models of different uses. (From Karplus 1977, Fig: 1 1977 Simulation Councils, Inc. Reprinted withOUT permission Simulation Councils; Inc. , publisher:)

# 1.2 U SES OF S CIENTIFIC M ODELS

 Three general problems that human face with respect to any discipline or body of knowledge are:

 Synthesis – use knowledge of inputs and outputs to infer system characteristics.

 Analysis use knowledge of the parts and their stimuli to account for the observed responses.

 Instrumentation design a system such that a specified output is the result of an input.

# 1.2 U SES OF S CIENTIFIC M ODELS

 Secondary uses of scientific models that derive fro the social characteristics of science:

 Use as a conceptual framework for organizing or coordinating empirical research (e.g., designing experiments or sampling studies, allocating limited research dollars).

 Use as a mechanism to summarize or synthesize large quantities of data (e.g., a simple linear regression equation y = mx + b to reduce all of the to two parameters m and b ).

 Identify areas of ignorance, especially when definin relations between objects (e.g., Does species A eat species B).

 Provide "insight" to managers or planners (or other performing "what-if“ simulations ("gaming").

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

#  Physical Setting

40

8

30

20

10

300

70d

100

Days

Since Defaunation

Figure 1.2: Numbers of insect species on a small mangrove island following defaunation. (From Simberloff and Wilson 1970, Fig. 1. 1970 Ecological Society of America. Reprinted with permission of the publisher )

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

#  Theory

 The number of species is a balance of two processes: immigration and extinction.

 The rate of both processes depend on the number of species currently on the island.

 The net rate of change of species is the sum of these two “forces.”

Mainland

Species

A

Figure 1.3: Physical picture of island biogeography theory Organisms colonize randomly (arrows) . Islands can vary by their distance tothe mainland (near or far) and their size (large or small) .

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

#  Biological Hypotheses

 Individuals of each species have a constant probabi of arriving at the island and this probability is i for all individuals and all species. The rate of immigration ( I ) of new species only occurs upon t arrival of an individual of a species not currently island.

 The probability of extinction of any single species constant. Consequently, as the number of species on the island increases, the probability that any one species goes extinct increases. Thus, the total rate extinction (E) increases with R (number of species the island).

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

 Graphical Illustration of the Hypotheses

1

(# species)

R

1

Ex

E = (Er/P)R

R (# species)

Figure 1.4: Quantitative relationships between number of species on an island (R) and rates of immigration (I) and extinction (E). Pis the number of species in the mainland pool of species.

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

 Mathematical Expression of the Hypotheses

 Linear model

$$
P R E E I I I x x x ) / ( ) / (   
$$

$$
P R
$$

 Assemble into one recursive finite difference equation

$$
(1.1) t x t x x t t t t t P R E P R I I R E I R R ) / ( ) / ( 1        
$$

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

 A Classroom Physical Simulation of the Colonization Process

10

20

(a)

R

(b)

8

15

6

5

10

1

5

2

Madiloc

parametors

0

10

15

20

25

10

12

Iteration (time)

R

Figure 1.5: Data and results from a simulated biogeographical experiment. (a) Immigrashown are Extinction rate (E, numbersltime; open circles) and its regression line (dashed line). (b) Observed and predicted number of species by iterating Eq: 1.2 using two estimates of parameters.

# 1.3 E XAMPLE : I SLAND B IOGEOGRAPHY

 A Classroom Physical Simulation of the Colonization Process

 Equation based on regression

$$
)     (1.2) t t t t R R R R (0.0656) 0.011 ( ) 0.359 (8.963 1       
$$

 Computing the equilibrium state

$$
P R E P R I I x x x ˆ ) / ( ˆ ) / ( 0   
$$

 Mechanism (Fig. 1.5a) vs. observable dynamics (Fig. 1.5b)

# 1.4 C LASSIFICATIONS OF M ODELS

#  Forms of Models

- 1. Conceptual or Verbal descriptions in a natural language.
- 2. Diagrammatic graphical representations of the objects and relations (e.g., ecological "box-andarrow" diagrams of energy flow, physiological diagrams of metabolic pathways such as the Krebs cycle).
- 3. Physical a real, physical mock-up of a real system or object (either larger or smaller: a "tinker-toy' model of DNA or a scale model of an airplane for a wind tunnel).
- 4. Formal mathematical (usually using algebraic or differential equations).


# 1.4 C LASSIFICATIONS OF M ODELS

#  Mathematical Classification

1. Does the mathematics have an explicit representatio processes?

YES: Process-oriented or mechanistic models (e.g., h models using Newtonian physics and chemistry).

NO: Descriptive or phenomenological models (e.g., t biogeography model).

2. Does the mathematics have an explicit representatio system states or conditions?

YES: Dynamic models (e.g., island biogeography model

NO: Static models (e.g., linear regression equation x and y).

3. Does the mathematics represent time continuously?

# 1.4 C LASSIFICATIONS OF M ODELS

#  Mathematical Classification

4. Does the mathematics have an explicit representatio

YES: Spatially heterogeneous models (e.g., objects h space, or occupy a finite region of space).

- a) Discrete: space is represented as cells or block is represented as spatially homogeneous.
- b) Continuous: every point in space is different (e equations in physics).


NO: Spatially homogeneous models (e.g., simple equa population dynamics or enzyme kinetics).

5. Does the model allow random events?

# 1.4 C LASSIFICATIONS OF M ODELS

 Mathematical Classification

 Example:

The model of island biogeography (Eq. 1.1) is a deterministic, spatially homogeneous, discrete time, descriptive, dynamic model.

# 1.4 C LASSIFICATIONS OF M ODELS

 System Concept Classification

- 1. Compartment model differential or finite difference equations .
- 2. Transport model partial differential equations.
- 3. Particle model – fate of individual particles moving in space or individual organisms changing their condition.
- 4. Finite state automata represent an object as being in only a few, finite number of states or conditions.


# 1.5 C ONSTRAINTS ON M ODEL S TRUCTURE

 Realism: the degree to which model structure mimics the real world. In formal models that are realistic, the equ correct, not just the model output. In physical mod scale airplane) maximal physical detail is present

 Precision: the accuracy of the model predictions (output). In precise models, the air flow around the scale model same as that around the fullsize plane. Precision is in the statistical sense, which refers to the degre a set of measurements.

 Generality: the number of systems and situations to which the model correctly applies. In physical models, a gene airplane model applies to both a Piper Cub (small, aircraft) as well as a Boeing 747 (large, multipleaircraft).

# 1.6 SOME TERMINOLOGY

# 1.6 SOME TERMINOLOGY

# 1.7 M ISUSES OF M ODELS : T HE D

#  Motivations for modeling

EXPERIMENTATION

WITH CONTROL

PREDICTION

STRATEGIES

TESTING OF

FOR

THEORIES

ACTION

GAINING

PERFORMANCE

INSIGHT

PREDICTION

POLLUTION

PHYSIOLOGICAL

DESIGN

PROCESS

CONTAOL

ECOLOGICAL

HYDROLOGICAL

ECONOMIC

AIRCRAFT

DYNAMICS

CONTROL

SOCIAL

POLITICAL

ELECTRIC

CIRCUITS

BLACK

WHITE

BOX

BOX

(Karplus, 1983)

1.7 MISUSES OF MODELS: THE D

 “White box” vs. “Black box”

 Quantitative model vs. qualitative model

