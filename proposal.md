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
  - **Labels**: Manually assigned to 31 classes (focusing on key species like Calanoid_1, Cyclopoid_1, Bosmina_1, etc.).
- **Challenges**:
  - Missing `.csv` data.
  - Erroneous image dimensions.
  - Class imbalance.

## 3. Methods and Tools
- **Tools**:
  - **Data Preprocessing**: Python (`Pandas`, `OpenCV`) for handling missing values and cleaning data.
  - **Modeling**: TensorFlow or PyTorch for classification tasks.
  - **Analysis**: R for exploratory data analysis and visualization.
- **Why these tools?**
  - They are well-suited for handling large image datasets and structured tabular data.
  - Provide robust libraries for machine learning and statistical analysis.

## 4. Preliminary Analysis
- **Summary Table**:
  - A table summarizing species distributions and highlighting data imbalances (to be included).
- **Visual Example**:
  - Include a sample image mosaic with annotations for zooplankton species.

## 5. Timeline
### Gantt Chart
| Phase                  | Duration   |
|------------------------|------------|
| Data Cleaning          | Week 1-2   |
| Exploratory Analysis   | Week 3-4   |
| Model Training         | Week 5-6   |
| Validation/Testing     | Week 7     |
| Report Writing         | Week 8     |

## 6. Expected Outcomes
- A reliable classification model for zooplankton species.
- Insights into the most important features for classification.
- Recommendations for addressing dataset challenges.

---

### Notes:
- This proposal is formatted based on the STA2453 project guidelines.
- Additional details like figures, sample data tables, and model outputs will be included in the final draft.

