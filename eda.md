I mainly focused on three parts of the data.

First thing is relationship between features of images of plankton. For example, there are similar features so that I can group them. 
Grouping features based on their covariances can help to make model more efficiently. I can have enough reasons to remove redundant features or run PCA. 
Or I can derive new composite features. For example, this is not finalized version but maybe I can combine circulairtyu and convexity.
Also, if we use linear regression like logistic regression or SVM in further study, multicollinearity due to highly correlated value can hinder to interpret what feature is critical for classifying. 
Also in neural network like CNN, redundant information can cause weight redundancy since redundant features will learn same underlying pattern which will cause inefficient learning. Also redundant features can make model overly complex which will cause overfitting. 

Second thing is unbalanced label. Since in data explanation it says data is unbalanced and we have specific classes want to focus on, I'll discover how unbalanced are they. 

Third thing is variations and unusual values. 

Before I do EDA, I used SIMC_OverlapTiffsWithPP data. Also, for better understanding, I merged all data into one and proceeded EDA.
In here, notice that 9 files out of 252 files have three extra columns which are {'Biovolume..P..Spheroid.', 'Biovolume..Sphere.', 'Biovolume..Cylinder.'}, so I deleted them.

To catch relationship between features, I used heatmap of covariance. Before I use covariance, I grouped features into three based on my knowledge. Those are based on shape and size, structural and shape, and optical. This is the 
shape_and_size_cols = ["Area..ABD.", "Area..Filled.", "Width", "Length", "Volume..ABD.", "Volume..ESD.", "Sphere.Volume", "Diameter..ABD.", "Diameter..ESD.", "Feret.Angle.Max", "Feret.Angle.Min"]
structural_and_shape_cols = ["Symmetry", "Circularity", "Convexity", "Aspect.Ratio", "Compactness", "Elongation", "Fiber.Curl", "Fiber.Straightness", "Roughness"]
optical_cols = ["Transparency", "Sum.Intensity", "Intensity", "Sigma.Intensity", "Edge.Gradient"].

