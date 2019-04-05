# Assessment for Team-Based Project Work

## Assessment Key

* N = None
* I = Inadequate
* A = Adequate
* G = Good
* E = Excellent

## Technical Skills

### Software Development with Python

This section of the document contains the assessment categories related to
software development with Python. Every topic includes five levels of
competency that will be used to assess individuals in this class. A wide
variety of topics are included that all relate to software development
using Python. Among these topics are configuring a development environment,
using Python packages to aid in development, and applying best practices
when creating Python programs.

* Configuring a development environment for Python
  * N = Unable to setup development environment
  * I = Minimal development environment for Python
  * A = Basic development environment configured, including proper dependencies
    and development tools
  * G = Additional development tools configured, in addition to minimum required
    dependencies and tools
  * E = Additional development tools configured and is capable of assisting
    and troubleshooting other individuals development environment
* Running Python programs with `pyenv` and `pipenv`
  * N = `pyenv` and `pipenv` not installed
  * I = Unable to run programs with `pyenv` and `pipenv`
  * A = Able to run programs with `pyenv` and `pipenv`
  * G = Able to run programs with `pyenv` and `pipenv` using additional commands
    and flags as necessary
  * E = Able to run programs with `pyenv` and `pipenv` using additional commands
    and flags to streamline workflow, while providing assistance and
    troubleshooting to other individuals using `pyenv` and `pipenv`
* Linting Python programs with `pylint` and `flake8`
  * N = `pylint` and `flake8` not installed, setup, or used
  * I = Unable to run `pylint` and `flake8` to lint Python programs
  * A = Able to run `pylint` and `flake8` to lint Python programs but encounter
    some linting errors
  * G = Able to run `pylint` and `flake8` to lint Python programs and pass
    at least one check
  * E = Able to run `pylint` and `flake8` to lint Python programs and pass
    both checks
* Formatting Python programs with `black`
  * N = `black` not installed, setup, or used
  * E = Ran `black` successfully and file was formatted
    additional command line options if necessary
* Testing of Python programs with `pytest`
  * N = Did not use `pytest`
  * I = Created inadequate test cases
  * A = Created few test cases
  * G = Created thorough test cases
  * E = Created thorough and documented test cases
* Calculating code coverage of a `pytest` test suite
  * N = Did not check code coverage
  * E = Checked code coverage with `pytest`
* Reporting code coverage through an online provider
  * N = Did not check coverage
  * A = Checked code coverage using an online provider
  * E = Checked code coverage through an online provider and documentation provided
* Using docstrings to document a Python program
  * N = Did not use docstrings
  * I = Incorrectly use of docstrings which are unidentifiable to the compiler
  * A = Added docstrings, but they do not fully describe the functions'/methods'
    effect as a command
  * G = Successfully added docstrings with useful description, but they
    lack some proper syntax
  * E = Successfully added docstring with useful description and proper
    syntax
* Adopting and applying appropriate naming conventions
  * N = Used unconventional naming styles foreign to python's syntax
  * I = Used appropriate naming styles that are not entirely conventional
  * A = Used inappropriate naming styles that are not
    prescriptive or descriptive
  * G = Used appropriate naming styles, but is missing syntax used with
    variables, function, and methods
  * E = Used appropriate naming styles with correct syntax used with
    variables, functions, and methods
* Using exception handling to create a robust Python program
  * N = Code crashes because of no exception handling
  * I = Code crashes because of incorrect exception handling
  * A = Code does not handle few exceptions
  * G = Code handles most of exceptions
  * E = Code handles all exceptions and documents causes
* Refactoring a Python program to improve its characteristics
  * N = No refactoring done
  * I = Little code refactored and no documentation
  * A = Some code refactored and changes documented
  * G = Refactored code contains easy to understand functions and documentation
  * E = Refactored code is clean, efficient, well documented, and maintainable
* Debugging Python programs using logging and other methods
  * N = No bugfixing or bugfinding done
  * I = Identified bugs in code but did not provide any fixes
  * A = Fixed some identified bugs using logging/other methods
  * G = Fixed most identified bugs using logging/other methods
  * E = Fixed all bugs using logging/other methods and well documented
* Adopting and using appropriate Python language constructs
  * N = No written code or monolithic code
  * I = Language constructs used inappropriately
  * A = Some language constructs used appropriately
  * G = Most language constructs used efficiently
  * E = All language constructs used efficiently and reason is documented

### Project Management with GitHub

* Using the issue tracker
  * N = Issue tracker unused
  * I = Issue is raised but it is unclear or already exists
  * A = Issue is unique and has description for when issue occurs
  * G = Issue is unique, well described, and a possible reason for occurrence is
    mentioned
  * E = Issue is unique, well described, and a possible reason for occurrence
    and solution is mentioned
* Using the GitHub flow model
  * N = GitHub flow model unused or no commits
  * I = Pushed to master or non-descriptive commits
  * A = Pushed to correct repository with descriptive commits
  * G = Use of a branch/fork demonstrated appropriately
  (e.g having a feature branch) along with descriptive commits
  * E = Use of multiple useful branches/forks demonstrated appropriately
    containing multiple coherent and descriptive commits
* Creating and using a repository branch
  * N = Did not create or utilize branches
  * I = Create unclear branches
  * A = Create too many poorly named branches
  * G = Create useful adequately named branches
  * E = Create useful and descriptive branches
* Creating and using a repository fork
  * N = Did not create or utilize forks
  * I = Create unclear forks
  * A = Create too many poorly named forks
  * G = Create useful adequately named forks
  * E = Create useful and descriptive forks
* Merging a branch or a fork to another branch or fork
  * N = Not communicating changes before merging branches and forks
  * I = Merging with minimal communication or merging faulty code
  * A = Communicating changes with the team and reconciling differences
  * G = Merging branches after extensive communication
  * E = Merging branches with well-documented, detailed code and
    extensive communication
* Creating and reviewing a pull request
  * N = No PR made
  * I = Does not tag the related issues it is trying to close with poor description
  * A = Tags any related issues it is trying to close, describes
    proposed changes by a person
  * G = Tags any related issues it is trying to close, describes most proposed changes,
    discusses results of PR with Travis CI
  * E = Tags any related issues it is trying to close, fully describes all
    proposed changes and passes Travis CI
* Using appropriate commit messages
  * N = Commit messages are nonsensical
  * I = Commit messages are uninformative
  * A = Commit messages are sensible but not descriptive
  * G = Commit messages are both clear, and moderately descriptive
  * E = Commit messages are clear, concise and descriptive

### Continuous Integration with Travis

* Setup and configure Travis CI
  * N = Fails to perform any setup and configuration of Travis CI
  * I = Sets up and configures Travis CI which performs no checks
  * A = Sets up and configures Travis CI without performing checks on less
    relevant project deliverables
  * G = Sets up and configures Travis CI to perform checks on most relevant
    project deliverables
  * E = Correctly sets up and configures Travis CI to perform relevant
    checks for all project deliverables
* Perform secure releases of project deliverables
  * N = Does not utilize Travis CI when releasing project deliverables
  * I = Performs a release through Travis CI which is not secured
  * A = Performs a secure release through Travis CI while failing to sign
    commits
  * G = Performs a release through Travis CI with signed commits
  * E = Performs a release through Travis CI with signed commits
    and signed deliverables (e.g md5 hash)
* Create third-party integrations with Travis CI (e.g., codecov.io)
  * N = No incorporation of third party integrations
  * I = Third party integrations were only partially implemented
  * A = A few third party integrations were implemented
  * G = Most third party integrations were implemented
  * E = Many useful and relevant third party integrations were implemented
* Add README badges that show status of Travis CI builds
  * N = No addition of badges to the README
  * I = Badge added for Travis CI builds but does not work
  * A = A badge for Travis CI builds is in the README but is not in an
    appropriate location
  * G = A badge for Travis CI builds is in the README and is in an
    appropriate location but not in relation to any other status badges
  * E = A badge for Travis CI builds is in the README and is in an
    appropriate location in relation to any other status badges
* Add README badges that show characteristics (e.g., coverage and
  language)
  * N = No addition of status badges to the README
  * I = Relevant status badges added but do not work
  * A = A few status badges are in the README but are not in an
    appropriate location
  * G = Most relevant status badges are in the README and well located
  * E = All relevant and many useful status badges are in the README and well located

### Foundations of Software Engineering

* Requirements engineering
  * N = No effort to document, define, or maintain requirements present
  * I = Brief or unspecific documentation, definition, and maintenance given
  * A = Explains what requirements have been specified in enough detail
    to convey the most important information
  * G = Documentation and definitions are well written and gives other team members
    an informed idea of the process
  * E = The software engineer displayed highly detailed, elaborate, and complete
    documentation, definition, and maintenance in the given design process
* Software architecture
  * N = There is no consideration to the structure or organization of the project
  * I = There are small amounts of structure to the system
  * A = There is a blueprint for the software system that lacks completion
  * G = There is a completed blueprint for the software system
  * E = There is a completed detailed blueprint for all elements of the software
    system including detailed documentation
* Software design
  * N = No attempt to create a design
  * I = Initial steps are taken to conceptualize, frame, and design systems
  * A = Some software design is visible to the point where a software solution looks
    feasible
  * G = A software solution is created that includes both an algorithm design and
    a high-level architecture design
  * E = All goals and expectations of the design are met and compatibility, reliability,
    reusability, and scalability are included while a software solution is ultimately
    created that includes both an algorithm design and a high-level architecture
    design
* Software documentation
  * N = No explanation or comments about how to use or how the software works
  * I = A few comments in the code that are not detailed
  * A = Documentation has a bit of detail for every main part of the program
    and an overview of how to use the program
  * G = Documentation is detailed and visible for most of the software within the
    source code as well as possible constraints or additional details of the program
  * E = Explains in great detail how to use and operate the computer software,
    including reasoning and justification of why certain methods or approaches were
    taken
* Programming styles
  * N = Programming style is not specified
  * I = No clear programming style but has some structured style
  * A = At least one programming style used clearly
  * G = Most code conforms to predefined styles
  * E = All code conforms to predefined styles and well documented
* Managing software complexity
  * N = No complexity management techniques utilized
  * I = Code is frequently non-obvious and complex
  * A = Basic code management is used, such as code simplification or encapsulation
  * G = Most code is managed using code complexity management techniques such as
    continuous process
  * E = All code effectively utilizes many complexity reduction techniques such
    as modular design
* Mitigating software risk
  * N = No risk identified
  * I = Minimal risks identified
  * A = Some risks identified and basic risk mitigation techniques utilized
  * G = Most risk is identified and some risk mitigation techniques utilized
  * E = Extensive risk identification and mitigation techniques utilized

## Professional Skills

### Individual

* Continuous learning about
  * Python software development
    * N = A lack of new knowledge and/or contributions
      to any project
    * I = Incomplete knowledge or minimal contributions
      to projects
    * A = An average amount of knowledge and contributions
      to each project
    * G = An above average amount of knowledge and contributions
      to each project
    * E = Actively seeking to contribute and understand software development for
      each project
  * Project management with GitHub, specifically the Flow Model
    * N = A complete disregard for the model, especially multiple
      instances of pushing to the master branch
    * I = Occasional disregard for the model including at least one instance of
      pushing to the master branch
    * A = Almost always adhering to model and never pushing to
      the master branch
    * G = Making only minor mistakes while trying to follow the model
    * E = In addition to emerging as a leader who provides support to
      others who may be struggling with project management
  * Continuous integration with Travis CI
    * N = Travis CI not integrated
    * I = Integrated, but failing the majority of checks
    * E = Integrated, passing all checks
  * Foundations of software engineering practices
    * N = No effort demonstrated
    * I = Minimal effort demonstrated, little communication with others
    * A = Some effort and initiative demonstrated, participated in discussion
    * G = Moderate effort and initiative demonstrated, consistently
      participated in discussion
    * E = Significant effort and initiative demonstrated, actively fosters
      useful discussion
* Understanding and avoiding red flags like shallow modules,
  information leakage, and conjoined methods
  * N = Ignoring all red flags in the code
  * I = Identifying red flags in the code, but not fixing them
  * A = Identifying and fixing some red flags
  * G = Identifying, understanding and fixing most red flags
  * E = Identifying, understanding, and fixing all red flags with good documentation
* Understanding and adopting best practices
  * N = A severe lack of understanding and refusal to adopt best practices
  * I = Slight understanding and occasional use and identification of the
    best practices
  * A = An average amount of understanding and general identification and use of
    best practices
  * G = Above average demonstrations of understanding and the ability to find and
    utilize best practices
  * E = Full understanding of concepts, would also include the ability to determine
    which practices are better than others and then applying those practices

### Group

* Communication
  * N = Never checks appropriate slack channels and never communicates with
    teammates
  * I = Rarely checks appropriate slack channels and rarely communicates with
    teammates
  * A = Sometimes checks appropriate slack channels and sometimes communicates
    with teammates
  * G = Regularly checks appropriate slack channels and regularly communicates
    with teammates
  * E = Always checks appropriate slack channels and always communicates
    effectively with teammates
* Participation
  * N = Never participates in group conversation or activity
  * I = Rarely participates in group conversation or activity
  * A = Responds within 1-2 days to questions/comments
  * G = Responds within a day to questions/comments
  * E = Respond regularly and quickly to questions/comments, and willing to meet
    outside of class if necessary
* Decisions
  * N = Never participates in the decision making process
  * I = Rarely participates in the decision making process
  * A = Sometimes participates in the decision making process
  * G = Regularly participates in the decision making process
  * E = Always participates in the decision making process
* Postmortems
  * N = Never participates in postmortem discussions
  * I = Rarely participates in postmortem discussions
  * A = Sometimes participates in postmortem discussions
  * G = Regularly participates in postmortem discussions
  * E = Always participates in postmortem discussions
* Conflicts
  * N = Never addresses conflicts with teammates
  * I = Sometimes addresses conflicts with teammates
  * A = Addresses conflicts with teammates through communication
  * G = Addresses conflicts with teammates through mature communication while
    involving leaders
  * E = Addresses conflicts with teammates through mature communication while
    involving leaders and referencing conduct guide

### Interactions

* Interaction with the customer
  * N = Disrespects the customer and fails to consider any of their ideas
  * I = Respects customer but fails to value their needs
  * A = Respects customer and takes their needs into consideration
  * G = Respects customer, incorporates many of their ideas, and communicates
    difficulties
  * E = Respects customer, improves on their ideas, and engages in reasoned
    dialogue for further improvements
* Interaction with the team leaders
  * N = Impolite and impatient
  * I = Polite, impatient, and does not respond to team leaders
  * A = Polite, patient, responsive to team leaders but does not clearly
    communicates
  * G = Polite, patient, responsive to team leaders and clearly communicates
  * E = Polite, patient, responsive to team leaders, clearly communicates,
    and provides progress updates
* Interaction with the technical leads
  * N = Did not communicate with the technical leads
  * I = Communicated with the technical leads poorly or did not talk to them if needed
  * E = Communicated with the technical leads well

## Assessment and Conduct Guide

* Understanding the assessment form: [Assessment Sheet](https://github.com/Allegheny-Computer-Science-203-S2019/cs203-S2019-assessment)
  * N = Not reading the assessment form nor making contributions to it
  * I = Not reading the assessment form in its final state, but making minor
    contributions thus improving the initial state
  * A = A complete understanding of the assessment form and some contributions
    in order to enhance it
  * G = A complete understanding of the assessment form and multiple contributions
    to improve it
  * E = A complete understanding of the assessment form, major contributions, and
    continuing to improve it throughout the semester as needed
* Understanding the code of conduct: [Conduct Guide](https://github.com/Allegheny-Computer-Science-203-S2019/cs203-S2019-conduct)
  * N = Not reading the code of conduct nor making contributions to it
  * I = Not reading the code of conduct in its final state, but making minor
    contributions thus improving the initial state
  * A = A complete understanding of the code of conduct and some contributions
    in order to enhance it
  * G = A complete understanding of the code of conduct and multiple
    contributions to improve it
  * E = A complete understanding of the code of conduct, major contributions,
    and continuing to improve it throughout the semester as needed

### Revision of Guides

On request to change an element of either guide, unanimous consent among those
who abide by the guide is needed.
