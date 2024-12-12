<H1>xPore: An AI-Powered App for Bioinformatician<h1>

<h1>Problem Statement</h1>
Nanopore sequencing is an innovative technology that enables direct RNA molecule sequencing. It measures raw electrical signal data corresponding to each nucleotide position along the RNA strand. This signal data carries crucial information about RNA modifications, such as m6A methylation. The objective is to develop a computational method to precisely identify modified positions and quantify modification rates from the nanopore data.

<h1>Data Collection and Preparation</h1>
Nanopore sequencing generates raw signal data in the FAST5 format, while basecalled sequence data is provided in the FASTQ format. A reference genome is available in FASTA format. Data preprocessing involves aligning the sequences to the reference genome and aggregating the data into event-level representation, where each event corresponds to the raw signal for a k-mer in the RNA sequence.

<h1>Modeling</h1>
The approach employs a Bayesian multi-sample Gaussian mixture model (GMM) to characterize the distribution of electrical signal levels at each genomic position. The Expectation Maximization algorithm is utilized to estimate the GMM parameters. Each position is modeled as a mixture of two Gaussian distributions representing the unmodified and modified states. The model is trained across multiple samples simultaneously to enhance statistical robustness.

<h1>Evaluation</h1>
The model demonstrates an 86% AUC on a held-out test set for detecting known m6A modifications. It provides interpretable estimates of modification rates that align closely with expected values, performs consistently across diverse tissue types and cell lines, and facilitates the identification of differentially modified positions under varying conditions.

<h1>Future Work</h1>
Future directions include refining the method into an end-to-end model that processes raw signal data directly, exploring alternative model architectures such as deep autoencoders, and expanding the scope to detect other types of RNA modifications beyond m6A.


<h2>Assignment<h2>
<a href="https://colab.research.google.com/drive/1Y7ZdeJMQPba5KJRO_D_dNYsZzu0gJ9sx#scrollTo=nXJLGFO6XFTR">Colab</a>

<h1>TinySleepNet: Learning from Biosignal</h1>


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

<h3>NREM sleep, which is further divided into:<h3>
<h5>N1: The lightest sleep stage, with slow, rolling eye movements and reduced muscle activity.</h5>
<h5>N2: A deeper stage of sleep marked by regular brain waves and further decreased muscle activity.</h5>
<h5>N3: The deepest sleep stage, characterized by slow, delta waves and absence of muscle activity.</h5>
<h3>REM sleep:</h3> Involves rapid eye movements, increased brain activity, and muscle paralysis, believed to be important for memory consolidation and dreaming.
<h3>Awake:</h3> This stage occurs between sleep cycles and is characterized by the absence of the sleep stages N1-REM. It is typically brief.
The typical sleep pattern cycles through all NREM and REM stages multiple times during the night, with the first cycle being lighter and shorter than subsequent ones. REM periods become longer and deeper throughout the night.

Sleep stage scoring is treated as a multi-class classification problem with five stages to classify: N1, N2, N3, REM, and Awake.

<h1>Sleep Quality Metrics</h1>
To assess sleep quality, the following metrics are used:

<h3>Total Sleep Time (TST):</h3> The total minutes spent asleep.
<h3>Time in Bed (TIB):</h3> The total time spent in bed, including time spent awake.
<h3>Sleep Efficiency (%):</h3> The percentage of time in bed spent asleep.

<h1>Model Comparison</h1>
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

<h3>Experimental Setup:</h3> k-fold cross-validation with non-overlapping patient splits.

<h3>Performance Metrics:</h3>
Overall: accuracy (ACC), macro-averaged F1-Score (MF1), Cohen’s Kappa (κ).
Per-class: precision (PR), recall (RE), F1-Score (F1).
<h3>Visualization:</h3> Hypnogram to display the sleep stages over time.
  
<h1>Conclusions</h1>
Deep learning is widely applied to supervised learning tasks in biosignal analysis, relying on labeled data to predict outcomes. An alternative approach involves transforming raw signals into spectrogram or image representations, which can be processed using CNNs that excel in image recognition tasks. However, end-to-end training using raw signals can be challenging, especially when signals have unclear patterns or insufficient training data.

Remote monitoring using deep learning is a promising avenue, as it involves adapting models developed in clinical settings to function with wearable devices.
<h1>Assignment</h1>
<a href="https://github.com/punnavitp/project/commit/eef2dde028859b13fb213123d3c6cb4c7366093d">github</a>
