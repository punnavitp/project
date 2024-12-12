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
