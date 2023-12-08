## Machine Learning 101

#### Steps For Machine Learning

1. Import the data 📥
   - Ex: From a csv file
2. Clean the data 🧼
   - **Data Cleaning**: the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset
3. Split the data ✂️
   - Divide data into _training set_ and _test set_
     - <u>Training Set</u>: a subset of data to **train** a model
     - <u>Test Set</u>: a subset of data to **test** the trained model
4. Create a Model 🤖
   - <u>Model</u>: a program that can find _patterns_ or make _decisions_ from a previously unseen dataset
   - Usually import an algorithm via a library like [scikit-learn](https://scikit-learn.org/stable/)
5. Check the output 👀
   - against the _test set_
6. Improve 📈
   - based on output, adjust model, test again

---

#### Key Notes:

- More Data 📊 = Better Model 👍🏼
- Hardest part in machine learning: capturing good, large datasets
- Large companies, like Amazon, Facebook, Google, have access to big data hence why they tend to be pioneers of machine learning
- Big companies' models/algorithms are accessible but **data is kept private** 🔒

---

#### Helpful Tools:

- NumPy

  - Library that helps us use multidimensional arrays
  - Must for machine learning with Python

- Pandas

  - Used for data analysis
  - Allows us functionality to manipulate data in tabular structure (with rows and columns)
  - Extracts data from CSV to dataframes

- SciKit-learn

  - Pre built with different algorithms such as classification, regression, and clusetering

- matplotlib

  - Charting libaray: helps us vizualize data in a digestible way

- jupyter notebooks

  - Allows us to step through our code, see visualizations, run code separately
  - Standard to use in data science and machine learning field
  - Anaconda gives us access to jupyter notebooks

- kaggle
  - Has free datasets available
