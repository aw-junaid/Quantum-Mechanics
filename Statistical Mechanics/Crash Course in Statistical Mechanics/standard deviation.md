The standard deviation is a measure of the amount of variation or dispersion in a set of values. It quantifies how much individual data points in a dataset deviate from the mean (average) of the dataset. A smaller standard deviation indicates that the data points tend to be close to the mean, while a larger standard deviation indicates that the data points are spread out over a wider range of values.

### Definition

For a dataset with \( n \) values $\( x_1, x_2, \ldots, x_n \)$ and mean $\( \bar{x} \)$, the standard deviation $\( \sigma \)$ is defined as:

$\[
\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}
\]$

where:
- $\( \bar{x} \)$ is the mean of the dataset:
  $\[
  \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
  \]$
- $\( x_i \)$ are the individual data points.
- \( n \) is the number of data points.

### Sample vs. Population Standard Deviation

- **Population Standard Deviation**: Used when the dataset includes the entire population. The formula divides by \( n \):
  $\[
  \sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}
  \]$

- **Sample Standard Deviation**: Used when the dataset is a sample of a larger population. The formula divides by \( n-1 \) (Bessel's correction) to correct for the bias in the estimation of the population variance:
  $\[
  s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
  \]$

where $\( s \)$ denotes the sample standard deviation.

### Properties

1. **Non-Negativity**:
   - Standard deviation is always non-negative because it is the square root of a non-negative value.

2. **Same Units as Data**:
   - Standard deviation is expressed in the same units as the data, making it interpretable in the context of the original measurements.

3. **Sensitivity to Outliers**:
   - Standard deviation is sensitive to outliers. Extreme values can significantly increase the standard deviation, indicating a larger spread in the data.

4. **Relation to Variance**:
   - The standard deviation is the square root of the variance. Variance is another measure of spread, defined as:
     $\[
     \text{Variance} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2
     \]$
     and
     $\[
     \text{Standard Deviation} = \sqrt{\text{Variance}}
     \]$

### Example Calculation

Consider a dataset: $\( 5, 7, 3, 9, 6 \)$.

1. **Calculate the Mean**:
   $\[
   \bar{x} = \frac{5 + 7 + 3 + 9 + 6}{5} = \frac{30}{5} = 6
   \]$

2. **Calculate the Variance**:
   $\[
   \text{Variance} = \frac{1}{5} [(5-6)^2 + (7-6)^2 + (3-6)^2 + (9-6)^2 + (6-6)^2]
   \]$
   $\[
   = \frac{1}{5} [(-1)^2 + 1^2 + (-3)^2 + 3^2 + 0^2]
   \]$
   $\[
   = \frac{1}{5} [1 + 1 + 9 + 9 + 0]
   \]$
   $\[
   = \frac{20}{5} = 4
   \]$

3. **Calculate the Standard Deviation**:
   $\[
   \text{Standard Deviation} = \sqrt{4} = 2
   \]$

### Applications

1. **Descriptive Statistics**:
   - Standard deviation provides a measure of the spread or variability in a dataset, complementing the mean.

2. **Quality Control**:
   - In manufacturing and quality control, standard deviation is used to monitor the consistency of products and processes.

3. **Finance**:
   - In finance, standard deviation is used to measure the volatility or risk of investment returns.

4. **Psychometrics**:
   - In psychometrics and educational testing, standard deviation is used to interpret test scores and assess the spread of scores within a population.

### Summary

The standard deviation is a fundamental statistical measure that quantifies the amount of variation or dispersion in a dataset. It is used in various fields to understand the spread of data, assess consistency, and make informed decisions based on data variability.
