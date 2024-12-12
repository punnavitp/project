<h1>Problem Statement</h1>
Current techniques and tools for detecting code clones with multiple modifications (such as added, deleted, or modified statements) still face challenges. Additionally, existing clone detection and plagiarism detection tools are difficult to use due to being command-line based.

<h1>What are Code Clones?</h1>
Code clones refer to two or more code fragments that are similar enough to be considered duplicates. These can be classified into two primary types:

<h3>Syntactic Clones:</h3> These are identical or nearly identical code fragments, with differences mainly in layout, whitespace, and comments.
<h3>Functional Clones:</h3> These are code fragments that have the same functionality, but may differ in syntax or algorithmic structure.
Code clones can arise from various factors, including:

Copy-paste errors
Reusing code from other projects
Using code templates
Automated code generation
Modeling

<h1>Data Collection and Preparation:</h1>

<h1>Data Source: </h1> BigCloneBench, a large and reliable dataset of code clones.
Data Splitting: The dataset is split into training and testing sets using stratified sampling, ensuring balanced representation of different clone types.
<h3>Code Metrics Extraction:</h3>

<h1>Syntactic Metrics: </h1> 11 metrics are extracted, focusing on structural characteristics of the code, such as the number of tokens, identifiers, operators, differences in file and method names, return types, and lines of code.
Semantic Metrics: 12 features are obtained using code2vec, a neural model that represents code snippets as fixed-length vectors capturing their semantic meaning.
<h3>Machine Learning Models:</h3>

<h1>Models Considered: </h1> Decision Tree, Random Forest, and Support Vector Machine (SVM) with Sequential Minimal Optimization (SMO).
<h3>Key Points:</h3>

<h1>Data Quality: </h1> The model uses the reliable BigCloneBench dataset for training and evaluation.
<h3>Feature Engineering:</h3> Combines both syntactic and semantic metrics to capture different aspects of code similarity.
<h3>Model Exploration:</h3> Evaluates multiple machine learning models to find the best fit for detecting code clones.
<h1>Evaluation</h1>

Accuracy Evaluation:

<h3>BigCloneBench (BCB) Dataset:</h3> Precision, Recall, and F1-score were calculated for different clone types. The model achieved F1-scores ranging from 0.65 to 0.86.
<h3>Real Software Projects:</h3> The model was evaluated on three real-world projects (JUnit4, Natty, and Merry). Precision scores varied between 0.41 and 0.77.
<h3>Evaluation Involvement:</h3> Human experts were involved in evaluating the clone pairs.
<h3>Tool Adoption Evaluation:</h3>

<h3>Target Users:</h3> Computer Science students, programmers, and developers.
<h3>User Study Methodology:</h3> A between-subjects design, where participants were randomly assigned to either a command-line tool (Simian) or the Merry web-based tool.
<h3>Metrics:</h3> Likeliness of using the tool, ease of understanding, and ease of use.
<h1>Conclusions</h1>

<h3>Merry Tool:</h3> A web-based tool that uses machine learning for detecting code clones.
<h3>Goals:</h3> To improve accuracy and user experience compared to existing tools.

<h3>Merry Engine:</h3> Uses 4 machine learning models and shows good performance on the BigCloneBench dataset, although results on real-world projects vary.
<h3>Merry Web Application:</h3> Integrates with GitHub and provides a user-friendly interface for code clone detection.
<h3>Challenges and Limitations:</h3>

Currently supports only Java.
code2vec performance issues.
Evaluated performance might not reflect real-world project scenarios.
Concerns about database scalability.
Potential bias in user study due to small sample size.
<h1>Future Work</h1>

<h5>Expand the tool to detect clones in other programming languages.</h5>
<h5>Improve code2vec runtime performance.</h5>
<h5>Develop a dedicated machine learning model for each clone type.</h5>
<h5>Address MongoDB limitations by querying a part of the MongoDB document at a time.</h5>
<h5>Increase the number of participants in the user study to improve generalizability.</h5>
