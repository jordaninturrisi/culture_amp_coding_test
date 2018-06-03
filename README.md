# Culture Amp's Machine Learning Developer Coding Test

Your task is to build a simple CLI application that matches the text of user defined survey questions against a set of Reference Questions.


## Problem Statement

For the purposes of publishing **_Benchmark Reports_** from our aggregated survey data, we use a set of standard questions, known as **_Reference Questions_**. However, within each survey the actual question text may be slightly different. We need to be able to match each individual question to a standard **_Reference Question_** in order to collect aggregated results.


## Sample Data

Included in the folder `data` are three sample data files:
1. `reference_questions.csv` - Lists reference questions and unique codes used as identifiers
2. `labeled_data.csv` - test data consisting of example questions from real surveys together with the code representing the reference question they match to - this data can be used for training your application.
3. `test_questions.txt` - test data to use to run your application with.

__Note__: The `reference_questions` and `labeled_data` files use `"|"` as the field delimiter.


## The Application

Your coding challenge is to design and build the matching algorithm that will accept the text of any question and output the closest matching **_Reference Question_**. The application should be a simple CLI tool which allows the user to input any question text. It should output the two closest matching reference questions from the list in the attached CSV, with a relevance measure for each (an indicator of how well it matched). You are free to come up with a relevance measure, but provide a clear description of your selection.


## Other information

* Each **_Reference Question_** has a unique code, which you may use in the output to indicate which question is matched.
* We have also provided a set of test data, consisting of a number of example questions from real surveys, together with the **_Reference Question_** we would expect them to match. You can use this data to design and test your algorithm.
* Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate. Successful candidates will be asked to extend their implementation in a pair programming session as a component of the interview, so consider extensibility.
* Please include a `README` with any additional information you would like to include such as assumptions you made. You may wish to use it to explain any design decisions too.
* While we would like you to use this opportunity to show us what you can do, we also don't expect you to spend any longer than around 3-4 hours or build a large, complex application.
* If you have any questions or would like clarification on the requirements, please do email us.


## Submitting your solution

Assuming you use Git, when you're ready to submit your solution, please use `git bundle` to package up a copy of your repository (with complete commit history) as a single file and send it to us as an email attachment.

git bundle create culture-amp-coding-test.bundle master

We're looking forward to your innovative solutions!

Good luck!
