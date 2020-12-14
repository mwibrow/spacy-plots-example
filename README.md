# SpaCy training plots 

This repository provides a simple example of providing
real-times plots of training statistics (loss, precision, recall and f-score)
during training.

## Usage

Install the reqirements using `pipenv install` and then activate the resulting
virtual environment using `pipenv shell` (or your favorite method).

The `train_textcat.py` script can then be executed directly (after making it executable)
or using `python3 train_textcat.py`. 
An extra `p` command line flag has been added. Plots will only be shown
if this flag is present, for example:

```
$ python3 train-textcat.py -p
```

If plots are being shown, the script will pause at the end until the plot window is closed.

 