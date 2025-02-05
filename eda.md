## 1. first question
- How many missed data are there?
### Visualizing
### transforming
### modeling data
- refine question / generate new question

## 2. second question
- What type of variation occurs within my variables? (from https://r4ds.hadley.nz/eda#questions)

First, let's explain what each features mean.
I groupped image features into three groups.

First group is Shape and Size Features.
Area..ABD. and Area..Filled.: Total area of the plankton, which gives an idea of its size. (Still need to find what ABD means)
Aspect.Ratio: Ratio of length to width, useful for differentiating elongated species from more rounded ones.
Width and Length: Important for distinguishing between wide vs. narrow plankton.
Volume..ABD., Volume..ESD.: Estimates of volume based on different methods, which are crucial for species that differ significantly in size. (Still need to find what ABD means)
Sphere.Volume, Biovolume..P..Spheroid., Biovolume..Sphere., Biovolume..Cylinder.: Different approximations of biovolume, helping to categorize species with different body structures. Also, be aware that Biovolume..P..Spheroid., Biovolume..Sphere., Biovolume..Cylinder. are in only 9 csvs. 

Second group is Structural and Shape Complexity Features
Symmetry: Indicates how symmetrical the organism is; some species are bilaterally symmetrical while others are irregular.
Circularity: Helps differentiate between round and elongated organisms.
Convexity: Measures how much the object shape deviates from a convex shape, useful for identifying complex body structures.

Third group is 어쩌구.

In first group, we found that Sphere.Volume is all 0. Therefore we will not using this column in the classification model. 
Also, 