<H1>xPore: An AI-Powered App for Bioinformatician<h1>

<h1>Nanopore RNA Modification Detection</h1>

<h2>Problem Statement</h2>
<p>
Nanopore sequencing is a novel technology that can directly sequence RNA molecules. It measures raw electrical signal data at each nucleotide position along the RNA strand. This signal data contains information about RNA modifications, such as <code>m6A</code> methylation.
</p>
<p>The goal is to develop a computational method to accurately:</p>
<ul>
    <li>Locate modified positions.</li>
    <li>Quantify modification rates from nanopore data.</li>
</ul>

<h2>Data Collection and Preparation</h2>
<h3>Data Formats:</h3>
<ul>
    <li><strong>Raw Signal Data:</strong> Produced in <code>FAST5</code> format.</li>
    <li><strong>Basecalled Sequence Data:</strong> Output in <code>FASTQ</code> format.</li>
    <li><strong>Reference Genome:</strong> Provided in <code>FASTA</code> format.</li>
</ul>

<h3>Preprocessing Steps:</h3>
<ul>
    <li>Align raw sequencing data to the reference genome.</li>
    <li>Aggregate aligned data into event-level representations.</li>
    <li>Each event represents the raw signal for a k-mer in the original RNA sequence.</li>
</ul>

<h2>Modeling</h2>
<h3>Approach:</h3>
<p>
Bayesian multi-sample Gaussian Mixture Model (GMM):
</p>
<ul>
    <li>Models the distribution of electrical signal levels at each genomic position.</li>
    <li>Uses the Expectation Maximization (EM) algorithm to fit GMM parameters.</li>
</ul>

<h3>States Modeled:</h3>
<ul>
    <li>Mixture of 2 Gaussians:
        <ul>
            <li><strong>Unmodified State</strong></li>
            <li><strong>Modified State</strong></li>
        </ul>
    </li>
</ul>

<h3>Training:</h3>
<ul>
    <li>Performed on multiple samples simultaneously to improve statistical power.</li>
</ul>

<h2>Evaluation</h2>
<ul>
    <li>Achieved 86% AUC on a held-out test set for detecting known <code>m6A</code> modifications.</li>
    <li>Provides interpretable modification rate estimates that closely match expected levels.</li>
    <li>Performs well across various tissue types and cell lines.</li>
    <li>Enables discovery of differentially modified positions between conditions.</li>
</ul>

<h2>Future Work</h2>
<ul>
    <li>Explore potential improvements:
        <ul>
            <li>End-to-end modeling directly from raw signal data.</li>
            <li>Investigate alternative model architectures, such as deep autoencoders.</li>
            <li>Extend the model to detect additional RNA modification types beyond <code>m6A</code>.</li>
        </ul>
    </li>
</ul>

</body>
</html>


<h2>Assignment<h2>
<a href="https://colab.research.google.com/drive/1Y7ZdeJMQPba5KJRO_D_dNYsZzu0gJ9sx#scrollTo=nXJLGFO6XFTR">Colab</a>
