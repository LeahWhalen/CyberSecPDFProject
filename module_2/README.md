<h1>Anomaly Detection</h1>

<h3>Deps</h3>

* Python3 (3.6+ preferred)
* Conda (the dependencies are all saved to a .yml environment)

<h3>About</h3>
input: 
text files with pdf headers or decoded pdf's and headers. Text representation of pdf's.

output: 
1. graph of each pdf marking it as malicious and not malicious based on the contents
2. graph of all characters with malicious or not malicious

<h3>Usage</h3>
1. Change the directory to have the directory with all the test pdf's in it.
2. Run the jupyter notebook out of the conda environment

<h3>AI Algorithms Used</h3>
1. Lonely Forest: supervised learning
2. OCSVM: unsupervised learning