# data_selector
Python package for selecting data manually on a scatter plot.

Source: https://plotly.com/python/v3/selection-events/?_gl=1*1mrgxu1*_ga*MTg2MDIwODQ1Ny4xNzAwNjYwNzI0*_ga_6G7EE0JNSC*MTcwMDY2NTk1Ni4yLjEuMTcwMDY2NjExOS42MC4wLjA.



# LassoDataSelector Usage Guide

The `LassoDataSelector` is a feature of the `data_selector` package, providing an interactive way to select data from a scatter plot using a lasso tool. This guide describes how to use the `LassoDataSelector` in your projects.

## Installation

Install the `data_selector` package using pip:

```bash
pip install git+https://github.com/WEILMAX/data_selector.git
```

## Usage

Follow these steps to use the `LassoDataSelector`:

1. **Import the Class:**

   Import the `LassoDataSelector` class from the `data_selector` package.

   ```python
   from data_selector.lasso_data_selector import LassoDataSelector
   ```

2. **Create an Instance:**

    Create an instance of LassoDataSelector.
    You'll need to pass your DataFrame as an argument, and you can optionally specify the figure size and marker size.

    ```python
    # Assuming 'df' is your DataFrame
    selector = LassoDataSelector(df, fig_size=(1200, 600), marker_size=2)
    ```

3. **Display the Selector:**

    Call the select_data method to display the interactive scatter plot.
    This plot allows you to select data using the lasso tool.

    ```python
    display(selector.select_data())
    ```

## Attributes

The `LassoDataSelector` class provides several attributes to access the data selected through the interactive scatter plot:

- `selected_data`: This attribute holds the DataFrame of the data currently selected in the scatter plot. It updates dynamically as new selections are made.

- `confirmed_data`: This attribute contains the DataFrame of the last confirmed data. It represents the data that was selected when the user last clicked the 'Confirm Selection' button.

- `all_confirmed_data`: This attribute is a dictionary of DataFrames, where each entry corresponds to a set of data confirmed by the user at different times. Every time the user clicks 'Confirm Selection', the selected data at that moment is stored as a new entry in this dictionary.

## Example

Below is a complete example demonstrating how to use the `LassoDataSelector` in your project
(the notebooks folder contains this example with a synthetic dataset):

```python
from data_selector.lasso_data_selector import LassoDataSelector

# Replace 'df' with your DataFrame
selector = LassoDataSelector(df, fig_size=(1200, 600), marker_size=2)

# Display the interactive scatter plot for data selection
display(selector.select_data())

# After making a selection and clicking 'Confirm Selection',
# you can access the selected data in various ways:

# The data currently selected in the plot
current_data = selector.selected_data

# The last set of data confirmed by the user
last_confirmed_data = selector.confirmed_data

# All sets of data confirmed by the user over time
all_confirmed_data = selector.all_confirmed_data

#transform all selected data into one dataframe
selected_data = pd.concat([selector.all_confirmed_data[i] for i in list(selector.all_confirmed_data.keys())])
```

# DashLassoDataSelector Usage Guide
A dash implementation exists when handling large datasets as this can be slow in plotly on the local computer

## Example

Below is a complete example demonstrating how to use the `DashLassoDataSelector` in your project
(the notebooks folder contains this example with a synthetic dataset):

```python
from data_selector.dash_lasso_data_selector import DashLassoDataSelector
import dash

# Create a Dash app instance
app = dash.Dash(__name__)

# Create a DashLassoDataSelector instance and run it
# Replace 'df' with your DataFrame
dash_app = DashLassoDataSelector(df, app, fig_size=(1600, 600), marker_size=5,port=8000)
dash_app.run()

# After making a selection and clicking 'Confirm Selection',
# you can access the selected data in various ways:

# The data currently selected in the plot
current_data = dash_app.selected_data

# The last set of data confirmed by the user
last_confirmed_data = dash_app.confirmed_data

# All sets of data confirmed by the user over time
all_confirmed_data = dash_app.all_confirmed_data

#transform all selected data into one dataframe
selected_data = pd.concat([dash_app.all_confirmed_data[i] for i in list(dash_app.all_confirmed_data.keys())])
```