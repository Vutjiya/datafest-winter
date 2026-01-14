# Breast Cancer Wisconsin Dataset

**Source**: [Breast Cancer Wisconsin Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

**Description**: This dataset contains features computed from digitized images of fine needle aspirate (FNA) of breast masses, with $569$ total observations and $32$ variables. The features describe characteristics of the cell nuclei present in the image. The dataset was created by Dr. William H. Wolberg, W. Nick Street, and Olvi L. Mangasarian at the University of Wisconsin and donated in $1995$. The task is to identify whether a tumor diagnosis is malignant or benign.

**Variables**:

| Variable Name             | Type        | Description                                                                                  |
| ------------------------- | ----------- | -------------------------------------------------------------------------------------------- |
| `id`                      | Categorical | Unique identifier for each sample                                                            |
| `diagnosis`               | Categorical | Diagnosis (M = malignant, B = benign)                                                        |
| `radius_mean`             | Continuous  | Mean of distances from center to points on the perimeter                                     |
| `texture_mean`            | Continuous  | Standard deviation of gray-scale values                                                      |
| `perimeter_mean`          | Continuous  | Mean perimeter                                                                               |
| `area_mean`               | Continuous  | Mean area                                                                                    |
| `smoothness_mean`         | Continuous  | Local variation in radius lengths                                                            |
| `compactness_mean`        | Continuous  | $\text{Perimeter}^2 / \text{area} - 1.0$                                                     |
| `concavity_mean`          | Continuous  | Severity of concave portions of the contour                                                  |
| `concave_points_mean`     | Continuous  | Number of concave portions of the contour                                                    |
| `symmetry_mean`           | Continuous  | Mean symmetry                                                                                |
| `fractal_dimension_mean`  | Continuous  | "Coastline approximation" $- 1$                                                              |
| `radius_se`               | Continuous  | Standard error of distances from center to points on the perimeter                           |
| `texture_se`              | Continuous  | Standard error of gray-scale values                                                          |
| `perimeter_se`            | Continuous  | Standard error of perimeter                                                                  |
| `area_se`                 | Continuous  | Standard error of area                                                                       |
| `smoothness_se`           | Continuous  | Standard error of local variation in radius lengths                                          |
| `compactness_se`          | Continuous  | Standard error of $\text{perimeter}^2 / \text{area} - 1.0$                                   |
| `concavity_se`            | Continuous  | Standard error of severity of concave portions of the contour                                |
| `concave_points_se`       | Continuous  | Standard error of number of concave portions of the contour                                  |
| `symmetry_se`             | Continuous  | Standard error of symmetry                                                                   |
| `fractal_dimension_se`    | Continuous  | Standard error of "coastline approximation" $- 1$                                            |
| `radius_worst`            | Continuous  | Worst (mean of the three largest values) of distances from center to points on the perimeter |
| `texture_worst`           | Continuous  | Worst (mean of the three largest values) of gray-scale values                                |
| `perimeter_worst`         | Continuous  | Worst perimeter                                                                              |
| `area_worst`              | Continuous  | Worst area                                                                                   |
| `smoothness_worst`        | Continuous  | Worst local variation in radius lengths                                                      |
| `compactness_worst`       | Continuous  | Worst $\text{perimeter}^2 / \text{area} - 1.0$                                               |
| `concavity_worst`         | Continuous  | Worst severity of concave portions of the contour                                            |
| `concave_points_worst`    | Continuous  | Worst number of concave portions of the contour                                              |
| `symmetry_worst`          | Continuous  | Worst symmetry                                                                               |
| `fractal_dimension_worst` | Continuous  | Worst "coastline approximation" $- 1$                                                        |