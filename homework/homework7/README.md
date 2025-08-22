# Summary
## Methods/Thresholds

The methods to mask were both the outliers in z-score and outliers in IQR. The threshold for z was 3 as that excludes around 1% siginificance data. Thus taking the model from what is shown in the figure 1 to what is shown in figure 2. We can see that the use of the thresholds and masking our data becomes significantly less skewed and more centralized to the natural average.

	      all	    filtered_iqr

mean	-0.001434	-0.000039

median	-0.000187	-0.000100

std	     0.040579	 0.009443


As we can see with the difference in data post filtering the mean and median have a much lower difference and the St.D varies significantly less. This is shown in also in the histogram as it goes from a tri-variate pattern to much more normal distribution. 

## Write up

The filtering that we used can have great significance in our data and can also hinder us heavily. Knowing when to filter outliers is going to be crucial to the work that we do in the future of the program. If I filter my data too heavily we could be accepting averages that are not correct or even figures that are missing underlying patterns. Thus ensuring that the data removed should be removed and won't skew our results in the negative will be the most important part of our results!