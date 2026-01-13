# Breast Cancer Wisconsin Dataset

**Source**: [Breast Cancer Wisconsin Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

**Description**: This dataset contains features computed from digitized images of fine needle aspirate (FNA) of breast masses, with $569$ total observations and $32$ variables. The features describe characteristics of the cell nuclei present in the image. The dataset was created by Dr. William H. Wolberg, W. Nick Street, and Olvi L. Mangasarian at the University of Wisconsin and donated in $1995$. The task is to identify whether a tumor diagnosis is malignant or benign.

**Variables**:

| Variable Name        | Type        | Description                                                                                  |
| -------------------- | ----------- | -------------------------------------------------------------------------------------------- |
| `id`                 | Categorical | Unique identifier for each sample                                                            |
| `diagnosis`          | Categorical | Diagnosis                                                                                    |
| `radius1`            | Continuous  | Mean of distances from center to points on the perimeter                                     |
| `texture1`           | Continuous  | Standard deviation of gray-scale values                                                      |
| `perimeter1`         | Continuous  | Mean perimeter                                                                               |
| `area1`              | Continuous  | Mean area                                                                                    |
| `smoothness1`        | Continuous  | Local variation in radius lengths                                                            |
| `compactness1`       | Continuous  | $\text{Perimeter}^2 / \text{area} - 1.0$                                                     |
| `concavity1`         | Continuous  | Severity of concave portions of the contour                                                  |
| `concave_points1`    | Continuous  | Number of concave portions of the contour                                                    |
| `symmetry1`          | Continuous  | Mean symmetry                                                                                |
| `fractal_dimension1` | Continuous  | "Coastline approximation" $- 1$                                                              |
| `radius2`            | Continuous  | Standard error of distances from center to points on the perimeter                           |
| `texture2`           | Continuous  | Standard error of gray-scale values                                                          |
| `perimeter2`         | Continuous  | Standard error of perimeter                                                                  |
| `area2`              | Continuous  | Standard error of area                                                                       |
| `smoothness2`        | Continuous  | Standard error of local variation in radius lengths                                          |
| `compactness2`       | Continuous  | Standard error of $\text{perimeter}^2 / \text{area} - 1.0$                                   |
| `concavity2`         | Continuous  | Standard error of severity of concave portions of the contour                                |
| `concave_points2`    | Continuous  | Standard error of number of concave portions of the contour                                  |
| `symmetry2`          | Continuous  | Standard error of symmetry                                                                   |
| `fractal_dimension2` | Continuous  | Standard error of "coastline approximation" $- 1$                                            |
| `radius3`            | Continuous  | Worst (mean of the three largest values) of distances from center to points on the perimeter |
| `texture3`           | Continuous  | Worst (mean of the three largest values) of gray-scale values                                |
| `perimeter3`         | Continuous  | Worst perimeter                                                                              |
| `area3`              | Continuous  | Worst area                                                                                   |
| `smoothness3`        | Continuous  | Worst local variation in radius lengths                                                      |
| `compactness3`       | Continuous  | Worst $\text{perimeter}^2 / \text{area} - 1.0$                                               |
| `concavity3`         | Continuous  | Worst severity of concave portions of the contour                                            |
| `concave_points3`    | Continuous  | Worst number of concave portions of the contour                                              |
| `symmetry3`          | Continuous  | Worst symmetry                                                                               |
| `fractal_dimension3` | Continuous  | Worst "coastline approximation" $- 1$                                                        |
