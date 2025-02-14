# Automating Zooplankton Classification Using Geometric and Environmental Features

## 1. Introduction
- **Research Question**: Make machine learning model to classify zooplankton species based on their images and features like geometric environmental.
- **Significance**: Zooplankton are vital indicators of freshwater ecosystem health. Current manual classification is labor-intensive and prone to observer bias.

## 2. Data Description
- **Source**: Ministry of Natural Resources and Forestry, Ontario.
- **Structure**:
  - **Images**: `.tif` mosaics containing zooplankton images.
  - **Features**:
    - **Geometric**: Transparency, symmetry, compactness, etc.
    - **Environmental**: Latitude, longitude, depth, distance to shore.
  - **Response Variable**: Manually assigned to 31 classes in "Class" column (focusing on key species like Calanoid_1, Cyclopoid_1, Bosmina_1, etc.).
- **Challenges**:
  - Missing `.csv` data.
  - Erroneous image dimensions.
  - Class imbalance.

## 3. Methods and Tools
- **Tools**:
  - **Data Preprocessing**: `Pandas` library for handling missing values and cleaning data.
  - **Feature Extraction**: Rather than relying on raw pixel values, we’ll extract geometric and texture features from each cropped zooplankton image. This approach accounts for variations in plankton images due to rotation and different camera angles, making the model more robust to these changes.
- **Methods**:
  - **The following features will be used**:
    - **Geometric Features**: Area, Perimeter, Aspect Ratio, Compactness, Symmetry, Transparency.
    - **Texture Features**: Contrast, Homogeneity, Energy, Correlation.
  - **Modeling**: Multinomial Naive Bayes will be used as a baseline classifier. Since extracted features are categorical or frequency, MNB is well suited for this dataset. We will preprocess features using Min Max Scaling to ensure all values are positive.
  If MNB struggles, we can use CNN. Since there are imbalanced plankton species, MNB handles class prior by assigning probability based on frequency. 

## 4. Preliminary Analysis
- **Visual Example**:
  - The same species can have different shapes due to variations in camera angle, lighting, and positioning.
  - Below is an example of 22 images of Bosmina_1 plankton, showing the morphological differences within a single species.
  ![Bosmina_1 Example](test/image_grid.png)

## 5. Timeline
![Jira Board](timetable.png)