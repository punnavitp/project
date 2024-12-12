<h1>Problem Statement</h1>
Biosignal analysis is often labor-intensive and time-consuming. Additionally, the collection of numerous signals in a home setting can be impractical, requiring complex and cumbersome device setups that are not portable.

<h1>Data Preparation</h1>
Before analyzing biosignals, they must be cleaned to remove noise and artifacts that could interfere with analysis. This cleanup is a crucial step in ensuring the data is suitable for further analysis.

<h1>Feature Extraction</h1>
Once the data is cleaned, experts identify key features or characteristics that are meaningful for sleep stage scoring. These features are chosen based on their relevance to sleep patterns and what is important for accurate classification.

<h1>Model Building</h1>
Machine learning models are trained using the extracted features to learn patterns and relationships that can be associated with different sleep stages (e.g., REM, NREM). Deep learning methods are applied to extract useful representations from the input data, transforming it in non-linear ways to facilitate classification tasks.

<h1>Sleep Stage Scoring</h1>
Sleep is classified into several stages, including:

<h3>NREM sleep, which is further divided into:</h3>
<h4>N1: The lightest sleep stage, with slow, rolling eye movements and reduced muscle activity.</h4>
<h4>N2: A deeper stage of sleep marked by regular brain waves and further decreased muscle activity.</h4>
<h4>N3: The deepest sleep stage, characterized by slow, delta waves and absence of muscle activity.</h4>
<h3>REM sleep:</h3> Involves rapid eye movements, increased brain activity, and muscle paralysis, believed to be important for memory consolidation and dreaming.
<h3>Awake:</h3> This stage occurs between sleep cycles and is characterized by the absence of the sleep stages N1-REM. It is typically brief.
The typical sleep pattern cycles through all NREM and REM stages multiple times during the night, with the first cycle being lighter and shorter than subsequent ones. REM periods become longer and deeper throughout the night.

Sleep stage scoring is treated as a multi-class classification problem with five stages to classify: N1, N2, N3, REM, and Awake.

<h1>Sleep Quality Metrics</h1>
To assess sleep quality, the following metrics are used:

<h3>Total Sleep Time (TST): The total minutes spent asleep.</h3>
<h3>Time in Bed (TIB): The total time spent in bed, including time spent awake.</h3>
<h3>Sleep Efficiency (%): The percentage of time in bed spent asleep.</h3>
<h1>Model Comparison</h1>
The two models used in sleep stage scoring are DeepSleepNet and TinySleepNet, with the following differences:

<table border="1">
  <thead>
    <tr>
      <th>Feature</th>
      <th>DeepSleepNet</th>
      <th>TinySleepNet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Representation Learning</td>
      <td>Two branches of CNNs</td>
      <td>Single branch of CNNs with hierarchical structure</td>
    </tr>
    <tr>
      <td>Sequence Learning</td>
      <td>Bidirectional RNNs</td>
      <td>Unidirectional RNNs</td>
    </tr>
    <tr>
      <td>Data Augmentation</td>
      <td>Signal augmentation</td>
      <td>Signal augmentation and sequence augmentation</td>
    </tr>
    <tr>
      <td>Computational Resources</td>
      <td>More</td>
      <td>Less</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>More</td>
      <td>Less</td>
    </tr>
    <tr>
      <td>Performance</td>
      <td>Similar</td>
      <td>Similar</td>
    </tr>
    <tr>
      <td>Deployment</td>
      <td>More challenging</td>
      <td>Easier</td>
    </tr>
  </tbody>
</table>

<h1>Evaluation</h1>
<h3></h3>The model evaluation includes:</h3>

<h3>Experimental Setup:</h3> k-fold cross-validation with non-overlapping patient splits.
<h3>Performance Metrics:</h3>
<h3>Overall:</h3> accuracy (ACC), macro-averaged F1-Score (MF1), Cohen’s Kappa (κ).
<h3>Per-class:</h3> precision (PR), recall (RE), F1-Score (F1).
<h3>Visualization:</h3> Hypnogram to display the sleep stages over time.
<h1>Conclusions</h1>
Deep learning is widely applied to supervised learning tasks in biosignal analysis, relying on labeled data to predict outcomes. An alternative approach involves transforming raw signals into spectrogram or image representations, which can be processed using CNNs that excel in image recognition tasks. However, end-to-end training using raw signals can be challenging, especially when signals have unclear patterns or insufficient training data.

Remote monitoring using deep learning is a promising avenue, as it involves adapting models developed in clinical settings to function with wearable devices.

<h2>Assignment<h2>
<a href="https://github.com/punnavitp/project/blob/main/brain.py">code</a>
