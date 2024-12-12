<h1>Data Acquisition</h1>
<h3>Surveys:</h3> Surveys were conducted with youth in the region to understand their interest in coding and AI education, their skills and knowledge in these fields, and their career aspirations.
<h3>Focus Groups:</h3> Focus group discussions were held with youth, educators, and industry experts to collect feedback on the project and its objectives.
Ultrasound Screening Data:</h3> Ultrasound screenings are performed bi-annually for a group of youth in the region. The collected data is used to identify youth who may be at risk for specific health conditions.
<h1>Data Preparation</h1>
<h3>Data Collection:</h3> Ultrasound images are gathered using a variety of tools, including portable ultrasound devices and telemedicine consultations. The images are securely stored in a database.
<h3>Data Cleaning:</h3> The images undergo cleaning processes, such as image segmentation and noise reduction, to ensure clarity and ease of interpretation.
<h3>Data Labeling:</h3> Expert radiologists label the images using a standardized classification system to categorize them as either normal or abnormal.
<h3>Data Augmentation:</h3> The dataset is expanded through techniques such as horizontal and vertical shifts, rotations, brightness modifications, shearing, and zooming, to enhance its size and diversity, which aids in improving the performance of machine learning models.
<h1>Model Development</h1>
<h3>Model Selection:</h3> The team chose the EfficientNetB5 model due to its proven success in a variety of tasks, including image classification. Additionally, the BiTNet model was selected because it is specifically designed for medical image classification.

<h3>Data Preparation:</h3> The data preparation process involved:

<h3>Data Collection:</h3> Ultrasound images were gathered from youth in northeastern Thailand every six months, with the goal of identifying individuals at risk for specific health conditions.
<h3>Data Cleaning:</h3> Background elements irrelevant to health condition identification were removed using image segmentation and noise reduction techniques.
<h3>Data Labeling:</h3> Radiologists labeled the images as either normal or abnormal based on their diagnoses.
<h3>Data Augmentation:</h3> The images were augmented with transformations like shifts, rotations, brightness adjustments, and zooming to increase dataset size and variability, improving the machine learning model’s effectiveness.
<h3>Model Training:</h3> The EfficientNetB5 model was trained through the following steps:

<h3>Pre-training:</h3> Initially, the model was pre-trained on the ImageNet dataset, which consists of over 14 million images across 1,000 different categories. The training utilized the Adam optimizer with a learning rate of 0.0001.
<h3>Fine-tuning:</h3> The model was then fine-tuned using the ultrasound dataset, again with the Adam optimizer and a learning rate of 0.0001, for 100 epochs.
<h1>Future Work</h1>
<h3>The First AI System to Screen for CCA Using Ultrasound:</h3> This groundbreaking development could significantly improve early detection and treatment of cholangiocarcinoma (CCA), a type of liver cancer.
<h3>Diagnosing 25 Abnormalities in the Upper Abdomen:</h3> This demonstrates that the AI models developed can potentially handle a broad spectrum of diagnostic tasks.
<h3>Implementation in Srinagarind Hospital and 205 Affiliated Hospitals:</h3> This indicates that the project has already made a meaningful impact on the healthcare system in Thailand.
<h3>Cloud-Based AI Services:</h3> By offering cloud-based AI solutions, the models developed are made more accessible to a broader range of users.
