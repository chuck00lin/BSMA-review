# L ECTURE 3:

# Q UALITATIVE M ODEL F ORMULATION

# OUTLINE

3.1 How to Eat an Elephant

3.2 Forrester Diagrams

3.3 Examples

3.4 Errors in Forrester Diagrams

3.5 Advantages and Disadvantages of Forrester Diagrams

3.6 Principles of Qualitative Formulation

3.7 Model Simplification

3.8 Other Modeling Problems

# 3.1 H OW TO E AT AN E LEPHANT

 Qualitative model formulation is the conversion of objective statement and a set of hypotheses and assumptions into an informal, conceptual model.

 This form does not contain explicit equations, but i purpose is to provide enough detail and structure so that a consistent set of equations can be written

 Qualitative models can take any form (except mathematical), but diagrams are the usual representation. Three important diagrammatic schemes are:

- (1) Block structure diagram
- (2) Odum energy flow diagram
- (3) Forrester diagram


# 3.1 H OW TO E AT AN E LEPHANT

# Odum energy flow diagram

'Energese'

Energy Storage System

Jo

Xo

Energy

8

"Interaction"

"Source"

"Store'

Loss

"Source"

Qo

"Store"

2

Generic

"Consumption"

"Production"

~Self-Limiter"

"Transaction"

Flow

Passive electrical equivalent

HT Odum's System of Generic Symbols (Energy CircuitlSystems Language Symbols)

Resistor

Jo

9

RC

{Eagles]

Qo

Soil

Wcascls

Heat

Capacitor

Micc

Sun,

Plants

Rain

Acapted from H T Odum (1994) Fig 3-8, P 35

Bacteria

Source: http://en.wikipedia.org/wiki/Howard_T._Odum https://racerocks.ca/energy-diagrams/

An example of food chain

# 3.2 F ORRESTER D IAGRAMS

 Forrester diagrams are designed to represent any dynamic system in which a measurable quantity flows between system components.

 Forrester diagrams are such an abstraction of the basic concepts of system components material flows to obtain a general tool for qualitative modeling of systems.

# 3.2 F ORRESTER D IAGRAMS

#  A Simple Grass-Deer Ecosystem

tree

deer

COz

grass

# 3.2 F ORRESTER D IAGRAMS

 The internal objects that are modeled explicitly are called state variables and are those that, taken all together, characterize the condition or state of the system.

 The outside or external variables are either sources or sinks and are not modeled explicitly (i.e., no equations are written for these).

 Relations between system objects have two forms: (1) the direction and rates of flow between the quantity of interest and the objects and (2) the influences of a variable (e.g., the quantity of interest) on the rates of flow.

3.2 FORRESTER DIAGRAMS

#  The Basic Components of a Forrester Diagram

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 3.2 F ORRESTER D IAGRAMS

 Objects: They are the primary system components whose values over time we wish to predict.

 Material Flows: A flow is represented as a solid arrow and identifies the pathway over which the quantity interest (e.g., grams of carbon) flows.

 Information Flow or Influences: The second manifestation of relations between objects are the effects that the quantity of one object has on the of inputs to or outputs from another object (e.g., effects on growth rates).

# 3.2 F ORRESTER D IAGRAMS

 Sources and Sinks: Objects that are defined to be outside the system of interest, but which are inputs to stat or outputs from state variables.

 Parameters: Constants in equations.

 Rate Equations: Total (or absolute) rates of input to, or output from, a state variable are described mathemat with rate equations.

 Auxiliary Variables and Equations : Auxiliary variables are variables that are computed from an auxiliary equat

 Driving Variables: Dynamic events that relate to variables that are not state variables (e.g., season or temper some models) are often used as forcing functions.

# 3.3 E XAMPLES

 Forrester Diagram for the Grass-Deer Ecosystem Assumptions:

- 1. The per capita rate of growth of grass (g C produce per g C of existing grass) is constant. Therefore, t total growth will be the per capita rate times the total amount of C present.
- 2. The only loss to the quantity of C in the grass population is by deer consumption.
- 3. Deer compete with one another for grass so that, as the quantity of deer increases, each deer receives less C.
- 4. Deer excrete or respire a fixed proportion of their existing C as either atmospheric C or solid/liquid waste.


# 3.3 E XAMPLES

#  Forrester Diagram for the Grass-Deer Ecosystem

9c

2

3

for C flow; dolted arrows represent relations between levels and input or output rates as hypolhesized.  (Numbered ellipses on information flows are nat part of Forresler dlagrams, but are used lor explanatory purposes only)

# 3.3 E XAMPLES

 Population Growth with Explicit Birth and Death Density-Independent Model

$$
(3.1) dN bN N N t t t t     1
$$

N

{

Figure 3.4: Forrester diagram for one form of the density-independent population growth model.

# 3.3 E XAMPLES

 Population Growth with Explicit Birth and Death Density-Dependent Model

$$
(3.2) dN K N bN N N t R t t t t      ) (1 1
$$

1.0

N

N

R

k

N

Fduzllon

K

Feclor

R

Figure 3.5: Forrester diagram for one form of density-dependent population growth model.

# 3.3 E XAMPLES

#  Net Population Growth

(b)

(a)

N

Figure 3.6: Forrester diagrams for density-dependent (a) and density-independent (b) growth using the normal parameterization.

# 3.3 E XAMPLES

#  Multiple State Variables

 When a model has more than one state variable, then each object is represented by a box (level) that co with the others according to the flow of material ( defined by the relations (i.e., foraging relationshi

Figure 3.7: Forrester diagram showing multiple state variables; The set of three offset boxes represents three state variables all of which have the same relations (inputs and outputs) to other state variables in the system.

3.3 EXAMPLES

#  Multiple State Variables

A Hypothetical Agroecosystem Model

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 3.3 E XAMPLES

#  Multiple Flow Variables and Units

 When different units on flow variables are modeled (e.g., g N and g C), parallel models (or multiple models) must be used to avoid having "apples" flow into “oranges.”

 The dynamics of many biological processes depend on several interacting variables.

# 3.3 E XAMPLES

#  Multiple Flow Variables and Units

 Variables that are on the same level of organizatio may interact to affect some biological process negatively (negative feedback), positively (synergism), or independently (substitutable).

 If we wish to describe the dynamics of the affected process as influenced by the variables, then we must describe the dynamics of the individual variables and their effect on the process.

# 3.3 E XAMPLES



Multiple Flow Variables and Units

A Simple Model of Nerve Cell Activity

Na

Elactrical

Polontial

K

Figure 3.9: Forrester diagram when multiple flow variables are used.  Unlabeled material transfers are assumed to be losses or gains caused by ion pumping

# 3.3 E XAMPLES

#  Multiple Flow Variables and Units

A Simple Predator-Prey Model

Predalor

Figure 3.10: Simplified Forrester diagram for linked population models based on numbers of individuals.

# 3.4 E RRORS IN F ORRESTER D IAGRAMS

- 1. Using any symbols other than those defined in Fig. 3.2. For example, there is no symbol like a solid line with no arrowhead attached (Fig. 3.11a).
- 2. Failing to label all boxes, variables (auxiliary and driving), and parameters with names and units (where appropriate, Fig. 3.11a
- 3. Showing sources or sinks influencing rates (Fig. 3.11b).
- 4. Showing rates influencing state variables (Fig. 3.11c).
- 5. Showing information flows directly into state variables (Fig. 3.11a). State variables only change by a change in rates.
- 6. Showing material flows (solid arrows) between objec variables and sources and sinks (Fig. 3.11d).
- 7. Showing an influence on a quantity that cannot chan Fig. 3.11d).
- 8. Showing information flows between state variables (
- 9. Using incompatible units of flows or state variables (Fig. 3.11f).
- 10. Using state variables that are not in the model (objectives or equations) or not including state variables that are in the model.


# 3.4 E RRORS IN F ORRESTER D IAGRAMS

(a)

(b)

(d)

(c)

plant

insect

(e)

(f)

Figure 3.11: Examples of incorrect Forrester diagram fragments.

# 3.5 A DVANTAGES AND D ISADVANTAGES OF F ORRESTER D IAGRAM

#  Advantages

 Forrester diagrams help in learning the rudiments o the system objects.

 Understanding is more quickly attained, and constructive criticism is more readily achieved.

 Forrester diagrams can be a valuable aid in organizing the computer simulation program.

#  Disadvantages

 There is a point at which diagram complexity obfuscates the basic structure of the model and frustrates attempts to effectively communicate.

3.5 ADVANTAGES AND DISADVANTAGES OF FORRESTER DIAGRAM

##  Forrester diagrams - Computer simulation program

http://www.vensim.com/

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 3.5 A DVANTAGES AND D ISADVANTAGES OF F ORRESTER D IAGRAM

# 

# Forrester diagrams – Group practice Draw the Forrester diagram of Pan Water

# Pan Water Cycle

 What does this Model Represent?

This model represents a model of a pan filled with water. The water will eventually evaporate, at which point it will then condense on the lid of the pan and fall back into the water below. Models such as this can help to simulate the much larger pan of water that is our oceans, whose evaporation yields rain.

 What are the elements of this Model?

The water in this model is divided into three categories water in the pan, water in the air, and water on the cover of the pan. Water can transform between each of these categories through evaporation, condensation, and precipitation. The quantity of water in each area is displayed on the graph to the right.

#  How do I use this Model?

Set the parameters of the model to your liking to determine the rate at which water evaporates, leaks, condenses, and so on. Then, run the model and view your results on the right.

#  What should I expect?

In general, any setup should reach equilibrium at some point, when the water in the pan, in the air, and on the cover is relatively constant. However, the total water will continuously decrease due to leakage.

# 3.5 A DVANTAGES AND D ISADVANTAGES OF F ORRESTER D IAGRAM

 Forrester diagrams – Group practice Draw the Forrester diagram of Pan Water Cycle

# PAN WATER CYCLE

k 1

PAN-COVER-AIR Content over time

water on

cover

condelsation

100

100

100

100

water in

total

lprecipitation

air

water

water vapor leak

2

evaporation

water in

pan

water temperature

evaporation per degree

amount of

2

3

water in pan : Current

water in air : Current

water on cover : Current

total water : Current

4  3

6

Time (Minute)

8

7

10

# 3.6 P RINCIPLES OF Q UALITATIVE F

#  Key Steps in Qualitative Formulation

Identify the state variables (levels)

Identify the flows among the state variables

Identify the controls on the flow rates

Identify the auxiliary and driving variables

# 3.6 P RINCIPLES OF Q UALITATIVE F

#  Questions Need to be Answered:

What are the questions to be answered?

What quantities are needed to answer the questions?

What equations will answer the questions?

What other primary flow quantities are needed?

Is an explicit spatial representation required?

What are the controls on the flow rates between the

Do you know any parameter names?

# 3.7 M ODEL S IMPLIFICATION

# Eliminate State Variables

- • Convert a state variable into a constant or an aux
- • Aggregate state variables.


# Make "Stronger" Assumptions

- • Convert functions of state variables into constant
- • Convert nonlinear relationships into linear relati


# Remove Temporal Complexity

- • Convert random models into deterministic models.
- • Convert driving variables to constants.


# Remove Spatial Complexity

# 3.8 O THER M ODELING P ROBLEMS

#  Transport Models

 In transport models, we have a substance [energy (he or a quantity of matter] that flows from spatial po point.

 Conceptual rate equation:

$$
                                                        Distruction Pollutant Creation Pollutant Out Diffusion In Diffusion Out Advection In Advection t t p x ) , (
$$

 A compartment model paradigm and the Forrester diagram approach are not always appropriate for transport model when the system is modeled as spati continuous with small spatial resolution. Neverthel least in early model formulation stages, the compart model concept can be useful for transport models.

# 3.8 O THER M ODELING P ROBLEMS

#  Transport Models

(a)

(c)

(b)

Figure 3.12: (a) Flow between imaginary compartments in a continuous one-dimensional system. (b) Discrete system used in two-dimensional transport models . (b) A close-up of five points showing the similarity to compartment models. grid gríd

# 3.8 O THER M ODELING P ROBLEMS

#  Particle Models

 Particle models describe systems in which the variables are physical objects (e.g., billiard balls individual organisms) that change in some way according to dynamic equations. This is called the Lagrangian frame of reference, as opposed to the Eulerian approach of transport models.

 As with the transport model, Forrester diagrams can be useful for initial model formulation and detaili a subset of the objects and interactions. But it is useful to describe all of the objects this way.

3.8 OTHER MODELING PROBLEMS

#  Particle Models

BME 5113 Biological Systems Modeling and Analysis Department of Biomechatronics Engineering, National Taiwan University

# 3.8 O THER M ODELING P ROBLEMS

#  Finite State Models

(b)

(a)

time

B

3

GIIGBIGIIBBGBGI

state

3

(c)

Noxt

State

Flgure 3.14: A finite state weather model represented as a state transition graph (a) where the numbers represent the probabililies of the transitions denoted by arrows. (b) One stochastic realization of the showing the resulting dynamics of states. (c) A Forrester diagram ol the model graph

